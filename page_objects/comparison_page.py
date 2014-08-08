class ComparisonPage():
    
    def __init__(self, driver, wait, fresh_load=False):
        self.driver = driver
        self.wait = wait
        if fresh_load:
            self.driver.get("http://azaem-web1-test2.awsdev.telegraph.co.uk/best/smartphones/")
        self.wait.until(lambda driver:driver.find_element_by_css_selector("body.comparisonRenderer"))
