from typing import List

from src.rules.base import Rule

CATEGORY = "Imports"

RULES: List[Rule] = [
    Rule(
        id="IMPORT_001",
        category=CATEGORY,
        tags=["imports", "static-import"],
        name="No Static Imports",
        description="'import static' is forbidden. Always use fully qualified class reference.",
        wrong_example="""import static java.lang.Math.PI;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.when;""",
        correct_example="""import java.lang.Math;
import org.junit.jupiter.api.Assertions;
import org.mockito.Mockito;"""
    ),
    Rule(
        id="IMPORT_002",
        category=CATEGORY,
        tags=["imports", "wildcard-import"],
        name="No Wildcard Imports",
        description="'import package.*' is forbidden. Every imported class must be listed explicitly.",
        wrong_example="""import java.util.*;
import com.example.service.*;""",
        correct_example="""import java.util.List;
import java.util.Map;
import java.util.Optional;
import com.example.service.UserService;
import com.example.service.OrderService;"""
    ),
    Rule(
        id="IMPORT_003",
        category=CATEGORY,
        tags=["imports", "formatting", "structure"],
        name="Import Order",
        description="Imports must be grouped: 1) java.*/javax.* 2) Third-party libraries 3) Project packages. Blank line between groups.",
        wrong_example="""import com.yourcompany.domain.model.User;
import java.util.List;
import org.springframework.http.ResponseEntity;""",
        correct_example="""import java.time.LocalDate;
import java.util.List;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;

import com.yourcompany.domain.model.User;
import com.yourcompany.service.UserService;"""
    ),
]
