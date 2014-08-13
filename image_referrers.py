class ImageReferrers():
    
    def __init__(self, brw):
        self.browser = brw
    
    
    def HOMEPAGE_ELEMENT_TITLE(self):
        return 'element-title-' + self.browser
        
    def HOMEPAGE_ELEMENT_IMAGE(self):
        return 'element-image-' + self.browser
    
    def HOMEPAGE_ELEMENT_TEXT(self):
        return 'element-text-' + self.browser
    
    def PRODUCT_PAGE_OVERALL_RATING(self): 
        return 'overall-rating-' + self.browser
    
    def PRODUCT_PAGE_GOLD_RIBBON(self):
        return 'gold-ribbon-' + self.browser