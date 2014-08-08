from page_objects.store_page import StorePage


class ProductPage():
    
    overall_rating = 'div.entity-property.component.entity-property-overall-rating'
    gold_ribbon = 'div.product-ribbon.promoted-gold'
    
    def __init__(self, driver, wait, fresh_load=False):
        self.driver = driver
        self.wait = wait
        if fresh_load:
            self.driver.get("http://azaem-web1-test2.awsdev.telegraph.co.uk/best/smartphones/apple-iphone-5s/")
        self.wait.until(lambda driver:driver.find_element_by_css_selector("body.productRenderer"))


    def click_go_to_store(self):
        self.go_to_store_button = self.wait.until(lambda driver:driver.find_element_by_css_selector("a.call-to-action-box-btn"))
        self.go_to_store_button.click()
        return StorePage(self.driver, self.wait)