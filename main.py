from selenium import webdriver

# Change the executable_path to the correct path of your chromedriver.exe
driver = webdriver.Chrome(
    executable_path='D:\Documents\CodingBlocks\CNinjas\Selenium\chromedriver_win32\chromedriver.exe')

executor_url = driver.command_executor._url
session_id = driver.session_id


print(executor_url)
print(session_id)

# driver.get('https://web.whatsapp.com/')


# name = input("Enter the name of user: ")
# msg = input("Enter message to be sent: ")
# count = int(input("Enter count: "))

# input()

# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# user.click()

# msg_box = driver.find_element_by_xpath(
#     '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

# for i in range(count):
#     msg_box.send_keys(msg)
#     send_button = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
#     send_button.click()
