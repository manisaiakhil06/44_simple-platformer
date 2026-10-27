# Static Code Analysis Issue Log

**Student:** NALLAMALLI KANAKA MANI SAI AKHIL  
**USN:** PES1UG24CS290  
**Assigned repository:** https://github.com/SETAPESU26/L5_44_employee_payroll_system

The line references below refer to the original repository version; line numbers can change after edits.

| Issue | Type / severity | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Dynamic `eval()` | Security / High | 388–394 | Evaluating a caller-provided expression can execute arbitrary Python code. | Removed the expression parameter; calculate net pay from the stored tax rate. |
| Shell command built from filename | Security / Medium | 404–412 | Passing a filename into `os.system()` can enable shell injection. | Removed shell execution; use `pathlib.Path` for file output and print a normal status message. |
| Hard-coded payroll secret | Security / Medium | 414–431 | A master secret is embedded in source code and printed. | Removed the hard-coded secret and its output. |
| Mutable default argument | Correctness / Medium | 352–361 | `transaction_logs=[]` is shared between calls. | Use `None` as the default and create a fresh list inside the function. |
| Bare `except` silently ignores failures | Reliability / Medium | 363–371 | Any exception is swallowed, hiding programming errors and failed deductions. | Validate employee and penalty explicitly and return a success/failure result. |
| Weak MD5 hash | Security / Low–Medium | 396–398 | MD5 is unsuitable for security-sensitive hashing. | Use SHA-256 for a stable identifier; do not treat this hash as password storage. |
| Predictable random token | Security / Medium | 400–402 | `random.randint` is not intended for security tokens. | Use `secrets.randbelow` for token generation. |
| File opened without a context manager | Quality / Low | 404–409 | An exception can prevent the file from being closed. | Use `with` to manage the file lifecycle and UTF-8 encoding. |
| Style and naming violations | Style / Low | Throughout | Inconsistent blank lines, spacing, camelCase, and formatting. | Apply PEP 8 naming and consistent formatting. |
| Unused import / variable | Quality / Low | Original imports and eligibility function | `math` and `statutory_buffer` are unused. | Remove unused code. |
