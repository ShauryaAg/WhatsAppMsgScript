from selenium import webdriver

# Change the executable_path to the correct path of your chromedriver.exe
driver = webdriver.Chrome(
    executable_path='D:\Documents\CodingBlocks\CNinjas\Selenium\chromedriver_win32\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input("Enter the name of person/group: ")
msg = input("Enter message to be sent: ")
count = int(input("Enter count: "))

driver.implicitly_wait(5)

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath(
    '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msg_box.send_keys(msg)
    send_button = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
    send_button.click()
