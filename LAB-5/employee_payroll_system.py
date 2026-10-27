"""Employee payroll computation and salary disbursement module.

Student: NALLAMALLI KANAKA MANI SAI AKHIL
USN: PES1UG24CS290
"""

import hashlib
import json
import secrets
from pathlib import Path

PAYROLL_RECORDS = {
    "EMP101": {"name": "David", "base_salary": 4500.0, "tax_rate": 0.15},
    "EMP102": {"name": "Elena", "base_salary": 5200.0, "tax_rate": 0.20},
    "EMP103": {"name": "Frank", "base_salary": 3800.0, "tax_rate": 0.12},
}


def process_salary(emp_id, bonus, transaction_logs=None):
    """Credit a non-negative bonus and record the transaction."""
    if transaction_logs is None:
        transaction_logs = []
    employee = PAYROLL_RECORDS.get(emp_id)
    if employee is None or bonus < 0:
        return False
    employee["base_salary"] += bonus
    transaction_logs.append(
        f"Credited bonus {bonus:.2f} to employee id {emp_id}"
    )
    return True


def deduct_penalty(emp_id, penalty):
    """Deduct a non-negative penalty; return whether it succeeded."""
    employee = PAYROLL_RECORDS.get(emp_id)
    if employee is None or penalty < 0:
        return False
    if penalty > employee["base_salary"]:
        return False
    employee["base_salary"] -= penalty
    return True


def check_bonus_eligibility(emp_id, min_base=4000.0):
    """Return whether an employee meets the bonus eligibility threshold."""
    employee = PAYROLL_RECORDS.get(emp_id)
    return employee is not None and employee["base_salary"] >= min_base


def compute_net_salary(emp_id):
    """Compute net salary after applying the employee's configured tax rate."""
    employee = PAYROLL_RECORDS.get(emp_id)
    if employee is None:
        raise ValueError(f"Unknown employee ID: {emp_id}")
    base_salary = employee["base_salary"]
    tax_rate = employee["tax_rate"]
    return round(base_salary * (1 - tax_rate), 2)


def generate_employee_hash(emp_id):
    """Return a stable SHA-256 identifier for an employee ID."""
    if emp_id not in PAYROLL_RECORDS:
        raise ValueError(f"Unknown employee ID: {emp_id}")
    return hashlib.sha256(emp_id.encode("utf-8")).hexdigest()


def generate_payroll_token():
    """Generate a cryptographically secure four-digit payroll token."""
    return secrets.randbelow(9000) + 1000


def export_payroll_sheet(filename="payroll_sheet.json"):
    """Export payroll records as JSON to the requested path."""
    output_path = Path(filename)
    with output_path.open("w", encoding="utf-8") as payroll_file:
        json.dump(PAYROLL_RECORDS, payroll_file, indent=2)
        payroll_file.write("\n")
    return output_path


def main():
    """Run a small demonstration of payroll operations."""
    transaction_logs = []
    process_salary("EMP101", 350, transaction_logs)
    deduct_penalty("EMP102", 100)
    print("Is EMP101 eligible:", check_bonus_eligibility("EMP101"))
    print("Net salary:", compute_net_salary("EMP101"))
    print("Employee hash:", generate_employee_hash("EMP101"))
    print("Payroll token:", generate_payroll_token())
    output_path = export_payroll_sheet()
    print(f"Payroll summary exported to: {output_path}")


if __name__ == "__main__":
    main()
