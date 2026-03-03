from typing import List
from typing import Optional

from src.rules.base import Rule
from src.rules.dto import RULES as DTO_RULES
from src.rules.formatting import RULES as FORMATTING_RULES
from src.rules.imports import RULES as IMPORTS_RULES
from src.rules.lookup import RULES as LOOKUP_RULES
from src.rules.time_and_date import RULES as TIME_RULES
from src.rules.variables import RULES as VARIABLES_RULES

JAVA_RULES: List[Rule] = [
    *FORMATTING_RULES,
    *IMPORTS_RULES,
    *LOOKUP_RULES,
    *VARIABLES_RULES,
    *TIME_RULES,
    *DTO_RULES,
]


def get_rules_by_category(category: str) -> List[Rule]:
    return [rule for rule in JAVA_RULES if rule.category.lower() == category.lower()]


def get_rules_by_tag(tag: str) -> List[Rule]:
    return [rule for rule in JAVA_RULES if tag.lower() in [t.lower() for t in rule.tags]]


def get_rules_filtered(
    categories: Optional[List[str]] = None,
    tags: Optional[List[str]] = None
) -> List[Rule]:
    if not categories and not tags:
        return JAVA_RULES

    matched_ids: set = set()

    if categories:
        categories_lower = {c.lower() for c in categories}
        matched_ids |= {r.id for r in JAVA_RULES if r.category.lower() in categories_lower}

    if tags:
        tags_lower = {t.lower() for t in tags}
        matched_ids |= {r.id for r in JAVA_RULES if any(t.lower() in tags_lower for t in r.tags)}

    return [r for r in JAVA_RULES if r.id in matched_ids]


def get_all_categories() -> List[str]:
    return sorted(set(rule.category for rule in JAVA_RULES))


def get_all_tags() -> List[str]:
    tags = set()
    for rule in JAVA_RULES:
        tags.update(rule.tags)
    return sorted(tags)


def get_rule_by_id(rule_id: str) -> Rule | None:
    for rule in JAVA_RULES:
        if rule.id == rule_id:
            return rule
    return None
