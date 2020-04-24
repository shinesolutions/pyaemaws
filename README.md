[![Build Status](https://github.com/shinesolutions/pyaemaws/workflows/CI/badge.svg)](https://github.com/shinesolutions/pyaemaws/actions?query=workflow%3ACI)
[![Known Vulnerabilities](https://snyk.io/test/github/shinesolutions/pyaemaws/badge.svg)](https://snyk.io/test/github/shinesolutions/pyaemaws)

pyaemaws
--------

pyaemaws is a Python client for Shine Solutions [Adobe Experience Manager (AEM)](http://www.adobe.com/au/marketing-cloud/enterprise-content-management.html) Platform on AWS.

This library provides an API which enables the interaction with the platform via Python language, allowing a deep integration with a number of Python-based tools such as [Ansible](https://ansible.com/).

pyaemaws is part of [AEM OpenCloud](https://aemopencloud.io) platform.

Installation
------------

From [PyPI](https://pypi.org/):

    pip3 install pyaemaws

From [Python Wheel](https://pythonwheels.com/):

    make deps package install

Usage
-----

To retrieve all stack prefixes of AEM Full-Set stacks:

    from pyaemaws.stack_prefix import StackPrefix

    stack_prefix = StackPrefix(region_name='ap-southeast-2')
    full_set_stack_prefixes = stack_prefix.get_full_set_stack_prefixes()

    for full_set_stack_prefix in full_set_stack_prefixes:
        print(full_set_stack_prefix)
