"""Validate the distributable skill, its metadata, and local Markdown links."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


def validate(root: Path) -> list[str]:
    errors = []
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if len(skills) != 1:
        return [f"Expected one installable skill, found {len(skills)}"]

    manifest = skills[0]
    skill = manifest.parent
    text = manifest.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.S)
    if not frontmatter:
        return ["SKILL.md must begin with YAML frontmatter"]
    data = yaml.safe_load(frontmatter.group(1))
    if not isinstance(data, dict):
        return ["Skill frontmatter must be a mapping"]

    name = data.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("Skill name must use lowercase letters, digits, and single hyphens")
    elif len(name) > 64 or name != skill.name:
        errors.append("Skill name must match its directory and be at most 64 characters")
    description = data.get("description")
    if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
        errors.append("Description must contain 1–1024 characters")
    if not text[frontmatter.end():].strip():
        errors.append("Skill body is empty")

    for required in ("LICENSE", "THIRD_PARTY_NOTICES.md", "agents/openai.yaml"):
        if not (skill / required).is_file():
            errors.append(f"Missing installable resource: {required}")
    if (skill / "LICENSE").is_file() and (root / "LICENSE").is_file():
        if (skill / "LICENSE").read_bytes() != (root / "LICENSE").read_bytes():
            errors.append("Root and installable licenses differ")
    else:
        errors.append("Both the root and installable skill need a license")

    interface_path = skill / "agents" / "openai.yaml"
    if interface_path.is_file():
        interface = yaml.safe_load(interface_path.read_text(encoding="utf-8"))
        interface = interface.get("interface", {}) if isinstance(interface, dict) else {}
        for key in ("display_name", "short_description", "default_prompt"):
            if not isinstance(interface.get(key), str) or not interface[key].strip():
                errors.append(f"Missing UI metadata: {key}")
        if isinstance(name, str) and f"${name}" not in interface.get("default_prompt", ""):
            errors.append("The default prompt must invoke the packaged skill name")

    # Installed references must stay inside the copied skill. Repository docs may
    # link elsewhere in the repository. Fragments and remote URLs are not fetched.
    markdown = list(root.glob("*.md")) + list((root / "tests").glob("*.md"))
    markdown += list(skill.rglob("*.md"))
    for document in markdown:
        body = document.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", body):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (document.parent / unquote(parsed.path)).resolve()
            boundary = skill if document.is_relative_to(skill) else root
            if not destination.is_relative_to(boundary):
                errors.append(f"Reference escapes its distributable folder: {document.name}: {target}")
            elif not destination.exists():
                errors.append(f"Broken local reference: {document.name}: {target}")
    return errors


if __name__ == "__main__":
    project = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    try:
        failures = validate(project)
    except (OSError, UnicodeError, yaml.YAMLError) as error:
        failures = [str(error)]
    for failure in failures:
        print(f"ERROR: {failure}")
    if failures:
        sys.exit(1)
    print("PASS: skill metadata, bundled resources, license consistency, and local references")
