from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\Your_Name\\Downloads\\chromedriver_win32\\chromedriver.exe') #Change the executable_path to the correct path of your chromedriver.exe

driver.get('https://web.whatsapp.com/')


name = input("Enter the name of user: ")
msg = input("Enter message to be sent: ")
count = int(input("Enter count: "))

input()

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_1Plpp')


for i in range(count):
    msg_box.send_keys(msg)
    send_button = driver.find_element_by_xpath('//button[@class="_35EW6"]')
    send_button.click()