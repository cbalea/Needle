class ImageReferrers():
    
    def __init__(self, brw):
        self.brw = brw
    
    
    def HOMEPAGE_ELEMENT_TITLE(self):
        return 'element-title-' + self.brw
        
    def HOMEPAGE_ELEMENT_IMAGE(self):
        return 'element-image-' + self.brw
    
    def HOMEPAGE_ELEMENT_TEXT(self):
        return 'element-text-' + self.brw
    
    def PRODUCT_PAGE_OVERALL_RATING(self): 
        return 'overall-rating-' + self.brw
    
    def PRODUCT_PAGE_GOLD_RIBBON(self):
        return 'gold-ribbon-' + self.brw