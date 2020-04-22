import unittest

from pyaemaws.aem_opencloud.stack_types import StackTypes

class TestStackTypes(unittest.TestCase):

    def test_full_set(self):
        stack_type = StackTypes.FULL_SET
        self.assertEqual(stack_type.name, 'FULL_SET')
        self.assertEqual(stack_type.get_name(), 'full-set')
        self.assertEqual(stack_type.get_abbreviation(), 'fs')

    def test_consolidated(self):
        stack_type = StackTypes.CONSOLIDATED
        self.assertEqual(stack_type.name, 'CONSOLIDATED')
        self.assertEqual(stack_type.get_name(), 'consolidated')
        self.assertEqual(stack_type.get_abbreviation(), 'con')

    def test_stack_manager(self):
        stack_type = StackTypes.STACK_MANAGER
        self.assertEqual(stack_type.name, 'STACK_MANAGER')
        self.assertEqual(stack_type.get_name(), 'stack-manager')
        self.assertEqual(stack_type.get_abbreviation(), 'sm')

if __name__ == '__main__':
    unittest.main()
