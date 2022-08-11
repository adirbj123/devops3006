from selenium import webdriver
my_driver = webdriver.Chrome(executable_path="C:/Users/adirb/Downloads/chromedriver_win32 (1)/chromedriver.exe")
billamt = my_driver.find_element(by="id", value="billamt")
billamt.send_keys("100")