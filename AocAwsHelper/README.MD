#### AOC (AEM Opencloud ) AWS Helper
AOC AWS Helper helps to query aws resources in-order to work easily with AEM Opencloud Manager. 

Check setup.py for package configuration and dependencies. 


**How to Build**

`python3 setup.py sdist bdist_wheel`

**How to Install**

`pip3 install dist/AocAwsHelper-<version_from_setup.py>-py3-none-any.whl`

`eg: pip3 install dist/AocAwsHelper-0.0.2-py3-none-any.whl`


**Usage**
```from StackPrefixHelper import StackPrefixHelper

s = StackPrefixHelper.StackPrefixHelper(stack_type="consolidated")
print(s.fetch_stack_details())
aoc-con62-npe-pdev-01 aoc-con62-npe-dev1-19 aoc-con62-npe-dev5-04 aoc-con62-npe-dev3-03 aoc-con62-npe-dev2-18

s = StackPrefixHelper.StackPrefixHelper(stack_type="stack-manager")
print(s.fetch_stack_details())
 aoc-sm-npe-18
```

More details and usage to be added.
