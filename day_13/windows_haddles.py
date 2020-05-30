from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\py_se_boot\\webdriver\\chromedriver.exe")
driver.get("https://www.amazon.in")
driver.maximize_window()
search_box = driver.find_element_by_id("twotabsearchtextbox")  # Find the location of search box
search_box.send_keys("Macbook pro")  # to enter text we have to use send_keys()

# Finding xpath using contains(attribute, textwithinattributevalue)
search_icon = driver.find_element_by_xpath("//input[@type='submit']")
search_icon.click()

time.sleep(5)
parent_window = driver.current_window_handle
print(parent_window)
select_product = driver.find_element_by_xpath("(//a[@class='a-link-normal a-text-normal'])[1]").click()
time.sleep(3)
set_windows = driver.window_handles
print(set_windows)
for window in set_windows:
    if parent_window!=window:
        driver.switch_to.window(window)
productTitle = driver.find_element_by_id("productTitle") #this is wrire outside of loops
print(productTitle.text)
time.sleep(3)
driver.switch_to.window(parent_window)
driver.close()
driver.quit()
