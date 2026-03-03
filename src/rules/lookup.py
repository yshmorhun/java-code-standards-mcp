from typing import List

from src.rules.base import Rule

CATEGORY = "Lookup Logic"

RULES: List[Rule] = [
    Rule(
        id="LOOKUP_001",
        category=CATEGORY,
        tags=["collections", "structure", "switch"],
        name="No Switch-Based Lookup Tables",
        description="Using switch or long if-else chains as lookup tables is forbidden. Use Map data structures instead.",
        wrong_example="""default String getCountryName(Integer siteCode) {
    return switch (siteCode) {
        case 0 -> "USA";
        case 3 -> "UK";
        case 15 -> "Australia";
        default -> "Site " + siteCode;
    };
}""",
        correct_example="""private static final Map<Integer, String> SITE_COUNTRIES = Map.of(
    0, "USA",
    3, "UK",
    15, "Australia"
);

default String getCountryName(Integer siteCode) {
    if (siteCode == null) return null;
    return SITE_COUNTRIES.getOrDefault(siteCode, "Site " + siteCode);
}"""
    ),
]
