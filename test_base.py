import os
from subprocess import Popen
import time

from needle.cases import NeedleTestCase
from server_related import ServerRelated


class TestBase(NeedleTestCase):
    
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