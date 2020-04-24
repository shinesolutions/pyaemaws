'''A module for retrieving stack prefix information.
'''
import re
from ..aem_opencloud.stack_types import StackTypes
from ..aws.cloud_formation import CloudFormation

class StackPrefix:
    '''A class for StackPrefix.
    '''
    def __init__(self, region_name=None):
        '''Instantiate a new StackPrefix object'''
        self.cloud_formation = CloudFormation(region_name)

    def __get_stack_prefixes(self, stack_type):
        '''Retrieve stack prefixes for the specified stack type'''
        stack_prefixes = []

        stack_names = self.cloud_formation.get_active_stack_names()
        for stack_name in stack_names:
            search_pattern = '^(.+?)-aem-{}-main-stack$'.format(
                stack_type.get_name()
            )
            search_result = re.search(search_pattern, stack_name)
            if search_result:
                stack_suffix = '-aem-{}-main-stack'.format(
                    stack_type.get_name()
                )
                stack_prefix = stack_name.replace(stack_suffix, '')
                stack_prefixes.append(stack_prefix)

        return stack_prefixes

    def get_full_set_stack_prefixes(self):
        '''Retrieve stack prefixes for Full-Set stack type'''
        return self.__get_stack_prefixes(StackTypes.FULL_SET)

    def get_consolidated_stack_prefixes(self):
        '''Retrieve stack prefixes for Condolidated stack type'''
        return self.__get_stack_prefixes(StackTypes.CONSOLIDATED)

    def get_stack_manager_stack_prefixes(self):
        '''Retrieve stack prefixes for Full-Set stack type'''
        return self.__get_stack_prefixes(StackTypes.STACK_MANAGER)

    def __str__(self):
        return self.__class__.__name__
