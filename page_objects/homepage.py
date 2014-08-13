from page_objects.comparison_page import ComparisonPage


class Homepage():
    
    element_title_selector = 'h3.list-of-entities-item-headline a'
    element_text_selector = 'span.list-of-entities-item-body-rating-item-string'
    element_image_selector = 'a.list-of-entities-item-image-container'
    
    def __init__(self, driver, wait, fresh_load=False):
        self.driver = driver
        self.wait = wait
        if fresh_load:
#             self.driver.get("file:///C:/Users/tim-vm-015/Downloads/Best.htm")
            self.driver.get("http://azaem-web1-test2.awsdev.telegraph.co.uk/best.html")
        self.product_area = self.wait.until(lambda driver:driver.find_element_by_css_selector("div.list-of-entities-item-link"))
    
    def element_title(self):
        return self.wait.until(lambda driver:driver.find_element_by_css_selector(self.element_title_selector))
    
    def element_text(self):
        return self.wait.until(lambda driver:driver.find_element_by_css_selector(self.element_text_selector))
    
    def element_image(self):
        return self.wait.until(lambda driver:driver.find_element_by_css_selector(self.element_image_selector))

    def click_product_area(self):
        self.product_area.click()
        return ComparisonPage(self.driver, self.wait)
