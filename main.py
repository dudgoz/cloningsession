from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options



#1.a
# driver = webdriver.Chrome(executable_path="C:\\Users\\davidgoz\\Downloads\\chromedriver.exe")
# driver.get("http://www.ynet.co.il")
# #1.b
# driver1 = webdriver.Edge(executable_path= "C:\\Users\\davidgoz\\Downloads\\msedgedriver.exe")
# driver1.get("https://www.ynet.co.il")
# #2.a
# title = driver.title
# driver.refresh()
# if title == driver.name:
#     print("Equal")
#3. The answer is yes, the elemnts are the same for each browser.


#4.a,b:
# GT = webdriver.Chrome(executable_path="C:\\Users\\davidgoz\\Downloads\\chromedriver.exe")
# GT.get("https://translate.google.com/?sl=iw&tl=en&op=translate")
# GT.find_element(By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys("שלום לכם")
# GT.find_element(By.ID, "gt-submit").click()

#5a,b:
# youtubedriver = webdriver.Chrome(executable_path="C:\\Users\\davidgoz\\Downloads\\chromedriver.exe")
# youtubedriver.get("https://www.youtube.com")
# youtubedriver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("the shape of you")
# youtubedriver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon").click()

#6a:
#
# my_driver = webdriver.Chrome(executable_path="C:\\Users\\davidgoz\\Downloads\\chromedriver.exe")
# my_driver.get("https://translate.google.com")
# my_driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys("שלום לכם")
# #first = my_driver.find_element(By.ID, "gt-submit").click()
# #second = my_driver.find_element(By.NAME, "jfk-button")
# third = my_driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
# print(third)

# 7a:
# fb_driver = webdriver.Chrome(executable_path="C:\\Users\\davidgoz\\Downloads\\chromedriver.exe")
# fb_driver.get('https://www.facebook.com')
# fb_driver.find_element(By.ID, 'email').send_keys("dudigoz@gmail.com")
# fb_driver.find_element(By.ID,'pass').send_keys('Cyberisf0n!')
# fb_driver.find_element(By.NAME,'login').click()


# 8a,b:
# fb_driver = webdriver.Chrome(executable_path="C:\\Users\\davidgoz\\Downloads\\chromedriver.exe")
# fb_driver.get('https://www.facebook.com')
# fb_driver.delete_all_cookies()
# print(fb_driver.get_cookies())


# 9a,b:
# git_webdriver = webdriver.Chrome(executable_path="C:\\Users\\davidgoz\\Downloads\\chromedriver.exe")
# git_webdriver.get("https://github.com")
# git_webdriver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/button').click()
# git_webdriver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]').send_keys("Selenium")
# git_webdriver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]').send_keys(Keys.RETURN)


# 10a,b,c:
# # ext = webdriver.Edge(executable_path= "C:\\Users\\davidgoz\\Downloads\\msedgedriver.exe")
# ext = webdriver.Chrome(executable_path= "C:\\Users\\davidgoz\\Downloads\\chromedriver.exe")
# ext.get("https://google.com")
# # chrome_options = Options()
# # chrome_options.add_argument('--disable-extensions')


ext = webdriver.Chrome(executable_path= "C:\\Users\\davidgoz\\Downloads\\chromedriver.exe")
ext.get("https://google.com")
trying = ext.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[1]/a').text
if trying == 'Gmail':
    print('Great Success')
else:
    print('Not gmail')