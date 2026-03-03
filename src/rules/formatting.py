from typing import List

from src.rules.base import Rule

CATEGORY = "Formatting"

RULES: List[Rule] = [
    Rule(
        id="FORMAT_001",
        category=CATEGORY,
        tags=["formatting", "line-length"],
        name="Line Length",
        description="Maximum line length: 150 characters. Break lines after opening parenthesis, before '.' in method chains, after ',' in parameters, before binary operators.",
        wrong_example="""public ResponseEntity<UserDTO> updateUserProfile(Long userId, String firstName, String lastName, String email, String phone, LocalDate birthDate) {""",
        correct_example="""public ResponseEntity<UserDTO> updateUserProfile(
        Long userId, String firstName, String lastName,
        String email, String phone, LocalDate birthDate) {"""
    ),
    Rule(
        id="FORMAT_002",
        category=CATEGORY,
        tags=["formatting", "line-length", "method-chain"],
        name="Method Chain Breaking",
        description="Method chains exceeding 150 characters must be broken before each '.'",
        wrong_example="""List<UserDTO> result = userRepository.findByActiveAndDepartment(true, department).stream().filter(u -> u.getAge() > 18).map(UserMapper::toDTO).collect(Collectors.toList());""",
        correct_example="""List<UserDTO> result = userRepository
        .findByActiveAndDepartment(true, department)
        .stream()
        .filter(u -> u.getAge() > 18)
        .map(UserMapper::toDTO)
        .collect(Collectors.toList());"""
    ),
]
