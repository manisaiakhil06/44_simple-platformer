#!/usr/bin/env bash
set -euo pipefail
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pylint bandit flake8
mkdir -p reports/before reports/after
# Baseline reports are generated from the original version if you save it as
# employee_payroll_system_original.py in this directory.
if [[ -f employee_payroll_system_original.py ]]; then
  pylint employee_payroll_system_original.py > reports/before/pylint_report.txt || true
  bandit -r employee_payroll_system_original.py > reports/before/bandit_report.txt || true
  flake8 employee_payroll_system_original.py > reports/before/flake8_report.txt || true
else
  echo "Original source not present; see issues.md for reviewed baseline findings." > reports/before/README.txt
fi
pylint employee_payroll_system.py > reports/after/pylint_report.txt || true
bandit -r employee_payroll_system.py > reports/after/bandit_report.txt || true
flake8 employee_payroll_system.py > reports/after/flake8_report.txt || true
echo "Reports written under reports/before and reports/after."
