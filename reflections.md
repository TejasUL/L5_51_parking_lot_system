# Lab 5 — Static Code Analysis

## Reflection

### 1. What is static code analysis?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, and coding-style violations before the software is deployed.

### 2. What did Pylint, Bandit, and Flake8 help identify?

Pylint identified code-quality issues such as naming conventions, unused variables, and missing documentation. Bandit identified security risks such as unsafe evaluation, weak hashing, insecure random-number generation, and shell execution. Flake8 identified formatting issues, unused imports, and overly long lines.

### 3. What changes were made to improve the program?

The program was updated to remove unsafe `eval()` usage, use SHA-256 for vehicle hashing, generate ticket PINs with the `secrets` module, avoid shell execution, handle invalid parking slots explicitly, and improve naming, documentation, and file handling.

### 4. How does static code analysis improve software quality?

Static analysis helps developers find problems early, improve code readability and maintainability, and reduce potential security risks. Using multiple tools provides different perspectives on code quality and makes the program easier to review and maintain.