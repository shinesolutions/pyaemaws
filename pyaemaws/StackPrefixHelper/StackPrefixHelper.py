"""
Notes
"""

import re
import boto3
import json
import argparse
from datetime import datetime


class StackPrefixHelper:
    def __init__(self, stack_type="full-set", return_as="text"):

        #stack filter abbrevation is to filter the stack name, load from config
        self.stack_type_filter_abbrev = {
            "full-set": "fs",
            "consolidated": "con",
            "stack-manager": "sm",
        }
        self.stack_type = stack_type
        self.return_as = return_as
        #load region value from config
        self.cfn_client = boto3.client('cloudformation', region_name='ap-southeast-2')
        self.stack_details = {}
        self.stack_list = {}
        self.stack_type_values = ["full-set", "consolidated", "stack-manager"]
        self.return_as_values = ["text", "list", "json"]
        # self.validate_inputs(self.stack_type, "stack_type")
        # self.validate_inputs(self.return_as, "return_as")
        # return self.fetch_stack_details(self.stack_type_filter_abbrev[self.stack_type])

    def datetime_convertor(self, o):
        if isinstance(o, datetime):
            return o.__str__()

    def validate_inputs(self, input_value, input_type):
        if input_type == "stack_type" and input_value not in self.stack_type_values:
            return False

        if input_type == "return_as" and input_value not in self.return_as_values:
            return False

        return True

    def fetch_stack_details(self):
        stack_type_filter = self.stack_type
        # stack_type_filter = self.stack_type_filter_abbrev[self.stack_type]
        #load StackStatusFilter from config or as parameter
        response = self.cfn_client.list_stacks(
            StackStatusFilter=[
                'CREATE_COMPLETE', 'UPDATE_COMPLETE'
            ]
        )
        for stack_summary in response['StackSummaries']:
            x = re.search("^(.+?)-aem-(.+?)-main-stack$", stack_summary['StackName'])
            stack_prefix = ""
            stack_type = ""
            if x:
                stack_prefix = x.group(1)
                stack_type = x.group(2)

            if str(stack_summary['StackName']).endswith("main-stack") and stack_prefix:

                self.stack_details[stack_summary['CreationTime']] = [stack_prefix, stack_type, stack_summary['StackStatus']]
                if stack_type_filter in self.stack_type_filter_abbrev.keys():
                    matched_stack_name = re.search("^(.+?)" + self.stack_type_filter_abbrev[stack_type_filter] + "(.+?)$", str(stack_summary['StackName']))
                    if matched_stack_name:
                        # print matched_stack_name.group(0), stack_type_filter, str(stack_summary['StackName'])
                        self.stack_list[stack_prefix] = [matched_stack_name.group(0), stack_type, stack_summary['StackStatus'], stack_summary['CreationTime']]

        stack_list_keys = self.stack_list.keys()
        if self.return_as == "json":
            sorted_stack_details = sorted(self.stack_details.items())
            # print sorted_stack_details
            return json.dumps(sorted_stack_details, indent=2, default=self.datetime_convertor)
        if self.return_as == "list":
            return stack_list_keys
        if self.return_as == "text":
            return " ".join(stack_list_keys)

        return " ".join(stack_list_keys)

if __name__ == '__main__':
    s = StackPrefixHelper(stack_type="full-set", return_as="json")
    print(s.fetch_stack_details())