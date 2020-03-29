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

    from pyaemaws.StackPrefixHelper.StackPrefixHelper import StackPrefixHelper

    self.sph_fs_text = StackPrefixHelper(stack_type="full-set", return_as="text")
    self.stack_type = ['full-set', 'stack-manager', 'consolidated']
    self.return_values = ["text", "list", "json"]
