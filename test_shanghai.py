import unittest

from test_base import TestBase
from tools.xmltestrunner.xmlrunner import XMLTestRunner


class ShanghaiTest(TestBase):

    def test_homepage(self):
        self.driver.get('http://azaem-web1-test2.awsdev.telegraph.co.uk/best.html')
        self.assertScreenCapture('h3.list-of-entities-item-headline a', 'element-title')

if __name__ == "__main__":
    unittest.main()
#     loader = unittest.TestLoader()
#     tests = loader.discover(".")
#     runner = XMLTestRunner()
#     runner.run(tests)