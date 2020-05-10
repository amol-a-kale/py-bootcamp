from selenium import webdriver
import time


# A - Arrange (Setup/Prerequsite)
# A - Action
# A = Assert  (Validate)


def verify_search_functionality(search_text):
    # ARRANGE

    driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\py_se_boot\\webdriver\\chromedriver.exe")
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    time.sleep(4)

    ## ACTION
    driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click();

    search_box = driver.find_element_by_name("q")  # Find the location of search box
    # search_box.send_keys("Macbook pro")   # to enter text we have to use send_keys()
    search_box.send_keys(search_text)

    # Finding xpath using contains(attribute, textwithinattributevalue)
    search_icon = driver.find_element_by_xpath("//button[@type='submit']")
    search_icon.click()

    time.sleep(5)

    ## ASSERT
    search_product_info_element = driver.find_element_by_xpath("//span[@class='_2yAnYN']")
    search_product_info = search_product_info_element.text

    # if(search_product_info == 'Showing 1 – 17 of 17 results for "macbook pro"'):
    #     print("We have successfully searched the product " + search_text)
    # else:
    #     print("The search product is not listed here")

    if (('results for "' + search_text.lower() + '"') in search_product_info):
        print("We have successfully searched the product " + search_text)
    else:
        print("The search product is not listed here")

    driver.close()
    driver.quit()


verify_search_functionality("Macbook pro")

verify_search_functionality("samsung mobile phone")
