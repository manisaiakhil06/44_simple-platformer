# Lab 5 — Static Code Analysis: Employee Payroll System

**Student:** NALLAMALLI KANAKA MANI SAI AKHIL  
**USN:** PES1UG24CS290  
**Assigned repository:** https://github.com/SETAPESU26/L5_44_employee_payroll_system

## Files
- `employee_payroll_system.py` — revised payroll program.
- `issues.md` — issue log mapped to the original source.
- `reflection.md` — four reflection responses.
- `run_analysis.sh` — setup and commands for Pylint, Bandit, and Flake8.
- `reports/` — report folders; run the script to generate genuine tool outputs.

## Run
```bash
python3 employee_payroll_system.py
```

## Run static analysis
```bash
bash run_analysis.sh
```

The script creates a virtual environment, installs Pylint, Bandit, and Flake8, and writes reports. To produce true baseline reports, place the original repository source in this directory as `employee_payroll_system_original.py` before running the script. Review reports and fix any remaining findings; tool versions can affect results.

## Git deliverable
The handout asks for three commits, one for each tool's fixes. Suggested commit sequence:
1. `git add employee_payroll_system.py && git commit -m "Fix payroll security issues identified by Bandit"`
2. `git add employee_payroll_system.py && git commit -m "Improve payroll code quality identified by Pylint"`
3. `git add employee_payroll_system.py && git commit -m "Apply PEP 8 formatting fixes from Flake8"`

These are suggested messages, not commits made to the remote repository. The repository could not be cloned from this execution environment, so changes have not been pushed to GitHub.
