
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

if str(sys.argv[1]) == "en":
	translateFrom = "en"
	translateTo = "fr"
else:
	translateFrom = "fr"
	translateTo = "en"

url = ("https://translate.google.com/?hl=fr#view=home&op=translate&sl=%s&tl=%s" %(translateFrom, translateTo))

driver.get(url)

inputElement = driver.find_element_by_xpath('//*[@id="source"]')

inputElement.send_keys(str(sys.argv[2]))

time.sleep(0.5)

outputElement = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/span')
print(translateFrom + ": " + str(sys.argv[2]))
print(translateTo + ": " + outputElement.text)
