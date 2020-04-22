'''An enum to represent stack types.
'''
import enum

class StackTypes(enum.Enum):
    '''A class for StackTypes enum defining:
    - type name
    - type abbreviation
    '''

    FULL_SET = 'full-set', 'fs'
    CONSOLIDATED = 'consolidated', 'con'
    STACK_MANAGER = 'stack-manager', 'sm'

    def get_name(self):
        '''Retrieve the name of this stack type'''
        return self.value[0]

    def get_abbreviation(self):
        '''Retrieve the abbreviation of this stack type'''
        return self.value[1]
