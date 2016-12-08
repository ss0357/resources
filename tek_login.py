import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pdb


class TestLogin(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()

    def test_add(self):
        driver = self.driver
        driver.get("http://cn.tek.com")
        self.assertIn("泰克科技", driver.title)

        driver.find_element_by_link_text("登录").click()
        WebDriverWait(driver, 10, 1).until(
            EC.presence_of_element_located((By.ID, "loginheader"))
        )
        #pdb.set_trace()

        username_box = driver.find_element_by_xpath("//input[@id='edit-name']")
        passwd_box = driver.find_element_by_xpath("//input[@id='edit-pass']")
        remeber_me = driver.find_element_by_xpath("//label[@for='edit-persistent-login']")
        submit_button = driver.find_element_by_xpath("//input[@id='edit-submit']")

        print('input username')
        username_box.send_keys('ss0357@126.com')
        print('input password')
        passwd_box.send_keys('66223290')
        print('un check remeber me')
        remeber_me.click()
        print('start login')
        submit_button.submit()

        WebDriverWait(driver, 10, 1).until(
            EC.title_contains("泰克科技")
        )

        ele_quit = driver.find_element_by_link_text("退出")
        #assertIsInstance(ele_quit, selenium.webdriver.firefox.webelement.FirefoxWebElement)
        self.assertIsNotNone(ele_quit)

    def tearDown(self):
        # Driver.Quit():   Quit this dirver, closing every associated windows;
        # Driver.Close():   Close the current window, quiting the browser if it is the last window currently open.
        self.driver.quit()
        print('test end')

if __name__ == '__main__':
    unittest.main()
