"""
@author : Tej Prakash Sharma
Base class for all the Test cases
"""
import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
