"""
@author : Tej Prakash Sharma
Test case to handle Dynamic Table
"""
from dynamic_table.pages.pagination import *
import json
import pytest
from dynamic_table.tests.base_test import BaseTest
from dynamic_table.pages.data import *


class Test_003(BaseTest):
    def test_sample3_1(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-data-download-demo.html")
        pg = Pagination(self.driver)
        head = pg.get_head()
        header = []
        for hea in head:
            header.append(hea.text)

        name = pg.get_name()
        position = pg.get_position()
        office = pg.get_office()
        age = pg.get_age()
        startdate = pg.get_startdate()
        salary = pg.get_salary()

        _data = {}
        for i in range(len(name)):
            _data[name[i].text] = [position[i].text, office[i].text, age[i].text, startdate[i].text, salary[i].text]

        with open("..//dynamic_table//report//data2.json", "w") as f:
            json.dump(_data, f, indent=4)