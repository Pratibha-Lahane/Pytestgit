import time

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


class Test_005:
    #@pytest.mark.xfail
    def test_credance(self):
        driver = webdriver.Chrome()
        #driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://credence.in/")
        offers = driver.find_element(By.XPATH,"//span[@class='text-white b label']").text
        print(offers)
        print(driver.title)

        if driver.title == "Credence":
            driver.close()
            assert True

        else:
            driver.close()
            assert False


    def test_credance_01(self):
        #driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()
        time.sleep(2)
        l = len(driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a"))
        print(l)
        list = []

        for r in range(1,l+1):
            contact = driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a["+str(r)+"]").text
            list.append(contact)
        if "+91 9579064658" in list :
            assert True
        else:
            assert False

        # if driver.title == "Credence":
        #     driver.close()
        #     assert True
        #
        # else:
        #     driver.close()
        #     assert False