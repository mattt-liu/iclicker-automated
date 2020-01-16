# reef i clicker automater
# Matthew Liu
# 01/14/2020

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://app.reef-education.com/#/login"
browser = webdriver.Chrome("C:\\Users\mattl\Downloads\chromedriver.exe")

## login info: username, then password on new line
file = open("C:/Users/mattl/Documents/Python/automated/login.txt", "r")
u = file.readline().strip() # username
p = file.readline().strip() # password

browser.get(url)

## login page
email_field = browser.find_element_by_id("userEmail")
password_field = browser.find_element_by_id("userPassword")
sign_in_button = browser.find_element_by_id("sign-in-button")

email_field.send_keys(u)
password_field.send_keys(p)
sign_in_button.click()

## class select

print("%-20s %s"%("Geography","1")) # ask user for class
print("%-20s %s"%("Software Design","2"))
class_num = 0;
while (class_num != 1 and class_num != 2):
    try:
        class_num = int(input("What class is this?\n"))
    except:

geo_url = "https://app.reef-education.com/#/courses/78c967fd-4e34-418b-a350-adc65c68fa2c/tab/default"
sse_url = "https://app.reef-education.com/#/courses/80ea7317-8320-4adc-ad7a-e949fb6eeeb6/tab/default"

classes = [geo_url, sse_url]

geo_xy = (43.0090, -81.2750)
sse_xy = (43.0056, -81.2755)

locations = [geo_xy, sse_xy]

browser.get(classes[class_num-1])
