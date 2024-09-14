from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    search = (By.CSS_SELECTOR, "input[type='search']")
    items = (By.XPATH, "//div[@class='products']/div")
    #displayed = (By.XPATH, "div/button")

    def search_page(self):
        return self.driver.find_element(*Homepage.search)

    def search_items(self):
        return self.driver.find_element(*Homepage.items)

    #def items_displayed(self):
        #return self.driver.find_elements(*Homepage.displayed)