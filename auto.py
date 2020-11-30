#coding = utf-8
from selenium import webdriver

from selenium.webdriver.support.select import Select
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
from time import sleep

def auto_email(title,message,to_email):
    #三个参数分别为 邮件标题，邮件内容，收件人邮箱
    
    #发信方的信息：发信邮箱，QQ邮箱SMTP授权码
    from_addr = '填入邮箱'
    password = '填入SMTP服务验证码'

    # 收信方邮箱
    to_addr = to_email
    # 发信服务器
    smtp_server = 'smtp.qq.com'
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(message,'plain','utf-8')
    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header(title)
    # 开启发信服务，这里使用的是加密传输
    server=smtplib.SMTP_SSL(smtp_server) 
    server.connect(smtp_server,465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()


def choose(_id,value):
    s1 = Select(browser.find_element_by_id(_id))  # 实例化Select
    s1.select_by_value(value)  # 选择value


def Main(username,password):
    #option = webdriver.ChromeOptions()
    #option.set_headless()
    
    global browser
    #options = Options()
    #options.headless = True
    #Error  This
    #火狐
    #browser = webdriver.Firefox(options=options)
    #谷歌
    #browser = webdriver.Chrome(options=options,executable_path='/opt/google/chromedriver')
    #browser = webdriver.Chrome()
    
    #测试
    #browser = webdriver.Chrome()
    #Centos7下采用这种方式
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)

    browser.delete_all_cookies()
    browser.get('http://xsdaka.iswufe.info/')
    browser.find_element_by_xpath('//*[@id="username"]').click()
    browser.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    browser.find_element_by_xpath('//*[@id="password"]').click()
    browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    # 登录
    browser.find_element_by_xpath('//*[@id="casLoginForm"]/p[4]/button').click()
    # 进入填报
    browser.find_element_by_xpath('/html/body/div[3]/img').click()
    # 填报
    choose('STSFYC','是,健康')
    choose('SFBZD','否')
    choose('JSSFBQZ','否')
    choose('SFJCYQRY','否')
    choose('SFJCFR','否')
    choose('SFJCQZBR','否')
    choose('SFDGYQ','否')
    choose('FHCD','否')
    choose('LKCD','否')
    choose('SFHCDYW','否')
    choose('SFGLGC','否')
    # 提交
    browser.find_element_by_xpath('//*[@id="checkb"]').click()
    browser.find_element_by_xpath('//*[@id="loadingDiv"]/button').click()
    # 确认
    s = browser.switch_to.alert.text
    browser.switch_to.alert.accept()
    # 关闭
    browser.quit()
    return s

    

if __name__ == "__main__":
    
    s=''
    try:
        while s != '请准确填写每日打卡内容。并确认各项内容无误填漏填后，再进行提交。':
            try:
                s = Main('账号','密码')
            except:
                browser.quit()
                sleep(5)
    finally:
        if s =='请准确填写每日打卡内容。并确认各项内容无误填漏填后，再进行提交。':
            auto_email("打开成功提醒","运气真好，竟然成功了","收件人邮箱")
            #auto_email("打开成功提醒","运气真好，竟然成功了","1307317886@qq.com")
        else:
            auto_email("打卡失败！","失败原因:"+s,"收件人邮箱")