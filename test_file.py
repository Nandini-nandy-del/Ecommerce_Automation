import time
from Utilities.BaseClass import Baseclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from homepage import Homepage


class TestWebSite(Baseclass):

    def test_shopping(self):

        #self.driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("c")
        obj1 = Homepage(self.driver)
        obj1.search_page().send_keys("c")
        time.sleep(3)
        carts = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
        time.sleep(3)
        for cart in carts:
            cart.find_element(By.XPATH, "div/button").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
        self.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
        self.driver.find_element(By.XPATH, "//button[text()='Apply']").click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(presence_of_element_located((By.CLASS_NAME, "promoInfo")))
        self.driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
        time.sleep(8)


