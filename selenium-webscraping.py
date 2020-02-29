from selenium import webdriver
from selinum.webdriver.common.by import By
from selenium.webdriver.support.ui import webdriverwait
from selenium.webdriver.support import expected_conditions as EC
fron selenium.common.exceptions import timeoutexception

#create new instance of chrome
browser = webdriver.chrome(executable_path '/library/appliation support/google/chromedriver',

# go to the website
browser.get("http://github/sivas1998/sivasubramanian")
#wait for 20 sec
timeout = 20
try:

webdriverwait(browser,timeout).until(EC.visibility_of_element_located(by.xpath,"//img[@class='siva width-full rounde-2'])))
except timeoutException:
print("timed out waiting for page to load")
browser.quit()

#find element by xpath - return an array of selenium object.
titles_element = browser.find_element by xpath("//a@class='text-bold']")

#lsit comprehension to get the actual repo titles and not the selenium oblect.
titles = [x.text for x in titles_element]
print('titles:')
print(titles, '\n')

#get all of the repo language
language element = browser.find_element_by_xpath("//p[@class='mb-0 f6 text-gray']")
language = [x.text for x in language_element]

#print response in terminal
print("language:")
print(language, '\n')

for title,language in zip(titles, language):
print("reponame : language")
print(title + ":" + language, '\n')
