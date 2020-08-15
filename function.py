from selenium import webdriver
from selenium.webdriver.support.select import Select

def choose(_id,value):
    s1 = Select(browser.find_element_by_id(_id))  # 实例化Select
    s1.select_by_value(value)  # 选择value

def Main(username,password):
    #option = webdriver.ChromeOptions()
    #option.set_headless()
    global browser
    browser = webdriver.Chrome()
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
    s = ''
    while s != '请准确填写每日打卡内容。并确认各项内容无误填漏填后，再进行提交。':
        try:
            s = Main('acount','password')
        except:
            browser.quit()
