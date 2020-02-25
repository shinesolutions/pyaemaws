###AOC (AEM Opencloud ) AWS Helper
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

##Tests

`python -m unittest discover -s <test_folder_name>
eg: python -m unittest discover -s tests
`

**Coverage**

`pip install coverage`

```
set pythonpath to pyaemaws
export PYHTONPATH=<path_to_pyaemaws>
eg: export PYTHONPATH=/opt/repos/shine/pyaemaws
```
```
coverage run --source=./AocAwsHelper -m unittest discover
coverage report
```

**Result:**
```
Example: 
Name                                                  Stmts   Miss  Cover
-------------------------------------------------------------------------
AocAwsHelper/S3Helper/__init__.py                         0      0   100%
AocAwsHelper/StackPrefixHelper/StackPrefixHelper.py      52     26    50%
AocAwsHelper/StackPrefixHelper/__init__.py                1      0   100%
AocAwsHelper/__init__.py                                  0      0   100%
AocAwsHelper/setup.py                                     4      4     0%
-------------------------------------------------------------------------
TOTAL                                                    57     30    47%
```
####To generate a html coverage report, run

```
coverage html
```