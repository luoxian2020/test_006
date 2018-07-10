from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from Base.get_driver import get_driver

# 点击 我的
driver = get_driver('com.tpshop.malls', '.SPMainActivity')
sleep(3)
driver.find_element_by_xpath(
    "//*[contains(@resource-id,'com.tpshop.malls:id/tab_txtv') and contains(@text,'我的')]").click()

# 点击 登录；注册
sleep(3)
# driver.find_element_by_id('com.tpshop.malls:id/nickname_txtv').click()
driver.find_element_by_id("com.tpshop.malls:id/nickname_txtv").click()
sleep(3)
# 输入账号
driver.find_element_by_id('com.tpshop.malls:id/edit_phone_num').send_keys('111')

# 输入密码
driver.find_element_by_id('com.tpshop.malls:id/edit_password').send_keys('111')

# 点击登录

# driver.find_element_by_id('com.tpshop.malls:id/btn_login').clcik()
driver.find_element_by_id("com.tpshop.malls:id/btn_login").click()
# 获取toast信息
# to = driver.find_element_by_xpath('//*[contains(@text,"用户名错误"]')
# to = WebDriverWait(driver, 5, 0.1).until(lambda x: x.find_element_by_xpath('//*[contains(@text,"不存在"]'))
to = WebDriverWait(driver, 5 , 0.1).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'不存在')]"))

print(to.text)
