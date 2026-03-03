from fastmcp import FastMCP
from pydantic import ValidationError

from src.rules import JAVA_RULES
from src.rules import get_all_categories
from src.rules import get_all_tags
from src.rules import get_rule_by_id
from src.rules import get_rules_by_tag
from src.rules import get_rules_filtered
from src.validators import GetJavaRulesRequest
from src.validators import GetRuleDetailsRequest
from src.validators import format_validation_error

mcp = FastMCP("java-code-standards")


@mcp.tool()
def get_java_rules(
    categories: list[str] = None,
    tags: list[str] = None
) -> dict:
    """Get Java coding standards rules filtered by categories and/or tags (OR logic).

    When both parameters are provided, rules matching EITHER categories OR tags are returned.
    Omit both to get all rules.

    Args:
        categories: List of categories to filter by (e.g., ["Variables", "DTO"]).
        tags: List of tags to filter by (e.g., ["naming", "lombok"]).

    Returns:
        List of rules with examples.
    """
    try:
        validated = GetJavaRulesRequest(categories=categories, tags=tags)
    except ValidationError as e:
        return format_validation_error(e)

    rules = get_rules_filtered(
        categories=validated.categories,
        tags=validated.tags
    )

    if not rules:
        return {
            "status": "error",
            "message": f"No rules found for categories={categories}, tags={tags}",
            "available_categories": get_all_categories(),
            "available_tags": get_all_tags()
        }

    rules_data = [
        {
            "id": r.id,
            "category": r.category,
            "tags": r.tags,
            "name": r.name,
            "description": r.description,
            "wrong_example": r.wrong_example,
            "correct_example": r.correct_example
        }
        for r in rules
    ]

    return {
        "status": "ok",
        "rules_count": len(rules_data),
        "rules": rules_data
    }


@mcp.tool()
def get_rule_details(rule_ids: list[str]) -> dict:
    """Get detailed information about one or more rules.

    Args:
        rule_ids: List of rule identifiers (e.g., ["FORMAT_001"] or ["VAR_001", "VAR_002", "DTO_001"]).

    Returns:
        Rule details with description and examples.
    """
    try:
        validated = GetRuleDetailsRequest(rule_ids=rule_ids)
    except ValidationError as e:
        return format_validation_error(e)

    rules_data = []
    not_found = []

    for rule_id in validated.rule_ids:
        rule = get_rule_by_id(rule_id)
        if rule:
            rules_data.append({
                "id": rule.id,
                "category": rule.category,
                "tags": rule.tags,
                "name": rule.name,
                "description": rule.description,
                "wrong_example": rule.wrong_example,
                "correct_example": rule.correct_example
            })
        else:
            not_found.append(rule_id)

    if not rules_data:
        return {
            "status": "error",
            "message": f"No rules found for ids: {not_found}",
            "available_rules": [r.id for r in JAVA_RULES]
        }

    result = {
        "status": "ok",
        "rules_count": len(rules_data),
        "rules": rules_data
    }

    if not_found:
        result["not_found"] = not_found

    return result


@mcp.tool()
def list_categories() -> dict:
    """List all available rule categories with rule counts and rule names.

    Returns:
        List of categories with their rules.
    """
    categories = get_all_categories()
    category_data = {}
    for cat in categories:
        rules = get_rules_filtered(categories=[cat])
        category_data[cat] = {
            "rules_count": len(rules),
            "rules": [{"id": r.id, "name": r.name} for r in rules]
        }

    return {
        "status": "ok",
        "categories": [
            {
                "name": cat,
                "rules_count": data["rules_count"],
                "rules": data["rules"]
            }
            for cat, data in sorted(category_data.items())
        ]
    }


@mcp.tool()
def list_tags() -> dict:
    """List all available rule tags with rule counts and rule names.

    Returns:
        List of tags with their rules.
    """
    tags = get_all_tags()
    tag_data = {}
    for tag in tags:
        rules = get_rules_by_tag(tag)
        tag_data[tag] = {
            "rules_count": len(rules),
            "rules": [{"id": r.id, "name": r.name} for r in rules]
        }

    return {
        "status": "ok",
        "tags": [
            {
                "name": tag,
                "rules_count": data["rules_count"],
                "rules": data["rules"]
            }
            for tag, data in sorted(tag_data.items())
        ]
    }


if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=80)
