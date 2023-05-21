import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_001:
    #@pytest.mark.skip
    def test_sum_006(self):
        a = 3
        b = 9
        sum = a + b
        print(sum)

        if sum == 8:
            print("test_sum_006 is passed")
            assert True

        else:
            print("test_sum_006 is failed")
            assert False