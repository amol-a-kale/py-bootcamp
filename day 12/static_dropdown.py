import time

from selenium import webdriver
from selenium.webdriver.support.select import Select


def verify_static_dropdown():

    # ARRANGE

    driver = webdriver.Chrome("C:\\Users\\Sanket\\Desktop\\py_se_boot\\webdriver\\chromedriver.exe")
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    time.sleep(4)

    day_loc = driver.find_element_by_id("day")

    select_day = Select(day_loc)
    select_day.select_by_value("4")  # 4

    time.sleep(3)

    month_loc = driver.find_element_by_xpath("//select[@title='Month']")
    select_day = Select(month_loc)
    select_day.select_by_visible_text("Mar")  # Mar

    time.sleep(3)

    year_loc = driver.find_element_by_name("birthday_year")
    select_day = Select(year_loc)
    select_day.select_by_index(3) # 2018

    time.sleep(3)

# This is for deselect functions

    select_day = Select(day_loc)
    select_day.deselect_by_value("4")  # 4

    time.sleep(3)

    month_loc = driver.find_element_by_xpath("//select[@title='Month']")
    select_day = Select(month_loc)
    select_day.deselect_by_visible_text("Mar")  # Mar

    time.sleep(3)

    year_loc = driver.find_element_by_name("birthday_year")
    select_day = Select(year_loc)
    select_day.deselect_by_index(3)  # 2018



    driver.close()
    driver.quit()

verify_static_dropdown()
