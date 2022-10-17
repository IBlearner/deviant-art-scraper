from time import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from excelLogic import *
import openpyxl

DRIVER_PATH = 'C:/Users/kienv/Downloads/chromedriver_win32/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

artist = "pryce14"
# artist = "ghost-malone"
url = f"https://www.deviantart.com/{artist}/gallery/all"

# driver.get(url)

# # Scan page for "next" button
# nextButton = ""
# potentialNextButtons = driver.find_elements(By.CLASS_NAME, "_1qdQj")
# for x in range(len(potentialNextButtons)):
#     if potentialNextButtons[x].text == "Next":
#         print(potentialNextButtons[x].text)
#         nextButton = potentialNextButtons[x]

# # Process the page with bs4
# page_source = driver.page_source
# soup = BeautifulSoup(page_source,"html.parser")

# # Scan page for images and keep an array off the links
# foundImgArr = []
# for elem in soup.find_all("a", {"data-hook": "deviation_link"}):
#     if elem["href"] != None:
#         foundImgArr.append(elem["href"])

# # Proceeding to next page if required
# time.sleep(2)
# nextButton.click()

# df = pd.DataFrame(foundImgArr, columns=["main-links"])
# print(df)
# df.to_excel(pathToExcel, sheet_name=f"user1")

excelData = readFromExcel()
response = requests.get(excelData[0])
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.find_all("div", {"class": "_1X6bR"}))

time.sleep(1200)