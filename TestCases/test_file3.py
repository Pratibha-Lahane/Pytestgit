import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
class Test_py:

    #@pytest.mark.xfail
    def test_sum_001(self):
        a = 3
        b = 5
        sum = a+b
        print(sum)

        if sum == 8:
            print("test_sum_001 is passed")
            assert True

        else:
            print("test_sum_001 is failed")
            assert False

    #@pytest.mark.skip
    def test_mul_002(self):
        a = 3
        b = 5
        mul = a*b
        print(mul)

        if mul == 16:
            print("test_mul_002 is passed")
            assert True

        else:
            print("test_mul_002 is failed")
            assert False

    def sum_003(self):      #this item not consider in testcases because of name
        a = 3
        b = 5
        sum = a+b

        if sum == 8:
            print("test_sum_001 is passed")

        else:
            print("test_sum_001 is failed")

    #@pytest.mark.group1
    def test_Google(self):
        driver = webdriver.Chrome()
        #driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.CLASS_NAME,"lnXdpd").is_displayed()
        print(logo)

        if logo == True:
            #driver.close()
            assert True

        else:
            driver.close()
            assert False










