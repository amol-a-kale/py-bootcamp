import time
import pytest

from selenium import webdriver


class TestAmazonProduct:

    @pytest.fixture
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/gaurnitai/Desktop/PySeBootcamp/drivers/chromedriver")
        self.driver.get("https://www.amazon.in")
        self.driver.maximize_window()
        time.sleep(4)
        yield
        time.sleep(3)
        self.driver.close()
        self.driver.quit()

    def test_product_title(self, setUp):
        self.driver.save_screenshot("/Users/gaurnitai/Desktop/dummyrepo/py-se-bootcamp/screenshots" + "homepage.png")
        search_box = self.driver.find_element_by_id("twotabsearchtextbox")
        search_box.send_keys("Macbook pro")
        search_icon = self.driver.find_element_by_xpath("//input[@type='submit']")
        search_icon.click()
        time.sleep(5)
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/dummyrepo/py-se-bootcamp/screenshots" + "productlisting.png")
        parent_window = self.driver.current_window_handle
        print(parent_window)
        self.driver.find_element_by_xpath("(//a[@class='a-link-normal a-text-normal'])[1]").click()
        time.sleep(3)
        windows_set = self.driver.window_handles
        print(windows_set)

        for window in windows_set:
            if (window != parent_window):
                self.driver.switch_to.window(window)
                self.driver.save_screenshot(
                    "/Users/gaurnitai/Desktop/dummyrepo/py-se-bootcamp/screenshots/" + "childtab.png")
        productTitle = self.driver.find_element_by_id("productTitle")
        print(productTitle.text)
        assert productTitle.text == "Macbook pro"

    def test_product_price(self, setUp):
        self.driver.save_screenshot("/Users/gaurnitai/Desktop/dummyrepo/py-se-bootcamp/screenshots" + "homepage.png")
        search_box = self.driver.find_element_by_id("twotabsearchtextbox")
        search_box.send_keys("Macbook pro")
        search_icon = self.driver.find_element_by_xpath("//input[@type='submit']")
        search_icon.click()
        time.sleep(5)
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/dummyrepo/py-se-bootcamp/screenshots" + "productlisting.png")
        parent_window = self.driver.current_window_handle
        print(parent_window)
        self.driver.find_element_by_xpath("(//a[@class='a-link-normal a-text-normal'])[1]").click()
        time.sleep(3)
        windows_set = self.driver.window_handles
        print(windows_set)

        for window in windows_set:
            if (window != parent_window):
                self.driver.switch_to.window(window)
                self.driver.save_screenshot(
                    "/Users/gaurnitai/Desktop/dummyrepo/py-se-bootcamp/screenshots/" + "childtab.png")

        productPrice = self.driver.find_element_by_id("priceblock_ourprice")
        assert productPrice.text == "₹ 1,27,990.00"
