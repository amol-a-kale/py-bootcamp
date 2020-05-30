from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


def verify_mobiles_details():
    driver = webdriver.Chrome("C:\\Users\\Sanket\\Desktop\\py_se_boot\\webdriver\\chromedriver.exe")
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    time.sleep(4)
    driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click()
    actions = ActionChains(driver)
    electronics = driver.find_element_by_xpath("//span[text()='Electronics']")
    actions.move_to_element(electronics).click().perform()
    time.sleep(3)
    samsung_click = driver.find_element_by_xpath("(//a[text()='Samsung'])[1]")
    actions.move_to_element(samsung_click).perform()
    actions.click().perform()
    time.sleep(3)
    # web elements list of all product
    product = driver.find_elements_by_xpath("(//div/p/a)")
    time.sleep(3)

    print(len(product))

    for i in product[0:3]:
        actions.move_to_element(i).perform()
        actions.click().perform()
        time.sleep(3)
        mobile_name = driver.find_element_by_class_name("_35KyD6")
        print(mobile_name.text)
        mobile_rating = driver.find_element_by_xpath("//span[@class='_38sUEc']/span/span[1]")
        print(mobile_rating.text)
        mobile_prize = driver.find_element_by_xpath("//div[@class='_1vC4OE _3qQ9m1']")
        print(mobile_prize.text)
        time.sleep(5)
        driver.back()


verify_mobiles_details()
