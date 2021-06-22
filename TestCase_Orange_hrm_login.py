from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest2
import HtmlTestRunner

class OrangeHRMTest(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\\Users\\DELL\\PycharmProjects\\unittesthtml\\Drivers\\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM",self.driver.title,"webpage title is not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    @classmethod
    def teardownClass(cls):
        cls.driver.quit()
        print("Test completed....")

if __name__=="__main__":
    unittest2.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\DELL\\PycharmProjects\\unittesthtml\\Reports'))
