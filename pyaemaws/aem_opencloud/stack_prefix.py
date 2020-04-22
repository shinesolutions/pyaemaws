'''A module for retrieving stack prefix information.
'''
import re
# from ..aem_opencloud.stack_types import StackTypes
from ..aws.cloud_formation import CloudFormation
# from datetime import datetime
#
# import json
# import argparse

class StackPrefix:
    '''A class for StackPrefix.
    '''
    def __init__(self, region_name=None):
        '''Instantiate a new StackPrefix object'''
        self.cloud_formation = CloudFormation(region_name)

    def get_full_set_stack_names(self):
        '''Retrieve stack names for Full-Set stack types'''
        stack_names = self.cloud_formation.get_active_stack_names()
        for stack_name in stack_names:
            main_stack_names = re.search("^(.+?)-aem-(.+?)-main-stack$", stack_name)

    def __str__(self):
        return self.__class__.__name__
