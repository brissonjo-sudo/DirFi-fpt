"""Validation statique reproductible du dépôt dirfi-fpt.

Ce script ne dépend que de la bibliothèque standard (aucun ``pip install``).
Il retourne 0 si tous les contrôles passent, 1 sinon, et affiche un
récapitulatif lisible en français.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "dirfi-fpt"

# Invariants de garde-fou : chaînes devant apparaître verbatim dans SKILL.md.
# Ce sont les deux "hard stops" (§5.2 et §5.3) et la frontière drh-fpt (§5.5) :
# l'invariant central de sûreté de ce skill.
REQUIRED_GUARDRAIL_SNIPPETS = (
    "STOP — Ce montage fait manier des deniers publics",
    "ALERTE BUDGÉTAIRE",
    "BASCULE drh-fpt",
    "gestion de fait",
    "ne vaut pas bascule",
    "comptable public assignataire",
)

# Fichiers .md attendus à la racine de references/ (hors references/templates/).
EXPECTED_REFERENCE_FILES = {
    "analyse-situation.md",
    "_gabarit-branche.md",
    "socle-sources-verification.md",
    "references-verifiees.md",
    "cache-taux-seuils.md",
    "budget-cycle.md",
    "nomenclature-m57.md",
    "execution-depense.md",
    "execution-recette.md",
    "fiscalite-locale.md",
    "dotations-perequation.md",
    "dette-tresorerie.md",
    "prospective-analyse.md",
    "subventions.md",
    "commande-publique-financiere.md",
    "controle-interne-financier.md",
    "ecrits-financiers.md",
    "controle-budgetaire.md",
    "contentieux-financier.md",
    "retex.md",
}
EXPECTED_TEMPLATES_COUNT = 5
EXPECTED_OBJETS_COUNT = 9
MIN_TEST_CASES = 24
MIN_ATTENDUS = 4

# Identifiants Légifrance en dur interdits hors registre vérifié : c'est
# l'invariant anti-hallucination central de ce skill (§5.4 du SKILL.md).
LEGIFRANCE_ID_PATTERN = re.compile(r"\b(?:LEGIARTI|JORFTEXT|CETATEXT)\d+\b")
LEGIFRANCE_REGISTRY = Path("references/references-verifiees.md")

# Anti-PII : IBAN français, NIR, adresse e-mail.
IBAN_FR_PATTERN = re.compile(r"\bFR\d{2}(?:[ -]?[0-9A-Z]){23}\b", re.IGNORECASE)
NIR_PATTERN = re.compile(
    r"(?<!\d)[12][ -]?\d{2}[ -]?(?:0[1-9]|1[0-2])[ -]?(?:2[AB]|\d{2})"
    r"[ -]?\d{3}[ -]?\d{3}[ -]?\d{2}(?!\d)",
    re.IGNORECASE,
)
EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
EMAIL_ALLOWED_EXACT = {"noreply@anthropic.com"}
EMAIL_ALLOWED_DOMAIN_SUFFIX = ".gouv.fr"

VERSION_TITLE_PATTERN = re.compile(
    r"#\s*Skill\s*:\s*" + re.escape(SKILL_NAME) + r"\s*\(v(\d+\.\d+\.\d+)\)"
)


class Validation:
    """Collecte les erreurs et avertissements sans interrompre les contrôles."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checks = 0

    def require(self, condition: bool, message: str) -> None:
        """Enregistre une exigence bloquante et son éventuel échec."""
        self.checks += 1
        if not condition:
            self.errors.append(message)

    def warn(self, condition: bool, message: str) -> None:
        """Enregistre un avertissement non bloquant."""
        self.checks += 1
        if not condition:
            self.warnings.append(message)


def read_text(path: Path) -> str:
    """Lit un fichier UTF-8."""
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse le frontmatter simple de SKILL.md sans dépendance externe."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    raw = text[4:end]
    fields: dict[str, str] = {}
    current: str | None = None
    for line in raw.splitlines():
        match = re.match(r"^([a-z_]+):(?:\s*(.*))?$", line)
        if match:
            current = match.group(1)
            value = match.group(2) or ""
            fields[current] = "" if value in {">-", "|-"} else value
        elif current and line.startswith("  "):
            fields[current] = f"{fields[current]} {line.strip()}".strip()
    return fields


