import unittest

from page_objects.homepage import Homepage
from page_objects.product_page import ProductPage
from test_base import TestBase


class TestHomepage(TestBase):
 
    def setUp(self):
        TestBase.setUp(self)
        self.homepage = Homepage(self.driver, self.wait, fresh_load=True)
    
    def test_homepage_elements(self):
        self.assertScreenCapture(self.homepage.element_title_selector, self.imgRef.HOMEPAGE_ELEMENT_TITLE())
        self.assertScreenCapture(self.homepage.element_image_selector, self.imgRef.HOMEPAGE_ELEMENT_IMAGE())
        self.assertScreenCapture(self.homepage.element_text_selector, self.imgRef.HOMEPAGE_ELEMENT_TEXT())
  
    def test_homepage_navigation(self):
        self.comparison_page = self.homepage.click_product_area()
    
    def test_homepage_elements_align(self):
        self.assertElementsAlign("vertical", self.homepage.element_text_selector, self.homepage.element_title_selector)


class TestProductPage(TestBase):
      
    def setUp(self):
        TestBase.setUp(self)
        self.product_page = ProductPage(self.driver, self.wait, fresh_load=True)
      
    def test_product_page_elements(self):
        self.assertScreenCapture(self.product_page.overall_rating, self.imgRef.PRODUCT_PAGE_OVERALL_RATING())
        self.assertScreenCapture(self.product_page.gold_ribbon, self.imgRef.PRODUCT_PAGE_GOLD_RIBBON())
      
    def test_homepage_navigation(self):
        self.store_page = self.product_page.click_go_to_store()

if __name__ == "__main__":
    unittest.main()