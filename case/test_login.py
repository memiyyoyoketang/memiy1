# coding:utf-8
from selenium import webdriver
from page.login_page import LoginPage,login_url
from page.findpage import FindPage
import unittest
import time

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.login_driver = LoginPage(self.driver)
        self.login_driver.open(login_url)
        self.find_driver = FindPage(self.driver)

    def test_01(self):
        # 第1步：输入账号：xxx
        self.login_driver.input_username("xxxx")
        # 第2步：输入密码:xx
        self.login_driver.input_psw("xxxx")
        # 第3步：点击登录按钮
        self.login_driver.click_login_button()
        time.sleep(3)
        # 第4步：获取返回结果
        t = self.login_driver.get_tip()
        print t
        # 第5步：判断结果跟预期是否一致
        self.assertIn(u"用户名或密码错误",t)

    def test_02(self):
        # 第1步：点击‘找回’按钮
        self.login_driver.click_find()
        # 第2步：获取页面元素“找回登录用户名”
        t1 = self.find_driver.get_find_text()
        print t1
        # 第3步：断言
        # 返回True 还是False
        t2 = self.find_driver.is_title_contains("找回登录用户名") # 返回True
        print t2
        self.assertTrue(t2)
        self.assertEqual(u"找回登录用户名", t1)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()