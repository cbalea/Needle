import os
from subprocess import Popen, PIPE

from needle.cases import NeedleTestCase


class ServerRelated():
    
    def get_project_directory_path(self):
        path = os.path.abspath(__file__)
        fold_index = path.index("Needle\\")
        return path[:fold_index]+"Needle\\"
    
    def get_path_in_project(self, location):
        return self.get_project_directory_path() + location


class TestBase(NeedleTestCase):
    def assertScreenCapture(self, target_selector, base_image):
#         try:
#             self.assertScreenshot(target_selector, base_image)
#         except AssertionError:
        baseline_png_path = ServerRelated().get_path_in_project("screenshots\\baseline\\%s.png" %base_image)
        baseline_jpg_path = ServerRelated().get_path_in_project("screenshots\\baseline\\%s.jpg" %base_image)
        actual_png_path = ServerRelated().get_path_in_project("screenshots\\%s.png" %base_image)
        actual_jpg_path = ServerRelated().get_path_in_project("screenshots\\%s.jpg" %base_image)
        
        convert_baseline_to_jpg = "convert %s %s" %(baseline_png_path, baseline_jpg_path)
#         convert_actual_to_jpg = "convert %s %s" %(actual_png_path, actual_jpg_path)
        print convert_baseline_to_jpg
#         print convert_actual_to_jpg
        Popen(convert_baseline_to_jpg)
#         Popen(convert_actual_to_jpg)
#         
#         compare_images = "compare %s %s diff.png" %(baseline_jpg_path, actual_jpg_path)
#         print compare_images
#         Popen(compare_images, stdout=PIPE)
        
        raise AssertionError("Images differ. Difference exported to screenshots\\diff.png")

class BBCNewsTest(TestBase):

    def test_masthead(self):
#         self.driver.get('http://www.bbc.co.uk/news/')
        self.assertScreenCapture('#blq-mast', 'bbc-masthead')