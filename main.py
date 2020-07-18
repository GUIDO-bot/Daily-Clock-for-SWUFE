from selenium import webdriver

def Main(username,password):
    option = webdriver.ChromeOptions()
    option.set_headless()
    global browser
    browser = webdriver.Chrome(chrome_options=option)
    browser.get('http://xsdaka.iswufe.info/')
    browser.find_element_by_xpath('//*[@id="username"]').click()
    browser.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    browser.find_element_by_xpath('//*[@id="password"]').click()
    browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    # 登录
    browser.find_element_by_xpath('//*[@id="casLoginForm"]/p[4]/button').click()
    # 进入填报
    browser.find_element_by_xpath('/html/body/div[3]/img').click()
    # 提交
    browser.find_element_by_xpath('//*[@id="checkb"]').click()
    browser.find_element_by_xpath('//*[@id="loadingDiv"]/button').click()
    # 确认
    browser.switch_to_alert().accept()
    # 关闭
    browser.close()
    return 0
if __name__ == "__main__":
    Main('用户名','密码')
