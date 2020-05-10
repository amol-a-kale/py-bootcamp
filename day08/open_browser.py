from selenium import webdriver
import time
from time import sleep


def open_chrome_browser():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\py_se_boot\\webdriver\\chromedriver.exe")
    driver.get("https://www.amazon.in")

    # Here we are using ID locator to find element
    searchBox = driver.find_element_by_id("twotabsearchtextbox")
    searchBox.send_keys("Macbook Pro")  # here we are entering text to serach box

    # To find the location of search icon webelement
    searchIcon = driver.find_element_by_class_name("nav-input")  # here we use class name to find element
    searchIcon.click()

    sleep(3)

    # To find element element using link_text
    # macbook_pro_details = driver.find_element_by_link_text("Apple 15\" MacBook Pro, Retina, Touch Bar, 2.9GHz Intel Core i7 Quad Core, 16GB RAM, 512GB SSD, Silver, MPTV2LL/A (Newest Version)")
    # macbook_pro_details.click()

    # To find all the links on webpage
    link = driver.find_element_by_tag_name("a")  # It always going to return the very first link
    print(link)
    print(link.text)

    list_of_links = driver.find_elements_by_tag_name("a")  # Its going to return the list of links
    # print(list_of_links)
    for link in list_of_links:
        print(link.text)

    # To find element element using partial_link_text
    macbook_pro_details = driver.find_element_by_partial_link_text("Apple MacBook Pro")
    macbook_pro_details.click()

    sleep(5)

    driver.close()


def open_ff_browser():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\py_se_boot\\webdriver\\chromedriver.exe")
    driver.get("https://www.amazon.in")

    driver.close()


open_chrome_browser()