def runtime_markdown_files() -> list[Path]:
    """Retourne les fichiers Markdown réellement chargés par le skill."""
    files: list[Path] = []
    skill = ROOT / "SKILL.md"
    if skill.is_file():
        files.append(skill)
    for directory in ("references", "objets"):
        base = ROOT / directory
        if base.is_dir():
            files.extend(sorted(base.rglob("*.md")))
    return files


def validate_frontmatter(validation: Validation) -> None:
    """Valide le contrat minimal du frontmatter du skill."""
    skill_path = ROOT / "SKILL.md"
    if not skill_path.is_file():
        validation.require(False, "SKILL.md : fichier absent")
        return
    skill = read_text(skill_path)
    fields = parse_frontmatter(skill)
    validation.require(
        set(fields) == {"name", "description"},
        "SKILL.md : le frontmatter doit contenir exactement name et description "
        f"(trouvé : {sorted(fields) or 'aucun'})",
    )
    validation.require(
        fields.get("name") == SKILL_NAME,
        f"SKILL.md : name invalide (attendu {SKILL_NAME!r}, trouvé {fields.get('name')!r})",
    )
    description = fields.get("description", "")
    validation.require(
        1 <= len(description) <= 1024,
        f"SKILL.md : description hors limite (longueur {len(description)})",
    )


def validate_guardrail_invariants(validation: Validation) -> None:
    """Vérifie que les garde-fous non négociables restent verbatim dans SKILL.md."""
    skill_path = ROOT / "SKILL.md"
    if not skill_path.is_file():
        validation.require(False, "SKILL.md : fichier absent pour le contrôle des garde-fous")
        return
    skill = read_text(skill_path)
    for snippet in REQUIRED_GUARDRAIL_SNIPPETS:
        validation.require(
            snippet in skill,
            f"SKILL.md : invariant de garde-fou absent (verbatim requis) : {snippet!r}",
        )


def extract_skill_version() -> str | None:
    """Extrait la version depuis le titre de SKILL.md (# Skill : dirfi-fpt (vX.Y.Z))."""
    skill_path = ROOT / "SKILL.md"
    if not skill_path.is_file():
        return None
    match = VERSION_TITLE_PATTERN.search(read_text(skill_path))
    return match.group(1) if match else None


def validate_versions(validation: Validation) -> None:
    """Vérifie l'alignement de la version courante entre les fichiers du dépôt.

    La version de référence est lue depuis le titre de SKILL.md, plutôt que
    codée en dur, pour que ce contrôle reste valable après un bump de version.
    """
    version = extract_skill_version()
    validation.require(
        version is not None,
        "SKILL.md : titre de version introuvable (attendu : # Skill : "
        f"{SKILL_NAME} (vX.Y.Z))",
    )
    if version is None:
        return

    skill_path = ROOT / "SKILL.md"
    skill_text = read_text(skill_path)
    validation.require(
        f"(v{version})" in skill_text,
        f"SKILL.md : motif (v{version}) absent du corps du document",
    )
    validation.require(
        f"version : **{version}**" in skill_text,
        f"SKILL.md : motif 'version : **{version}**' absent des métadonnées",
    )

    expected = {
        ROOT / "README.md": f"v{version}",
        ROOT / "CHANGELOG.md": f"[{version}]",
        ROOT / "vault" / "index-dirfi-fpt.md": f"version: {version}",
    }
    for path, marker in expected.items():
        if not path.is_file():
            validation.require(False, f"{path.relative_to(ROOT)} : fichier absent")
            continue
        validation.require(
            marker in read_text(path),
            f"{path.relative_to(ROOT)} : marqueur de version {marker!r} absent",
        )


