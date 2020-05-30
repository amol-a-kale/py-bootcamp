import time

from selenium import webdriver
import pytest


class TestAmazonWebsite:

    @pytest.fixture
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Sanket\\Desktop\\py_se_boot\\webdriver\\chromedriver.exe")
        self.driver.get("https://www.amazon.in")
        self.driver.maximize_window()
        time.sleep(4)
        yield
        time.sleep(3)
        self.driver.close()
        self.driver.quit()

    def test_website_title(self, setUp):
        # driver = webdriver.Chrome("/Users/gaurnitai/Desktop/PySeBootcamp/drivers/chromedriver")
        # driver.get("https://www.amazon.in")
        # driver.maximize_window()
        # time.sleep(4)
        # self.driver.save_screenshot("/Users/gaurnitai/Desktop/dummyrepo/py-se-bootcamp/screenshots" + "homepage.png")
        pageTitle = self.driver.title
        assert pageTitle == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"

    def test_search_functionality(self, setUp):
        # driver = webdriver.Chrome("/Users/gaurnitai/Desktop/PySeBootcamp/drivers/chromedriver")
        # driver.get("https://www.amazon.in")
        # driver.maximize_window()
        # time.sleep(4)
        # self.driver.save_screenshot("/Users/gaurnitai/Desktop/dummyrepo/py-se-bootcamp/screenshots" + "homepage.png")
        search_box = self.driver.find_element_by_id("twotabsearchtextbox")
        search_box.send_keys("Macbook pro")
        search_icon = self.driver.find_element_by_xpath("//input[@type='submit']")
        search_icon.click()
        time.sleep(5)
        # self.driver.save_screenshot(
        #     "/Users/gaurnitai/Desktop/dummyrepo/py-se-bootcamp/screenshots" + "productlisting.png")
        searched_product = self.driver.find_element_by_xpath("(//a[@class='a-link-normal a-text-normal'])[1]")
        assert searched_product.is_displayed() == True
