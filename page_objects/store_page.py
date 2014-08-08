from page_objects.base_page import BasePage


class StorePage(BasePage):
    
    def __init__(self, driver, wait, fresh_load=False):
        self.driver = driver
        self.wait = wait
        self.switchToNewestWindow()
        self.wait.until(lambda driver:driver.find_element_by_xpath("//div[@title='Google']"))
