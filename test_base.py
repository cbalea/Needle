import os
from subprocess import Popen
import time

from needle.cases import NeedleTestCase
from needle.driver import NeedleIe, NeedleFirefox
from selenium.webdriver.support.wait import WebDriverWait

from image_referrers import ImageReferrers
from server_related import ServerRelated


class TestBase(NeedleTestCase, ImageReferrers):
    
    def __init__(self, *args, **kwargs):
        super(NeedleTestCase, self).__init__(*args, **kwargs)
        self.output_directory = ServerRelated().get_path_in_project("screenshots")
        self.baseline_directory = ServerRelated().get_path_in_project("screenshots/baseline")

        if not os.path.exists(self.output_directory):
            raise Exception("Screenshots output directory %s does not exist! Please create it." %self.output_directory)
        if not os.path.exists(self.baseline_directory):
            raise Exception("Baseline directory %s does not exist! Please create it." %self.baseline_directory)
    
    @classmethod
    def get_web_driver(cls):
#         requested_browser = os.environ.get('NEEDLE_BROWSER')
#         if requested_browser == "ie":
#         cls.browser = "ie"
#         return NeedleIe()
#         else:
        cls.browser = "ff"
        return NeedleFirefox()
    
    def setUp(self):
        self.initializeWait(self.driver)
        self.imgRef = ImageReferrers(self.__class__.browser)
        NeedleTestCase.setUp(self)
    
    def initializeWait(self, driver, timeout=10):
        self.wait = WebDriverWait(driver, timeout)
        return self.wait
    
    
    
    def split_path_in_subfolder_and_filename(self, file_path):
        filename = file_path.split("\\")[-1]
        subfolder = file_path[:file_path.index(filename)]
        return subfolder, filename
    
    def wait_for_file_to_exist(self, file_path, timeout):
        subfolder, filename = self.split_path_in_subfolder_and_filename(file_path)
        
        while (filename not in os.listdir(ServerRelated().get_path_in_project(subfolder))) and (timeout > 0):  # case sensitive file_path search
            timeout -= 0.5
            time.sleep(0.5)
        if timeout <= 0:
            return False
        else:
            return True
    
    def fail_if_file_not_exists(self, filepath, timeout):
        if not self.wait_for_file_to_exist(filepath, timeout):
            raise Exception("File %s was not found after %d sec." %(filepath, timeout))
        else:
            pass
    
    def fail_if_file_exists(self, filepath, timeout):
        if self.wait_for_file_to_exist(filepath, timeout):
            raise Exception("File %s still exists after %d sec." %(filepath, timeout))
        else:
            pass
    
    def assertScreenCapture(self, target_selector, base_image):
        try:
            self.assertScreenshot(target_selector, base_image)
        except AssertionError:
            '''
                Convert to jpg
            '''
            baseline_png_path = ServerRelated().get_path_in_project("screenshots\\baseline\\%s.png" %base_image)
            baseline_jpg_path = ServerRelated().get_path_in_project("screenshots\\baseline\\%s.jpg" %base_image)
            actual_png_path = ServerRelated().get_path_in_project("screenshots\\%s.png" %base_image)
            actual_jpg_path = ServerRelated().get_path_in_project("screenshots\\%s.jpg" %base_image)
            
            convert_baseline_to_jpg = 'convert %s %s' %(baseline_png_path, baseline_jpg_path)
            convert_actual_to_jpg = 'convert %s %s' %(actual_png_path, actual_jpg_path)
#             print convert_baseline_to_jpg
#             print convert_actual_to_jpg
            os.system(convert_baseline_to_jpg)
            self.fail_if_file_not_exists("screenshots\\baseline\\%s.jpg" %base_image, 10)
            os.system(convert_actual_to_jpg)
            self.fail_if_file_not_exists("screenshots\\%s.jpg" %base_image, 10)
            
            '''
                Remove old -diff file if it exists
            ''' 
            diff_image = ServerRelated().get_path_in_project("screenshots\\failures\\%s-diff.png" %base_image)
            try:
                os.remove(diff_image)
                self.fail_if_file_exists("screenshots\\failures\\%s-diff.png" %base_image, 10)
            except:
                pass
            
            '''
                Compare images
            '''
            compare_images = 'compare %s %s %s' %(baseline_jpg_path, actual_jpg_path, diff_image)
#             print compare_images
            Popen(compare_images)

            if self.wait_for_file_to_exist("screenshots\\failures\\%s-diff.png" %base_image, 10):
                append_msg = " Difference exported to screenshots\\failures\\%s-diff.png" %base_image
            else:
                append_msg = " Image widths or heights differ. Diff file not exported."
            
            raise AssertionError("Images differ." + append_msg)
    
    def assertElementsAlign(self, direction="vertical", *selectors):
        alignments = []
        
        if len(selectors) < 2:
            raise Exception("Need at least 2 selectors to compare alignment.")
        
        # get elements alignments
        for sel in selectors:
            element = self.wait.until(lambda driver:driver.find_element_by_css_selector(sel))
            if direction == "vertical":
                alignments.append(element.location['y'])
            elif direction == "horizontal":
                alignments.append(element.location['x'])
        
        # verify alignments are the same
        baseline = alignments[0]
        for i in range(len(alignments)):
            if alignments[i] != baseline:
                raise AssertionError("Elements are not aligned %s: \n\t %dpx: %s \n\t %dpx: %s" %(direction, baseline, selectors[0], alignments[i], selectors[i]))
        








