from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\py_se_boot\\webdriver\\chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
search_box = driver.find_element_by_name("q")
# search_box.send_keys("python")
# search_box.send_keys(Keys.ENTER)

time.sleep(3)
actions = ActionChains(driver)
# actions.move_to_element(search_box).key_down(Keys.SHIFT).send_keys('python').key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()
actions.key_down(Keys.SHIFT).send_keys("Python").key_up(Keys.SHIFT).perform()
search_box.clear()
# action.key_down(Keys.SHIFT, search_box).send_keys("selenium").key_up(Keys.SHIFT, search_box).perform()

actions.key_down(Keys.SHIFT, search_box).send_keys("selenium").key_up(Keys.SHIFT, search_box).perform()
search_box.clear()
time.sleep(2)
actions.key_down("\ue008", search_box).send_keys("selenium").key_up("\ue008", search_box).perform()

time.sleep(3)
driver.close()
driver.quit()
