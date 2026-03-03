"""Input validation for MCP server tools using Pydantic."""

from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator

from src.rules import get_all_categories
from src.rules import get_all_tags
from src.rules import JAVA_RULES


class GetJavaRulesRequest(BaseModel):
    """Request model for get_java_rules tool."""

    categories: Optional[List[str]] = Field(
        default=None,
        description="List of categories to filter by"
    )
    tags: Optional[List[str]] = Field(
        default=None,
        description="List of tags to filter by"
    )

    @field_validator("categories")
    @classmethod
    def validate_categories(cls, value: Optional[List[str]]) -> Optional[List[str]]:
        if value is None:
            return None

        available = get_all_categories()
        available_lower = {c.lower(): c for c in available}

        validated = []
        for cat in value:
            if not cat or not cat.strip():
                raise ValueError("Category cannot be empty")

            cat_lower = cat.lower()
            if cat_lower not in available_lower:
                raise ValueError(f"Unknown category: '{cat}'. Available: {available}")

            validated.append(available_lower[cat_lower])

        return validated

    @field_validator("tags")
    @classmethod
    def validate_tags(cls, value: Optional[List[str]]) -> Optional[List[str]]:
        if value is None:
            return None

        available = get_all_tags()
        available_lower = {t.lower(): t for t in available}

        validated = []
        for tag in value:
            if not tag or not tag.strip():
                raise ValueError("Tag cannot be empty")

            tag_lower = tag.lower()
            if tag_lower not in available_lower:
                raise ValueError(f"Unknown tag: '{tag}'. Available: {available}")

            validated.append(available_lower[tag_lower])

        return validated


class GetRuleDetailsRequest(BaseModel):
    """Request model for get_rule_details tool."""

    rule_ids: List[str] = Field(
        ...,
        min_length=1,
        description="List of rule IDs to retrieve"
    )

    @field_validator("rule_ids")
    @classmethod
    def validate_rule_ids(cls, value: List[str]) -> List[str]:
        available_ids = {r.id for r in JAVA_RULES}
        available_upper = {r.id.upper(): r.id for r in JAVA_RULES}

        validated = []
        for rule_id in value:
            if not rule_id or not rule_id.strip():
                raise ValueError("Rule ID cannot be empty")

            if rule_id in available_ids:
                validated.append(rule_id)
            elif rule_id.upper() in available_upper:
                validated.append(available_upper[rule_id.upper()])
            else:
                sample = sorted(available_ids)[:10]
                raise ValueError(f"Unknown rule ID: '{rule_id}'. Example IDs: {sample}")

        return validated


def format_validation_error(error: Exception) -> dict:
    """Format Pydantic validation error to response dict."""
    if hasattr(error, "errors"):
        errors = [
            f"{'.'.join(str(loc) for loc in e['loc'])}: {e['msg']}"
            for e in error.errors()
        ]
    else:
        errors = [str(error)]

    return {
        "status": "validation_error",
        "errors": errors
    }
