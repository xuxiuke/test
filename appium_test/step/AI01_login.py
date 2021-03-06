# coding=utf-8

"""
作者: Duke
文件名: AI01_login.py
创建时间: 2019/12/24-14:26
"""

from appium_test.PO import base_page
from PO import excel
import time


class Login(base_page.Action):

    # 1、账号已有住宅情况，登录成功
    def login_success(self):
        self.sign_in_page()  # 登陆页面
        self.login('18013986382', 'wl123456789')
        return self.find_item('我的')  # 验证是否有首页导航栏

    # 2、账号没有住宅情况，登陆成功
    def login_success_no_house(self):
        self.sign_in_page()  # 登陆页面
        self.login('wlink2019003@126.com', 'v7654321')
        return self.find_item('添加网关')  # 验证是否进入添加网关页面

    # 3、注册页面
    def register(self):
        self.welcome_to_use_page()  # 欢迎使用页面
        self.find_text('注册').click()  # 点击注册按钮
        return self.find_item('注册即代表阅读并同意')

    # 4、使用条款与免责协议页面
    def agreement_page(self):
        self.register()  # 注册页面
        self.switch_h5()
        self.find_text('《隐私政策声明》').click()  # 点击使用条款与免责协议
        time.sleep(3)
        return self.find_item('《用户服务声明》')

    # 5、注册页面，获取验证码按钮置灰不可点击
    def register_no_phone(self):
        self.register()  # 注册页面
        return self.get_colour_text('获取验证码')  # 验证按钮颜色是否正确

    # 6、注册页面，输入手机号少一位，获取验证码按钮置灰不可点击
    def register_phone_10(self):
        self.register()  # 注册页面
        self.find_text('手机号/邮箱').send_keys('1801398638')
        return self.get_colour_text('获取验证码')  # 验证按钮颜色是否正确

    # 7、注册页面，输入手机号，获取验证码按钮可以点击
    def register_right_phone(self):
        self.register()  # 注册页面
        self.find_text('手机号/邮箱').send_keys('18013986383')
        return self.get_colour_text('获取验证码')  # 验证按钮颜色是否正确

    # 8、注册页面，输入已注册手机号，点击获取验证码按钮，弹窗手机号已被注册
    def register_phone_used(self):
        self.register()  # 注册页面
        self.find_text('手机号/邮箱').send_keys('18013986382')
        self.find_text('获取验证码').click()  #点击获取验证码按钮
        time.sleep(1)
        return self.find_item('手机号已被注册')  # 验证是否有手机号已被注册弹窗

    # 9、注册页面手机号已被注册弹窗，点击取消按钮，弹窗消失
    def register_popup_cancel(self):
        self.register()  # 注册页面
        self.find_text('手机号/邮箱').send_keys('18013986382')
        self.find_text('获取验证码').click()  # 点击获取验证码按钮
        time.sleep(1)
        self.find_text('取消').click()  # 点击取消按钮
        return self.find_item('手机号已被注册')  # 验证是否有手机号已被注册弹窗

    # 10、注册页面手机号已被注册弹窗，点击去登录按钮，进入登录页面
    def register_land(self):
        self.register()  # 注册页面
        self.find_text('手机号/邮箱').send_keys('18013986382')
        self.find_text('获取验证码').click()  # 点击获取验证码按钮
        time.sleep(1)
        self.find_text('去登录').click()  # 点击去登录按钮
        return self.find_text('手机号/邮箱') and self.find_text('密码')  # 验证是否进入登录页面

    # 11、注册页面，输入未注册手机号，点击获取验证码按钮，进入输入验证码页面
    def register_code_page(self):
        self.register()  # 注册页面
        self.find_text('手机号/邮箱').send_keys('18013980000')
        self.find_text('获取验证码').click()  # 点击获取验证码按钮
        time.sleep(1)
        return self.find_item('输入验证码')

    # 12、注册-输入验证码页面，输入错误验证码，提示验证码错误
    def code_page_wrongcode(self):
        self.register()  # 注册页面
        self.find_text('手机号/邮箱').send_keys('18013980000')
        self.find_text('获取验证码').click()  # 点击获取验证码按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('code_1')).send_keys('1')
        self.find_xpath(excel.xpath_con('code_2')).send_keys('2')
        self.find_xpath(excel.xpath_con('code_3')).send_keys('3')
        self.find_xpath(excel.xpath_con('code_4')).send_keys('9')
        time.sleep(2)
        return self.find_item('验证码错误')

    # 13、登录页面
    def sign_in(self):
        self.sign_in_page()  # 登录页面
        return self.find_text('手机号/邮箱') and self.find_text('密码')  # 验证是否进入登录页面

    # 14、登录页面，登录按钮置灰
    def login_button_gray(self):
        self.sign_in_page()  # 登录页面
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮颜色置灰

    # 15、登录页面，输入正确账号，不输入密码，登录按钮置灰
    def login_no_password(self):
        self.sign_in_page()  # 登录页面
        self.find_text('手机号/邮箱').send_keys('18013986382')  # 输入账号
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮颜色置灰

    # 16、登录页面，不输入账号，输入正确格式密码，登录按钮置灰
    def login_no_account(self):
        self.sign_in_page()  # 登录页面
        self.find_text('密码').send_keys('@q1234567')  # 输入密码
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮颜色置灰

    # 17、登录页面，输入手机号账号少一位（1801398638），输入正确格式密码，登录按钮置灰
    def login_one_less_cell_phone_number(self):
        self.sign_in_page()  # 登录页面
        self.find_text('手机号/邮箱').send_keys('1801398638')  # 输入手机号少一位
        self.find_text('密码').send_keys('@q1234567')  # 输入密码
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮颜色置灰

    # 18、登录页面，输入手机号账号多一位（180139863821），输入正确格式密码，登录按钮置灰
    def login_one_more_cell_phone_number(self):
        self.sign_in_page()  # 登录页面
        self.find_text('手机号/邮箱').send_keys('180139863821')  # 输入手机号多一位
        self.find_text('密码').send_keys('@q1234567')  # 输入密码
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮颜色置灰

    # 19、登录页面，输入邮箱账号没有@（qwerty126.com），输入正确格式密码，登录按钮置灰
    def login_wrong_mailbox_account_1(self):
        self.sign_in_page()  # 登录页面
        self.find_text('手机号/邮箱').send_keys('qwerty126.com')  # 输入邮箱账号少@
        self.find_text('密码').send_keys('@q1234567')  # 输入密码
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮颜色置灰

    # 20、登录页面，输入邮箱账号没有‘.’（1234567@126com），输入正确格式密码，登录按钮置灰
    def login_wrong_mailbox_account_2(self):
        self.sign_in_page()  # 登录页面
        self.find_text('手机号/邮箱').send_keys('1234567@126com')  # 输入邮箱账号少.
        self.find_text('密码').send_keys('@q1234567')  # 输入密码
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮颜色置灰

    # 21、登录页面，输入正确的账号，输入全数字密码（123456789），登录按钮置灰
    def login_wrong_password_all_digital(self):
        self.sign_in_page()  # 登录页面
        self.find_text('手机号/邮箱').send_keys('18013986382')  # 输入账号
        self.find_text('密码').send_keys('123456789')  # 输入全数字密码
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮颜色置灰

    # 22、登录页面，输入正确的账号，输入全字母密码（qwertyuiop），登录按钮置灰
    def login_wrong_password_all_letter(self):
        self.sign_in_page()  # 登录页面
        self.find_text('手机号/邮箱').send_keys('18013986382')  # 输入账号
        self.find_text('密码').send_keys('qwertyuiop')  # 输入全字母密码
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮颜色置灰

    # 23、登录页面，输入正确的账号，输入全符号密码（！@#￥%……&*（）），登录按钮置灰
    def login_wrong_password_all_character(self):
        self.sign_in_page()  # 登录页面
        self.find_text('手机号/邮箱').send_keys('18013986382')  # 输入账号
        self.find_text('密码').send_keys('！@#￥%……&*（）')  # 输入全字符密码
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮颜色置灰

    # 24、登录页面，输入正确的账号，输入少于8位密码（@q12345），登录按钮置灰
    def login_wrong_password_less_8(self):
        self.sign_in_page()  # 登录页面
        self.find_text('手机号/邮箱').send_keys('18013986382')  # 输入账号
        self.find_text('密码').send_keys('@q12345')  # 输入少于8位密码
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮颜色置灰

    # 25、登录页面，输入正确的账号，输入正确密码，登录按钮激活
    def login_right_account_password(self):
        self.sign_in_page()  # 登录页面
        self.find_text('手机号/邮箱').send_keys('18013986382')  # 输入账号
        self.find_text('密码').send_keys('wl123456789')  # 输入密码
        return self.get_colour_xpath(excel.xpath_con('login'))  # 登录按钮激活

    # 26、登录页面，输入未注册账号（18013980000），输入正确密码，点击登录，提示：用户不存在
    def user_does_not_exist(self):
        self.sign_in_page()  # 登录页面
        self.login('18013980000','wl123456789')  # 不存在账号登录
        return self.find_item('用户不存在')  # 验证用户不存在是否显示

    # 27、登录页面，输入正确的账号（18013986382），输入错误密码，点击登录，提示，密码错误
    def wrong_password(self):
        self.sign_in_page()  # 登录页面
        self.login('18013986382', 'as123456789')  # 错误密码登录
        return self.find_item('密码错误')  # 验证提示密码错误是否显示

    # 28、登录页面，输入正确的账号（17751027576），输入错误密码，连续点击登录3次，弹出找回密码弹窗
    def wrong_password_3(self):
        self.sign_in_page()  # 登录页面
        self.login('17751027576', 'v987456321')  # 错误密码登录
        n = 0
        while not self.find_item('您的账号或密码不正确，是否找回密码？') and n < 4:
            self.find_xpath(excel.xpath_con('login')).click()  # 登录
            time.sleep(3)
            n = n + 1
        return self.find_item('您的账号或密码不正确，是否找回密码？')  # 验证找回密码弹窗

    # 29、登录页面，找回密码弹窗（16574489975），点击取消按钮，弹窗消失
    def find_password_popup(self):
        self.sign_in_page()  # 登录页面
        self.login('16574489975', 'v987456321')  # 错误密码登录
        n = 0
        while not self.find_item('您的账号或密码不正确，是否找回密码？') and n < 4:
            self.find_xpath(excel.xpath_con('login')).click()  # 登录
            time.sleep(3)
            n = n + 1
        self.find_text('取消').click()  # 点击取消按钮
        return self.find_item('您的账号或密码不正确，是否找回密码？')  # 验证找回密码弹窗

    # 30、登录页面，找回密码弹窗（16558785250），点击找回密码按钮，进入找回密码页面
    def find_password_page_2(self):
        self.sign_in_page()  # 登录页面
        self.login('16558785250', 'v987456321')  # 错误密码登录
        n = 0
        while not self.find_item('您的账号或密码不正确，是否找回密码？') and n < 4:
            self.find_xpath(excel.xpath_con('login')).click()  # 登录
            time.sleep(3)
            n = n + 1
        self.find_xpath(excel.xpath_con('find_password')).click()  # 点击找回密码按钮
        time.sleep(1)
        return self.find_item('获取验证码')  # 验证是否进入找回密码页面

    # 31、登录页面，找回密码弹窗（16574488587、16558785248），点击取消后再点击2次登录，弹出安全提示弹窗
    def safety_tips_popup(self):
        self.sign_in_page()  # 登录页面
        self.login('16574488587', 'v987456321')  # 错误密码登录
        n = 0
        while not self.find_item('您的账号或密码不正确，是否找回密码？') and n < 4:
            self.find_xpath(excel.xpath_con('login')).click()  # 登录
            time.sleep(3)
            n = n + 1
        self.find_text('取消').click()  # 点击取消按钮
        time.sleep(1)
        self.find_xpath(excel.xpath_con('login')).click()  # 登录
        time.sleep(3)
        m = 0
        while not self.find_item('安全提示') and m < 2:
            self.find_xpath(excel.xpath_con('login')).click()  # 登录
            time.sleep(3)
            m = m + 1
        return self.find_item('安全提示')  # 验证安全提示弹窗

    # 32、登录页面，点击验证码登录，进入验证码登录页面
    def code_login_page(self):
        self.sign_in_page()  # 登录页面
        self.find_text('验证码登录').click()  # 点击验证码登录按钮
        return self.find_item('获取验证码')  # 验证是否进入验证码登录页面

    # 33、验证码登录页面，获取验证码按钮置灰
    def code_login_page_none(self):
        self.sign_in_page()  # 登录页面
        self.find_text('验证码登录').click()  # 点击验证码登录按钮
        return self.get_colour_text('获取验证码')  # 验证获取验证码按钮颜色

    # 34、验证码登录页面，输入正确手机号账号，获取验证码激活
    def code_login_page_right_phone(self):
        pass

    # 35、验证码登录页面，输入正确邮箱账号，获取验证码激活
    def code_login_page_right_mail(self):
        pass

    # 36、验证码登录页面，输入未注册账号，获取验证码激活，提示：用户不存在
    def code_login_page_unregistered(self):
        pass

    # 37、验证码登录页面，输入正确账号，点击获取验证码按钮，进入输入验证码页面
    def code_login_enter_code_page(self):
        pass

    # 38、验证码登录-输入验证码页面，输入错误验证码，提示：验证码错误
    def code_login_enter_code_page_wrong_code(self):
        pass

    # 39、登录页面，点击找回密码，进入找回密码页面
    def find_password_page(self):
        pass

    # 40、找回密码页面，获取验证码按钮置灰
    def find_password_page_none(self):
        pass

    # 41、找回密码页面，输入正确手机号账号，获取验证码激活
    def find_password_page_right_phone(self):
        pass

    # 42、找回密码页面，输入正确邮箱账号，获取验证码激活
    def find_password_page_right_mail(self):
        pass

    # 43、找回密码页面，输入未注册账号，获取验证码激活，提示：用户不存在
    def find_password_page_unregistered(self):
        pass

    # 44、找回密码页面，输入正确账号，点击获取验证码，进入输入验证码页面
    def find_password_enter_code_page(self):
        pass

    # 45、找回密码-输入验证码页面，输入错误验证码，提示：验证码错误
    def find_password_enter_code_page_wrong_code(self):
        pass
