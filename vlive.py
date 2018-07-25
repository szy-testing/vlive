# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://e.vhall.com/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys("13601222648")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("1qaz@WSX")
        driver.find_element_by_id("account-to-login").click()
        driver.find_element_by_link_text(u"开播").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.find_element_by_xpath("//p").click()
        driver.find_element_by_id("to-location").click()
        driver.find_element_by_link_text(u"开始直播").click()
        driver.close()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
