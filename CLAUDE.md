# Code Generation Workflow

> **Rules**
> - Follow steps **IN ORDER** — do not skip steps
> - Load rules **per class**, not all at once — avoid context overload
> - Make as many MCP requests as needed — each call must have a clear purpose; never skip a call that improves code quality
> - Each milestone is a **goal** — use your own best practices to achieve it

## Step 1: Planning & Architecture

**Milestones**:
1. Architecture rules loaded from MCP
2. Implementation plan complete:
   - All required classes identified
   - Correct package defined for each class
   - Naming conventions loaded and applied
   - Dependencies between classes defined
3. Plan documented:
   - All classes listed with packages
   - Rules noted for each class type
4. Packages and classes created according to the plan

## Step 2: Class Implementation

**Purpose**: For each class, load specific rules, then create the complete class with all internals.

**Milestones**: For each class — **ONE BY ONE**:
1. Rules loaded for **this specific** class type from MCP and reviewed before writing any code
2. Class internals implemented per loaded rules
3. Imports added per loaded rules
4. Class verified:
   - Correct package, name and suffix
   - Field and method names follow naming conventions per loaded rules
   - Imports organized per loaded rules
   - All internals comply with loaded rules
5. Repeated for **next class** until all classes are created

## Step 3: Test Implementation

**Purpose**: For each implemented class, load test rules and create corresponding test class.

**Milestones**: For each class — **ONE BY ONE**:
1. Rules loaded for **this specific** test class type from MCP and reviewed before writing any code
2. Test class internals implemented per loaded rules
3. Imports added per loaded rules
4. Test class verified:
   - Correct package, name and suffix
   - Field and method names follow naming conventions per loaded rules
   - Imports organized per loaded rules
   - All internals comply with loaded rules
5. Repeated for **next class** until all classes are covered

## Step 4: Compile & Verify

**Purpose**: Ensure code compiles and all tests pass.

**Milestones**:
1. Build tool detected and project compiles without errors
2. Compilation errors resolved — go back to **Step 2** if needed
3. All new tests pass
4. All existing tests pass without regression
5. Test failures resolved — go back to **Step 2** or **Step 3** if needed
6. Code is ready for review
