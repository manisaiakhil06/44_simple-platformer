import unittest

import employee_payroll_system as payroll


class PayrollTests(unittest.TestCase):
    def setUp(self):
        self.original_records = {
            key: value.copy() for key, value in payroll.PAYROLL_RECORDS.items()
        }

    def tearDown(self):
        payroll.PAYROLL_RECORDS.clear()
        payroll.PAYROLL_RECORDS.update(
            {key: value.copy() for key, value in self.original_records.items()}
        )

    def test_bonus_and_transaction_log(self):
        logs = []
        self.assertTrue(payroll.process_salary("EMP101", 100, logs))
        self.assertEqual(payroll.PAYROLL_RECORDS["EMP101"]["base_salary"], 4600.0)
        self.assertEqual(len(logs), 1)

    def test_unknown_employee_bonus_is_rejected(self):
        self.assertFalse(payroll.process_salary("UNKNOWN", 100))

    def test_negative_penalty_is_rejected(self):
        self.assertFalse(payroll.deduct_penalty("EMP101", -1))

    def test_net_salary_uses_tax_rate(self):
        self.assertEqual(payroll.compute_net_salary("EMP101"), 3825.0)

    def test_unknown_employee_salary_raises_value_error(self):
        with self.assertRaises(ValueError):
            payroll.compute_net_salary("UNKNOWN")


if __name__ == "__main__":
    unittest.main()
