'''A module for retrieving AWS CloudFormation resources information.
'''
import boto3

class CloudFormation:
    '''A class for CloudFormation client.
    '''

    def __init__(self,
                 region_name=None):
        '''Instantiate a new CloudFormation object'''
        self.client = boto3.client('cloudformation', region_name=region_name)

    def get_active_stack_names(self):
        '''Retrieve a list of stack names which have CREATE_COMPLETE or
        UPDATE_COMPLETE status.
        '''
        response = self.client.list_stacks(
            StackStatusFilter=[
                'CREATE_COMPLETE', 'UPDATE_COMPLETE'
            ]
        )
        stack_names = []
        for stack_summary in response['StackSummaries']:
            stack_names.append(stack_summary['StackName'])
        return stack_names

    def __str__(self):
        return self.__class__.__name__