def validate_runtime_file_inventory(validation: Validation) -> None:
    """Vérifie l'inventaire exact des fichiers runtime attendus."""
    references_dir = ROOT / "references"
    if references_dir.is_dir():
        present = {path.name for path in references_dir.glob("*.md")}
        missing = EXPECTED_REFERENCE_FILES - present
        unexpected = present - EXPECTED_REFERENCE_FILES
        for name in sorted(missing):
            validation.require(False, f"references/{name} : fichier manquant")
        for name in sorted(unexpected):
            validation.require(False, f"references/{name} : fichier inattendu")
        if not missing and not unexpected:
            validation.checks += 1
    else:
        validation.require(False, "references/ : dossier absent")

    templates_dir = ROOT / "references" / "templates"
    if templates_dir.is_dir():
        templates = sorted(templates_dir.glob("*.md"))
        validation.require(
            len(templates) == EXPECTED_TEMPLATES_COUNT,
            f"references/templates/ : {len(templates)} fichier(s) au lieu de "
            f"{EXPECTED_TEMPLATES_COUNT}",
        )
    else:
        validation.require(False, "references/templates/ : dossier absent")

    objets_dir = ROOT / "objets"
    if objets_dir.is_dir():
        objets = sorted(objets_dir.glob("*.md"))
        validation.require(
            len(objets) == EXPECTED_OBJETS_COUNT,
            f"objets/ : {len(objets)} fichier(s) au lieu de {EXPECTED_OBJETS_COUNT}",
        )
        validation.require(
            (objets_dir / "_gabarit-objet.md").is_file(),
            "objets/_gabarit-objet.md : gabarit absent",
        )
    else:
        validation.require(False, "objets/ : dossier absent")

    validation.require(
        not (ROOT / "assets").exists(),
        "assets/ : ce dossier ne doit pas exister",
    )


def validate_cases(validation: Validation) -> None:
    """Valide le schéma et la couverture minimale des cas de test structurés.

    Ce fichier est produit par un autre lot de travail : son absence à ce
    stade n'est qu'un avertissement non bloquant, pas une erreur.
    """
    path = ROOT / "tests" / "cas-de-test.json"
    if not path.is_file():
        validation.warn(False, "tests/cas-de-test.json : fichier absent (autre lot en cours)")
        return

    try:
        cases = json.loads(read_text(path))
    except json.JSONDecodeError as error:
        validation.require(False, f"tests/cas-de-test.json : JSON invalide ({error})")
        return

    validation.require(isinstance(cases, list), "tests/cas-de-test.json : racine non-liste")
    if not isinstance(cases, list):
        return

    validation.require(
        len(cases) >= MIN_TEST_CASES,
        f"tests/cas-de-test.json : {len(cases)} cas au lieu d'au moins {MIN_TEST_CASES}",
    )

    identifiers: list[str] = []
    expected_keys = {"id", "branche", "type", "prompt", "attendus"}
    for index, case in enumerate(cases, start=1):
        validation.require(
            isinstance(case, dict) and set(case) == expected_keys,
            f"cas {index} : schéma invalide (attendu {sorted(expected_keys)})",
        )
        if not isinstance(case, dict):
            continue
        identifier = case.get("id")
        if isinstance(identifier, str):
            identifiers.append(identifier)
        validation.require(bool(case.get("branche")), f"cas {index} : branche vide")
        validation.require(bool(case.get("type")), f"cas {index} : type vide")
        validation.require(bool(case.get("prompt")), f"cas {index} : prompt vide")
        attendus = case.get("attendus")
        validation.require(
            isinstance(attendus, list) and len(attendus) >= MIN_ATTENDUS,
            f"cas {index} : attendus insuffisants (au moins {MIN_ATTENDUS} requis)",
        )

    validation.require(
        len(identifiers) == len(set(identifiers)),
        "tests/cas-de-test.json : identifiants dupliqués",
    )


def extract_markdown_targets(text: str) -> set[str]:
    """Extrait les chemins Markdown locaux cités en backticks ou en lien."""
    targets = set(re.findall(r"`([^`\n]+\.md(?:#[^`\n]+)?)`", text))
    targets.update(re.findall(r"\[[^\]]+\]\(([^)\n]+\.md(?:#[^)\n]+)?)\)", text))
    return targets


def target_exists(source: Path, target: str) -> bool:
    """Résout un lien local selon l'ordre de résolution imposé.

    Ordre : relatif au fichier source, puis racine du dépôt, puis
    references/, puis references/templates/, puis objets/.
    """
    clean = target.split("#", 1)[0].replace("\\", "/")
    if not clean or "*" in clean:
        return True
    if clean.startswith(("http://", "https://")):
        return True
    candidates = (
        source.parent / clean,
        ROOT / clean,
        ROOT / "references" / clean,
        ROOT / "references" / "templates" / clean,
        ROOT / "objets" / clean,
    )
    return any(candidate.resolve().is_file() for candidate in candidates)


