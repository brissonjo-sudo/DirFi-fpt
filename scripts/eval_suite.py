"""Prépare et contrôle les artefacts d'une évaluation en contextes frais."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "tests" / "cas-de-test.json"
VALID_VERDICTS = {"RÉUSSITE", "DEMI-RÉUSSITE", "ÉCHEC"}


def load_cases(path: Path = CASES_PATH) -> list[dict[str, Any]]:
    """Charge la suite structurée courante ou sa copie figée dans un run."""
    return json.loads(path.read_text(encoding="utf-8"))


def suite_digest(path: Path = CASES_PATH) -> str:
    """Calcule l'empreinte d'un fichier de suite."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frozen_suite_path(run_dir: Path) -> Path:
    """Retourne la suite figée du run, ou la suite courante pour un ancien run."""
    snapshot = run_dir / "suite.json"
    return snapshot if snapshot.is_file() else CASES_PATH


def prepare_run(
    run_dir: Path, responder: str, judge: str, cases_path: Path = CASES_PATH
) -> None:
    """Crée un run sans exposer les attendus au répondant."""
    if run_dir.exists() and any(run_dir.iterdir()):
        raise ValueError(f"Le dossier de run n'est pas vide : {run_dir}")
    run_dir.mkdir(parents=True, exist_ok=True)
    cases = load_cases(cases_path)
    (run_dir / "suite.json").write_bytes(cases_path.read_bytes())
    manifest = {
        "format_version": 1,
        "skill_version": read_skill_version(),
        "created_at": datetime.now(UTC).isoformat(),
        "suite_sha256": suite_digest(cases_path),
        "suite_source": cases_path.name,
        "responder": responder,
        "judge": judge,
        "case_count": len(cases),
        "protocol": (
            "Le répondant reçoit seulement prompt.md. Le juge reçoit ensuite "
            "response.md, les attendus du cas et tests/bareme-cas-de-test.md."
        ),
    }
    (run_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for case in cases:
        case_dir = run_dir / case_dir_name(case)
        case_dir.mkdir(parents=True, exist_ok=False)
        (case_dir / "prompt.md").write_text(case["prompt"] + "\n", encoding="utf-8")




def read_skill_version() -> str:
    """Lit la version du skill depuis le titre de SKILL.md.

    Figer la version en dur dans ce script a produit un manifeste de run
    annonçant 1.0.0 alors que le dépôt était déjà en 1.0.1 : un run est
    d'abord une mesure attachée à une version précise, et se tromper de
    version rend la mesure inexploitable.
    """
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r"^# Skill : [\w-]+ \(v([0-9]+\.[0-9]+\.[0-9]+)\)", skill, re.M)
    if not match:
        raise ValueError("Version introuvable dans le titre de SKILL.md")
    return match.group(1)


def case_dir_name(case: dict) -> str:
    """Nom de dossier d'un cas.

    L'identifiant peut être numérique dans ``cas-de-test.json`` : le convertir
    en chaîne (``Path / int`` lève une ``TypeError``) et le zéro-padder pour que
    l'ordre alphabétique des dossiers suive l'ordre des cas.
    """
    case_id = case["id"]
    if isinstance(case_id, int):
        return f"cas-{case_id:02d}"
    return str(case_id)


def validate_run(run_dir: Path) -> dict[str, int]:
    """Valide réponses et jugements, puis calcule les totaux."""
    manifest_path = run_dir / "manifest.json"
    if not manifest_path.is_file():
        raise ValueError("manifest.json absent")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    suite_path = frozen_suite_path(run_dir)
    if manifest.get("suite_sha256") != suite_digest(suite_path):
        raise ValueError("L'empreinte de la suite ne correspond plus au manifest")
    totals = {verdict: 0 for verdict in sorted(VALID_VERDICTS)}
    missing: list[str] = []
    for case in load_cases(suite_path):
        case_dir = run_dir / case_dir_name(case)
        response = case_dir / "response.md"
        judgment = case_dir / "judgment.json"
        if not response.is_file() or not response.read_text(encoding="utf-8").strip():
            missing.append(f"{case_dir_name(case)}/response.md")
        if not judgment.is_file():
            missing.append(f"{case_dir_name(case)}/judgment.json")
            continue
        data = json.loads(judgment.read_text(encoding="utf-8"))
        verdict = data.get("verdict")
        if verdict not in VALID_VERDICTS:
            raise ValueError(f"{case['id']} : verdict invalide ({verdict!r})")
        # La note explicative du juge est acceptée sous "notes" ou sous
        # "justification" : les deux intitulés ont circulé dans les consignes
        # de jugement, et refuser l'un des deux invaliderait un run complet
        # pour une question de nommage.
        note = data.get("notes") or data.get("justification")
        if not isinstance(note, str) or not note.strip():
            raise ValueError(
                f"{case['id']} : note de jugement absente "
                "(champ 'notes' ou 'justification' attendu)"
            )
        totals[verdict] += 1
    if missing:
        raise ValueError("Artefacts manquants : " + ", ".join(missing))
    return totals


def write_summary(run_dir: Path, totals: dict[str, int]) -> Path:
    """Conserve une synthèse machine-readable sans effacer les artefacts bruts."""
    output = run_dir / "summary.json"
    suite_path = frozen_suite_path(run_dir)
    payload = {
        "suite_sha256": suite_digest(suite_path),
        "case_count": sum(totals.values()),
        "totals": totals,
        "completed_at": datetime.now(UTC).isoformat(),
    }
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


def parse_args() -> argparse.Namespace:
    """Construit les sous-commandes prepare et summarize."""
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    prepare = subparsers.add_parser("prepare", help="préparer un dossier de run")
    prepare.add_argument("--run-dir", required=True, type=Path)
    prepare.add_argument("--responder", required=True)
    prepare.add_argument("--judge", required=True)
    prepare.add_argument(
        "--cases",
        type=Path,
        default=CASES_PATH,
        help="suite JSON à figer dans le run (défaut : tests/cas-de-test.json)",
    )
    summarize = subparsers.add_parser(
        "summarize", help="valider et synthétiser un run complet"
    )
    summarize.add_argument("--run-dir", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    """Exécute la sous-commande demandée avec un code compatible CI."""
    args = parse_args()
    try:
        run_dir = args.run_dir.resolve()
        if args.command == "prepare":
            prepare_run(run_dir, args.responder, args.judge, args.cases.resolve())
            print(f"[OK] Run préparé : {run_dir}")
            print("[OK] Ajouter response.md et judgment.json dans chaque dossier de cas")
        else:
            totals = validate_run(run_dir)
            output = write_summary(run_dir, totals)
            print(f"[OK] Run complet : {totals}")
            print(f"[OK] Synthèse : {output}")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"[FAIL] {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
