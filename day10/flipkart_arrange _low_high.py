from selenium import webdriver
import time


def verify_low_to_high_prices(search_text):
    # ARRANGE

    driver = webdriver.Chrome("C:\\Users\\Sanket\\Desktop\\py_se_boot\\webdriver\\chromedriver.exe")
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    time.sleep(4)

    ## ACTION
    driver.find_element_by_xpath("//button[@class='_2AkmmA _29YdH8']").click();

    search_box = driver.find_element_by_name("q")  # Find the location of search box
    # search_box.send_keys("Macbook pro")   # to enter text we have to use send_keys()
    time.sleep(3)
    search_box.send_keys(search_text)
    time.sleep(5)

    # Finding xpath using contains(attribute, textwithinattributevalue)
    search_icon = driver.find_element_by_xpath("//button[@type='submit']").click()

    time.sleep(5)
    # click on price high to low option
    price_low_High_icon = driver.find_element_by_xpath("//div[text()='Price -- Low to High']").click()
    time.sleep(5)
    expected_price_list = ['₹1,12,990', '₹1,12,990', '₹1,14,990', '₹1,29,985', '₹1,29,985', '₹1,35,999', '₹1,54,990',
                           '₹1,66,292', '₹1,69,990',
                           '₹1,99,900', '₹2,24,990', '₹2,24,990', '₹2,29,990', '₹2,39,900', '₹2,39,990', '₹2,39,900']
    actual_price_list = driver.find_elements_by_xpath("//div[@class='_1vC4OE _2rQ-NK']")
    for i in range(0, len(expected_price_list)):
        if actual_price_list[i].text == expected_price_list[i]:
            print("The prouct price is valid")
        else:
            print("The product price is invalid")


verify_low_to_high_prices("Macbook pro")
