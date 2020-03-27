import unittest
from pyaemaws.StackPrefixHelper.StackPrefixHelper import StackPrefixHelper


class TestStackPrefixHelper(unittest.TestCase):

    def setUp(self):
        self.sph_fs_text = StackPrefixHelper(stack_type="full-set", return_as="text")
        # self.sph_fs_json = StackPrefixHelper(stack_type="full-set", return_as="json")
        # self.sph_fs_list = StackPrefixHelper(stack_type="full-set", return_as="list")
        # self.sph_con_text = StackPrefixHelper(stack_type="consolidated", return_as="text")
        # self.sph_con_json = StackPrefixHelper(stack_type="consolidated", return_as="json")
        # self.sph_con_list = StackPrefixHelper(stack_type="consolidated", return_as="list")
        # self.sph_sm_text = StackPrefixHelper(stack_type="stack-manager", return_as="text")
        # self.sph_sm_json = StackPrefixHelper(stack_type="stack-manager", return_as="json")
        # self.sph_sm_list = StackPrefixHelper(stack_type="stack-manager", return_as="list")
        self.stack_type = ['full-set', 'stack-manager', 'consolidated']
        self.return_values = ["text", "list", "json"]

    def test_sph_fs_inputs(self):
        self.assertEqual(
            sorted(self.sph_fs_text.stack_type_values),
            sorted(self.stack_type),
            "Assertion Failed in Stack Type Values"
        )

        self.assertEqual(
            sorted(self.sph_fs_text.return_as_values),
            sorted(self.return_values),
            "Assertion Failed in Return as Values"
        )

        self.assertEqual(
            sorted(self.sph_fs_text.stack_type_filter_abbrev.keys()),
            sorted(self.stack_type)
        )

    def test_sph_validate_inputs(self):
        self.assertTrue(self.sph_fs_text.validate_inputs("full-set", "stack_type"))
        self.assertTrue(self.sph_fs_text.validate_inputs("json", "return_as"))
        self.assertFalse(self.sph_fs_text.validate_inputs("json-test", "return_as"))
        self.assertFalse(self.sph_fs_text.validate_inputs("full-set-test", "stack_type"))

    def test_sph_date_convertor(self):
        from datetime import datetime
        dt_ins = datetime.now()
        self.assertEqual(str(dt_ins), self.sph_fs_text.datetime_convertor(dt_ins))


if __name__ == '__main__':
    unittest.main()
