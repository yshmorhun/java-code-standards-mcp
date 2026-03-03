from typing import List

from src.rules.base import Rule

CATEGORY = "DTO"

RULES: List[Rule] = [
    Rule(
        id="DTO_001",
        category=CATEGORY,
        tags=["lombok", "structure", "immutability"],
        name="No Record DTOs",
        description="Java record is forbidden for DTOs. DTOs must be regular classes with Lombok.",
        wrong_example="""public record AccountDetails(
    String id,
    String name
) {}""",
        correct_example="""@Value
@Builder
@AllArgsConstructor(access = AccessLevel.PRIVATE)
public class AccountDetailsDto {
    @NonNull
    private String id;
    private String name;
}"""
    ),
    Rule(
        id="DTO_002",
        category=CATEGORY,
        tags=["naming", "structure", "package"],
        name="DTO Package and Naming",
        description="DTOs must be in 'model' package. Class names must end with 'Dto'.",
        wrong_example="""// com.company.feature.UserData
public class UserData {}""",
        correct_example="""// com.company.feature.model.UserDto
public class UserDto {}"""
    ),
    Rule(
        id="DTO_003",
        category=CATEGORY,
        tags=["lombok", "jackson", "immutability", "structure"],
        name="DTO Structure",
        description="DTOs must: use @Value, @Builder, private @AllArgsConstructor. For JSON: @JsonIgnoreProperties(ignoreUnknown=true), @JsonDeserialize with builder, explicit @JsonProperty.",
        wrong_example="""public class UserDto {
    public String id;
    public String name;

    public UserDto(String id, String name) {
        this.id = id;
        this.name = name;
    }
}""",
        correct_example="""@Value
@Builder
@AllArgsConstructor(access = AccessLevel.PRIVATE)
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonDeserialize(builder = UserDto.UserDtoBuilder.class)
public class UserDto {
    @NonNull
    @JsonProperty("id")
    private String id;

    @JsonProperty("name")
    private String name;
}"""
    ),
]
