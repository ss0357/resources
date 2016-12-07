#coding=utf-8
from appium import webdriver
import ipdb
import unittest

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '750BCKQ2239H'
desired_caps['appPackage'] = 'com.meizu.flyme.calculator'
desired_caps['appActivity'] = '.Calculator'


#driver.find_element_by_accessibility_id("digit9").click()
#ipdb.set_trace()

# press 5
# driver.find_element_by_id("digit5").click()

# edit_text;   result_text
resource_id = {
    'clear': 'clear_simple',
    'delete': 'del_simple',
    '+': 'plus',
    '-': 'minus',
    '/': 'div',
    '*': 'mul',
    '.': 'dot',
    '(': 'brackets',
    ')': 'brackets',
    '=': 'eq'
}

for i in range(10):
    resource_id[str(i)] = 'digit'+str(i)

class Calculator(object):

    def __init__(self, driver):
        self.driver = driver

    def input_expr(self, expr):
        for key in expr:
            self.driver.find_element_by_id(resource_id[key]).click()

    def clear(self):
        self.driver.find_element_by_id(resource_id['clear']).click()

    def delete(self):
        self.driver.find_element_by_id(resource_id['delete']).click()

    def get_expr(self):
        return self.driver.find_element_by_id('result_text').get_attribute('text')

    def get_result(self):
        return self.driver.find_element_by_id('edit_text').get_attribute('text')



if __name__ == '__main__':
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    app = Calculator(driver)

    app.input_expr('123+456=')
    print(app.get_expr())
    print(app.get_result())
    ipdb.set_trace()

    driver.quit()
