from typing import List

from src.rules.base import Rule

CATEGORY = "Time and Date"

RULES: List[Rule] = [
    Rule(
        id="TIME_001",
        category=CATEGORY,
        tags=["time", "types", "declarations"],
        name="No String or Numeric Timestamps",
        description="Time values must not be String, Long, or Integer. All time fields must use LocalDateTime.",
        wrong_example="""public class Response {
    private String timestamp;
    private Long createdAt;
}""",
        correct_example="""public class Response {
    private LocalDateTime timestamp;
    private LocalDateTime createdAt;
}"""
    ),
    Rule(
        id="TIME_002",
        category=CATEGORY,
        tags=["time", "conversion", "boundary"],
        name="External Input Conversion",
        description="External time values must be converted immediately to LocalDateTime at the boundary. Raw timestamps must not propagate into business logic.",
        wrong_example="""process(timestampString);
save(timestampLong);""",
        correct_example="""LocalDateTime timestamp = LocalDateTime.parse(externalTimestamp);
process(timestamp);

// For epoch:
LocalDateTime timestamp = Instant.ofEpochMilli(epochMillis)
    .atZone(ZoneId.systemDefault())
    .toLocalDateTime();"""
    ),
]
