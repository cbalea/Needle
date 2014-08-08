import time


class BasePage():
    
    def switchToNewestWindow(self):
        self.waitUntilPopupOpens()
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
    
    def waitUntilPopupOpens(self, timeout=5):
        windows = len(self.driver.window_handles)
        while(windows == 1 and timeout < 0):
            time.sleep(1)
            windows = len(self.driver.window_handles)
            timeout -=1
        if(timeout == 0):
            raise Exception("Popup did not open")
