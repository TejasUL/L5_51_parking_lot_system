# Lab 5 — Static Code Analysis

## Issue Documentation Table

| Issue | Type | Line(s) Before Fix | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Bug | 15 | `entry_logs=[]` could share a list between function calls. | Changed the default to `None` and initialized a new list inside the function. |
| Unsafe `eval()` | Security | 48 | `eval()` could execute an arbitrary Python expression. | Replaced expression evaluation with a numeric surge multiplier. |
| Weak MD5 hash | Security | 53 | MD5 is not suitable for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Insecure random PIN | Security | 57 | `random.randint()` is not designed for security-sensitive PIN generation. | Used Python's `secrets` module. |
| Shell command execution | Security | 64 | `os.system()` invoked a shell to display a message. | Removed shell execution and used `print()`. |
| Broad exception handling | Bug | 32–33 | A bare `except` silently ignored errors. | Checked for invalid slot IDs explicitly. |
| Unused imports and variables | Code quality | 4, 37, 47 | Some imports and variables were unused. | Removed unused imports and variables. |
| Function naming and documentation | Style | Multiple | Several functions used camelCase and lacked docstrings. | Renamed functions to snake_case and added docstrings. |
| File handling and encoding | Code quality | 61–63 | The file was opened without an explicit encoding and closed manually. | Used a `with open(...)` block with UTF-8 encoding. |
| Long lines and formatting | Style | Multiple | Several lines exceeded Flake8's line-length limit. | Reformatted long lines and added a final newline. |

## Result

- Pylint score after fixes: 9.71/10
- Bandit: No issues identified
- Flake8: No issues reported