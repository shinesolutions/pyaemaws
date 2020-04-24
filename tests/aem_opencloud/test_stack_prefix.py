import sys
import unittest

from pyaemaws.aem_opencloud.stack_prefix import StackPrefix
from unittest.mock import MagicMock, patch

mock_response = {
    'StackSummaries': [
        { 'StackName': 'stack-prefix-1-aem-full-set-main-stack' },
        { 'StackName': 'some-other-stack-1' },
        { 'StackName': 'stack-prefix-2-aem-consolidated-main-stack' },
        { 'StackName': 'stack-prefix-3-aem-stack-manager-main-stack' },
        { 'StackName': 'some-other-stack-2' }
    ]
}
mock_boto3_client = MagicMock()
mock_boto3_client.list_stacks = MagicMock(return_value=mock_response)

class TestStackPrefix(unittest.TestCase):

    @patch('boto3.client', MagicMock(return_value=mock_boto3_client))
    def test_get_full_set_stack_prefixes(self):
        stack_prefix = StackPrefix(region_name='ap-southeast-2')
        full_set_stack_prefixes = stack_prefix.get_full_set_stack_prefixes()
        self.assertEqual(1, len(full_set_stack_prefixes))
        self.assertEqual(full_set_stack_prefixes[0], 'stack-prefix-1')

    @patch('boto3.client', MagicMock(return_value=mock_boto3_client))
    def test_get_consolidated_stack_prefixes(self):
        stack_prefix = StackPrefix(region_name='ap-southeast-2')
        consolidated_stack_prefixes = stack_prefix.get_consolidated_stack_prefixes()
        self.assertEqual(1, len(consolidated_stack_prefixes))
        self.assertEqual(consolidated_stack_prefixes[0], 'stack-prefix-2')

    @patch('boto3.client', MagicMock(return_value=mock_boto3_client))
    def test_get_stack_manager_stack_prefixes(self):
        stack_prefix = StackPrefix(region_name='ap-southeast-2')
        stack_manager_stack_prefixes = stack_prefix.get_stack_manager_stack_prefixes()
        self.assertEqual(1, len(stack_manager_stack_prefixes))
        self.assertEqual(stack_manager_stack_prefixes[0], 'stack-prefix-3')

    def test_str(self):
        stack_prefix = StackPrefix(region_name='ap-southeast-2')
        self.assertEqual(str(stack_prefix), 'StackPrefix')

if __name__ == '__main__':
    unittest.main()
