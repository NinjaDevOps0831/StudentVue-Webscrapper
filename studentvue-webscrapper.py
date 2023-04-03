from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import time

def delete_last_element(string1) :
	return string1[:-1]

startTime = time.time()

classNum = 0
classNames = []
classOverallGrades = []
courseTitles = []

#  Hide Pop-Up Window

WINDOW_SIZE = "1920,1080"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)


#  Login

id_password_file = open("id_password.txt", "r")
id_num = delete_last_element(str(id_password_file.readline()))
password_num = delete_last_element(str(id_password_file.readline()))
id_password_file.close()

browser = webdriver.Chrome(options=chrome_options)
browser.get("https://parentvue.cusdk8.org/PXP2_Login_Student.aspx?regenerateSessionId=True")
id_search_box = browser.find_element("id", "ctl00_MainContent_username")
password_search_box = browser.find_element("id", "ctl00_MainContent_password")
login_click = browser.find_element("id", "ctl00_MainContent_Submit1")
id_search_box.send_keys(id_num)
password_search_box.send_keys(password_num)
login_click.click()


#  Gradebook Data

browser.get("https://parentvue.cusdk8.org/PXP2_Gradebook.aspx?AGU=0&studentGU=E2D240A7-37CF-4998-9B44-162637F00C62")
gradeBookSoup = BeautifulSoup(browser.page_source, "lxml")

templist = gradeBookSoup.find_all("button", attrs={"class":"btn btn-link course-title"})
classNum = len(templist)
for i in range(classNum) :
	courseTitles.append(templist[i].get_text())

templist = []
templist = gradeBookSoup.find_all("span", attrs={"class":"score"})
for i in range(classNum) :
	classOverallGrades.append(templist[i].get_text())

for i in range(classNum) :
	print(courseTitles[i], ":", classOverallGrades[i], "percent")
browser.close()

endTime = time.time()

print("\n")
print("Time Elapsed :", endTime-startTime, "seconds")





