from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')        

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
show_message_button = chrome_browser.find_element_by_class_name('btn-default')


user_message= chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_select(_'#get-input > .btn')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')
show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

chrome_browser.quit()

