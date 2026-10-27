# Lab 5 Reflection

**Student:** NALLAMALLI KANAKA MANI SAI AKHIL  
**USN:** PES1UG24CS290

> Note: The supplied three-page handout describes the reflection deliverable but does not print the four reflection questions. These responses address four standard reflection themes; adjust the headings if your instructor has a separate question sheet.

## 1. What is static code analysis, and why is it useful?

Static code analysis checks source code without running the program. It helps identify likely bugs, unsafe coding patterns, and style problems early. Finding these issues before deployment makes software easier to maintain and reduces avoidable security risks.

## 2. How do Pylint, Flake8, and Bandit differ?

Pylint checks code quality, naming, unused code, and design problems. Flake8 focuses on Python syntax/style conventions and formatting issues. Bandit scans Python source for common security risks, such as unsafe dynamic evaluation and weak security-related functions. They overlap in places but provide complementary views.

## 3. Which issues were most important, and how were they fixed?

The highest-priority issue was `eval()` on an expression supplied to the salary calculation function because it could execute arbitrary code. I replaced it with a direct calculation using the employee's configured tax rate. I also removed shell execution and a hard-coded secret, fixed the shared mutable default, replaced broad exception handling with validation, and used a cryptographically secure token generator.

## 4. What did you learn, and what are the limitations of static analysis?

Static analysis can quickly point to suspicious code, but findings still need human review. A clean report does not prove that a program is correct or secure; runtime tests and review of business rules are still needed. I would use all three tools regularly and keep the before/after reports as evidence of the changes.

## Validation note

The source file was reviewed and can be syntax-checked with Python. The current working environment did not have Pylint, Bandit, or Flake8 installed and could not access package repositories, so no genuine tool-generated scores or clean after-reports are claimed here. Run `run_analysis.sh` in an environment where the three tools can be installed to generate them.
