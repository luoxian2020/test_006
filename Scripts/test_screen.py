import sys,os
sys.path.append(os.getcwd())
from Base.get_driver import get_driver
import allure
import time

class Test_Screen:
    def setup_class(self):
        self.driver = get_driver()
        time.sleep(3)

    def teardown_class(self):
        self.driver.quit()

    def get_screen_01(self):
        image_file = './screen/%d.png' % int(time.time())
        self.driver.get_screenshot_as_file(image_file)


        with open(image_file,'rb') as f:
            allure.attach('截图名字',f.read(),allure.attach_type.PNG)

    def test_01(self):
        allure.attach('描述','截图1')
        assert 0, self.get_screen_01()

    def test_02(self):
        allure.attach('描述','截图2')
        assert False, self.get_screen_01()

