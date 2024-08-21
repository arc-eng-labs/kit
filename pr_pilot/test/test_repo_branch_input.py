# coding: utf-8

"""
    PR Pilot API

    API for creating PR Pilot tasks

    The version of the OpenAPI document: 1.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pr_pilot.models.repo_branch_input import RepoBranchInput

class TestRepoBranchInput(unittest.TestCase):
    """RepoBranchInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RepoBranchInput:
        """Test RepoBranchInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RepoBranchInput`
        """
        model = RepoBranchInput()
        if include_optional:
            return RepoBranchInput(
                github_repo = '',
                branch = ''
            )
        else:
            return RepoBranchInput(
                github_repo = '',
                branch = '',
        )
        """

    def testRepoBranchInput(self):
        """Test RepoBranchInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
