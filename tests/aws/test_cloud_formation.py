import sys
import unittest

from pyaemaws.aws.cloud_formation import CloudFormation
from unittest.mock import MagicMock, patch

mock_response = {
    'StackSummaries': [
        { 'StackName': 'Stack-Name-1' },
        { 'StackName': 'Stack-Name-2' },
        { 'StackName': 'Stack-Name-3' }
    ]
}
mock_boto3_client = MagicMock()
mock_boto3_client.list_stacks = MagicMock(return_value=mock_response)

class TestCloudFormation(unittest.TestCase):

    @patch('boto3.client', MagicMock(return_value=mock_boto3_client))
    def test_get_active_stack_names(self):
        self.cloud_formation = CloudFormation(region_name='ap-southeast-2')
        stack_names = self.cloud_formation.get_active_stack_names()
        self.assertTrue(isinstance(stack_names, list))
        self.assertEqual(stack_names[0], 'Stack-Name-1')
        self.assertEqual(stack_names[1], 'Stack-Name-2')
        self.assertEqual(stack_names[2], 'Stack-Name-3')

if __name__ == '__main__':
    unittest.main()
