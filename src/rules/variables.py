from typing import List

from src.rules.base import Rule

CATEGORY = "Variables"

RULES: List[Rule] = [
    Rule(
        id="VAR_001",
        category=CATEGORY,
        tags=["declarations", "type-inference"],
        name="No var Declarations",
        description="Usage of 'var' for local variable declarations is forbidden. Use explicit, concrete types.",
        wrong_example="""var count = 10;
var user = userService.findById(id);
var map = new HashMap<String, List<User>>();""",
        correct_example="""int count = 10;
User user = userService.findById(id);
Map<String, List<User>> map = new HashMap<>();"""
    ),
    Rule(
        id="VAR_002",
        category=CATEGORY,
        tags=["naming", "formatting"],
        name="Variable Naming Convention",
        description="Variables must use lowerCamelCase. No underscores, prefixes, or Hungarian notation. Abbreviations treated as words.",
        wrong_example="""int item_count;
String userID;
HttpRequest HTTPRequest;""",
        correct_example="""int itemCount;
String userId;
HttpRequest httpRequest;"""
    ),
    Rule(
        id="VAR_003",
        category=CATEGORY,
        tags=["naming", "semantics"],
        name="Semantic Variable Naming",
        description="Variable names must clearly describe what the object represents. Generic names forbidden: data, info, value, object, result, temp, item, list, map, set.",
        wrong_example="""String data;
String value;
List<User> list;
Map<String, String> map;""",
        correct_example="""String countryCode;
String orderStatus;
List<User> activeUsers;
Map<String, String> countryByCode;"""
    ),
    Rule(
        id="VAR_004",
        category=CATEGORY,
        tags=["naming", "collections"],
        name="Collection Variable Naming",
        description="Collections must use plural names. Maps must describe key -> value relationship.",
        wrong_example="""List<User> user;
Map<String, Order> orders;""",
        correct_example="""List<User> users;
Map<String, Order> orderById;"""
    ),
    Rule(
        id="VAR_005",
        category=CATEGORY,
        tags=["naming", "boolean"],
        name="Boolean Naming",
        description="Boolean variables must start with is, has, or can.",
        wrong_example="""boolean active;
boolean permission;
boolean retry;""",
        correct_example="""boolean isActive;
boolean hasPermission;
boolean canRetry;"""
    ),
]
