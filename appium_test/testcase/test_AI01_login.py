# coding=utf-8

"""
作者: Duke
文件名: test_AI01_login.py
创建时间: 2019/12/24-14:41
"""

from PO.open_app import Open_app
from step import AI01_login
import unittest
import time


# @unittest.skip(u'添加场景、区域，跳过测试')
class Test001(unittest.TestCase, AI01_login.Login):  # TestCase类，所有测试用例类继承的基本类
    """登陆测试"""

    # setUp()方法用于测试用例执行前的初始化工作，如打开APP
    def setUp(self):
        self.ina = Open_app(self)
        self.ina.open()
        self.driver = self.ina.get_driver()
        self.verificationErrors = []  # 错误信息打印到这个列表
        self.accept_next_alert = True  # 是否继续接受下个警告

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 1、账号已有住宅情况，登录成功
    def test_login_success(self):
        self.assertTrue(self.login_success())

    # 2、账号没有住宅情况，登陆成功
    def test_login_success_no_house(self):
        self.assertTrue(self.login_success_no_house())

    # 3、注册页面
    def test_register(self):
        self.assertTrue(self.register())

    # 4、使用条款与免责协议页面
    def test_agreement_page(self):
        self.assertTrue(self.agreement_page())

    # 5、注册页面，获取验证码按钮置灰不可点击
    def test_register_no_phone(self):
        self.assertFalse(self.register_no_phone())

    # 6、注册页面，输入手机号少一位，获取验证码按钮置灰不可点击
    def test_register_phone_10(self):
        self.assertFalse(self.register_phone_10())

    # 7、注册页面，输入手机号，获取验证码按钮可以点击
    def test_register_right_phone(self):
        self.assertTrue(self.register_right_phone())

    # 8、注册页面，输入已注册手机号，点击获取验证码按钮，弹窗手机号已被注册
    def test_register_phone_used(self):
        self.assertTrue(self.register_phone_used())

    # 9、注册页面手机号已被注册弹窗，点击取消按钮，弹窗消失
    def test_register_popup_cancel(self):
        self.assertFalse(self.register_popup_cancel())

    # 10、注册页面手机号已被注册弹窗，点击去登录按钮，进入登录页面
    def test_register_land(self):
        self.assertTrue(self.register_land())

    # 11、注册页面，输入未注册手机号，点击获取验证码按钮，进入输入验证码页面
    def test_register_code_page(self):
        self.assertTrue(self.register_code_page())

    # 12、注册-输入验证码页面，输入错误验证码，提示验证码错误
    def test_code_page_wrongcode(self):
        self.assertTrue(self.code_page_wrongcode())

    # 13、登录页面
    def test_sign_in(self):
        self.assertTrue(self.sign_in())

    # 14、登录页面，登录按钮置灰
    def test_login_button_gray(self):
        self.assertFalse(self.login_button_gray())

    # 15、登录页面，输入正确账号，不输入密码，登录按钮置灰
    def test_login_no_password(self):
        self.assertFalse(self.login_no_password())

    # 16、登录页面，不输入账号，输入正确格式密码，登录按钮置灰
    def test_login_no_account(self):
        self.assertFalse(self.login_no_account())

    # 17、登录页面，输入手机号账号少一位（1801398638），输入正确格式密码，登录按钮置灰
    def test_login_one_less_cell_phone_number(self):
        self.assertFalse(self.login_one_less_cell_phone_number())

    # 18、登录页面，输入手机号账号多一位（180139863821），输入正确格式密码，登录按钮置灰
    def test_login_one_more_cell_phone_number(self):
        self.assertFalse(self.login_one_more_cell_phone_number())

    # 19、登录页面，输入邮箱账号没有@（qwerty126.com），输入正确格式密码，登录按钮置灰
    def test_login_wrong_mailbox_account_1(self):
        self.assertFalse(self.login_wrong_mailbox_account_1())

    # 20、登录页面，输入邮箱账号没有‘.’（1234567@126com），输入正确格式密码，登录按钮置灰
    def test_login_wrong_mailbox_account_2(self):
        self.assertFalse(self.login_wrong_mailbox_account_2())

    # 21、登录页面，输入正确的账号，输入全数字密码（123456789），登录按钮置灰
    def test_login_wrong_password_all_digital(self):
        self.assertFalse(self.login_wrong_password_all_digital())

    # 22、登录页面，输入正确的账号，输入全字母密码（qwertyuiop），登录按钮置灰
    def test_login_wrong_password_all_letter(self):
        self.assertFalse(self.login_wrong_password_all_letter())

    # 23、登录页面，输入正确的账号，输入全符号密码（！@#￥%……&*（）），登录按钮置灰
    def test_login_wrong_password_all_character(self):
        self.assertFalse(self.login_wrong_password_all_character())

    # 24、登录页面，输入正确的账号，输入少于8位密码（@q12345），登录按钮置灰
    def test_login_wrong_password_less_8(self):
        self.assertFalse(self.login_wrong_password_less_8())

    # 25、登录页面，输入正确的账号，输入正确密码，登录按钮激活
    def test_login_right_account_password(self):
        self.assertTrue(self.login_right_account_password())

    # 26、登录页面，输入未注册账号（18013980000），输入正确密码，点击登录，提示：用户不存在
    def test_user_does_not_exist(self):
        self.assertTrue(self.user_does_not_exist())

    # 27、登录页面，输入正确的账号（18013986382），输入错误密码，点击登录，提示，密码错误
    def test_wrong_password(self):
        self.assertTrue(self.wrong_password())

    # 28、登录页面，输入正确的账号（17751027576），输入错误密码，连续点击登录3次，弹出找回密码弹窗
    def test_wrong_password_3(self):
        self.assertTrue(self.wrong_password_3())

    # 29、登录页面，找回密码弹窗（wlink2019001@126.com），点击取消按钮，弹窗消失
    def test_find_password_popup(self):
        self.assertFalse(self.find_password_popup())

    # 30、登录页面，找回密码弹窗（wlink2019003@126.com），点击找回密码按钮，进入找回密码页面
    def test_find_password_page_2(self):
        self.assertTrue(self.find_password_page_2())

    # 31、登录页面，找回密码弹窗（wlink2019002@126.com），点击取消后再点击2次登录，弹出安全提示弹窗
    def test_safety_tips_popup(self):
        self.assertTrue(self.safety_tips_popup())

    # 32、登录页面，点击验证码登录，进入验证码登录页面
    def test_code_login_page(self):
        self.assertTrue(self.code_login_page())

    # 33、验证码登录页面，获取验证码按钮置灰
    def test_code_login_page_none(self):
        self.assertFalse(self.code_login_page_none())