def validate_runtime_links(validation: Validation) -> None:
    """Vérifie que chaque lien Markdown local cité pointe vers un fichier existant."""
    for path in runtime_markdown_files():
        for target in extract_markdown_targets(read_text(path)):
            validation.require(
                target_exists(path, target),
                f"{path.relative_to(ROOT)} : lien local introuvable ({target})",
            )


def validate_forbidden_content(validation: Validation) -> None:
    """Interdit tout identifiant Légifrance en dur hors du registre vérifié."""
    for path in runtime_markdown_files():
        relative = path.relative_to(ROOT)
        if relative == LEGIFRANCE_REGISTRY:
            continue
        matches = LEGIFRANCE_ID_PATTERN.findall(read_text(path))
        validation.require(
            not matches,
            f"{relative} : identifiant Légifrance en dur interdit hors registre "
            f"vérifié ({', '.join(sorted(set(matches)))})",
        )


def is_allowed_email(email: str) -> bool:
    """Détermine si une adresse e-mail détectée est explicitement tolérée."""
    if email.lower() in EMAIL_ALLOWED_EXACT:
        return True
    return email.lower().endswith(EMAIL_ALLOWED_DOMAIN_SUFFIX)


def validate_anti_pii(validation: Validation) -> None:
    """Recherche IBAN, NIR et adresses e-mail dans tous les fichiers .md du dépôt."""
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = read_text(path)
        relative = path.relative_to(ROOT)

        ibans = IBAN_FR_PATTERN.findall(text)
        validation.require(not ibans, f"{relative} : IBAN français détecté")

        nirs = NIR_PATTERN.findall(text)
        validation.require(not nirs, f"{relative} : numéro de sécurité sociale détecté")

        emails = [m for m in EMAIL_PATTERN.findall(text) if not is_allowed_email(m)]
        validation.require(
            not emails,
            f"{relative} : adresse e-mail détectée ({', '.join(sorted(set(emails)))})",
        )


def validate_plugin_adapter(validation: Validation) -> None:
    """Vérifie l'adaptateur de plugin et sa cohérence avec le noyau.

    Le paquet plugin expose le skill via ``skills/<nom>/SKILL.md``, qui ne
    duplique pas le noyau mais doit en porter exactement le même frontmatter :
    une divergence ferait déclencher le skill sur un périmètre différent selon
    le mode d'installation, sans que rien ne le signale.
    """
    adapter_path = ROOT / "skills" / SKILL_NAME / "SKILL.md"
    skill_path = ROOT / "SKILL.md"
    if not adapter_path.is_file():
        validation.require(False, f"skills/{SKILL_NAME}/SKILL.md : adaptateur de plugin absent")
        return
    if not skill_path.is_file():
        return
    adapter_fields = parse_frontmatter(read_text(adapter_path))
    skill_fields = parse_frontmatter(read_text(skill_path))
    validation.require(
        adapter_fields == skill_fields,
        f"skills/{SKILL_NAME}/SKILL.md : le frontmatter diverge de celui de SKILL.md",
    )
    body = read_text(adapter_path)
    validation.require(
        "../../SKILL.md" in body,
        f"skills/{SKILL_NAME}/SKILL.md : l'adaptateur doit renvoyer vers ../../SKILL.md",
    )


def main() -> int:
    """Exécute tous les contrôles et retourne un code compatible CI."""
    validation = Validation()
    validate_frontmatter(validation)
    validate_plugin_adapter(validation)
    validate_guardrail_invariants(validation)
    validate_versions(validation)
    validate_runtime_file_inventory(validation)
    validate_cases(validation)
    validate_runtime_links(validation)
    validate_forbidden_content(validation)
    validate_anti_pii(validation)

    for warning in validation.warnings:
        print(f"[AVERTISSEMENT] {warning}")

    if validation.errors:
        for error in validation.errors:
            print(f"[ÉCHEC] {error}")
        print(
            f"[ÉCHEC] {len(validation.errors)} erreur(s), "
            f"{len(validation.warnings)} avertissement(s), {validation.checks} contrôles"
        )
        return 1

    print(
        f"[OK] {validation.checks} contrôles statiques réussis "
        f"({len(validation.warnings)} avertissement(s) non bloquant(s))"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
