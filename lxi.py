from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("http://134.64.221.28/")

driver.find_element_by_xpath("//*[@id='controlpanel']").click()
driver.switch_to.frame("targetframe")

driver.find_element_by_xpath(".//*[@id='TriggerType']").send_keys(Keys.ARROW_DOWN)

driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id('su').click()
#driver.quit()
