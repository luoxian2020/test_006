from selenium.webdriver.support.wait import WebDriverWait
from Base.get_driver import get_driver
from time import sleep

driver = get_driver("com.tpshop.malls",".SPMainActivity")

sleep(3)
# 我的
my = "//*[contains(@resource-id,'com.tpshop.malls:id/tab_txtv') and contains(@text,'我的')]"
driver.find_element_by_xpath(my).click()
sleep(3)
# 登陆/注册
driver.find_element_by_id("com.tpshop.malls:id/nickname_txtv").click()
sleep(3)
# 输入用户名

driver.find_element_by_id("com.tpshop.malls:id/edit_phone_num").send_keys("1111")

# 输入密码
driver.find_element_by_id("com.tpshop.malls:id/edit_password").send_keys("1111")

# 点击登陆
driver.find_element_by_id("com.tpshop.malls:id/btn_login").click()


# 获取提示消息
to = WebDriverWait(driver, 5 , 0.1).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'不存在')]"))

print(to.text)