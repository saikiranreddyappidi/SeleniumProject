import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pandas import DataFrame
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r"C:\Drivers\ChromeDrivers\chromedriver119.0.6045.161.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(service=Service(path), options=chrome_options)
frame = {}
for i in range(4001, 4700):
    try:
        ht = '211FA0{}'.format(i)
        driver.get(
            "https://vignan.ac.in/vuresultsr22/results.asp?exam=BTECH_R22_3YEAR_1SEM_REG_December_2023&ht={}".format(
                ht))
        # time.sleep(5)
        # driver.implicitly_wait(10)
        # wait = WebDriverWait(driver, 10)  # wait for up to 10 seconds
        # details = wait.until(
        #     EC.presence_of_element_located((By.XPATH, "/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]")))
        details = driver.find_element(by=By.XPATH, value="/html/body/table/tbody/tr[2]/td")
        details = list(details.text.split("\n"))
        name = details[1].split(":")[1]
        details = driver.find_element(by=By.XPATH, value="/html/body/table/tbody/tr[3]/td/table/tbody")
        details = list(details.text.split("\n"))
        dis = {}
        each = []

        cgpa = 0
        t_credits = 0
        for i in range(1, len(details)):
            each = details[i].split(" ")
            dis[each[0]] = {"SubjectName": ' '.join(each[1:-3]), "Credits": each[-3], "Points": each[-2],
                            "Grade": each[-1]}
            cgpa += float(each[-2]) * float(each[-3])
            t_credits += float(each[-3])
        cgpa = cgpa / t_credits
        print(name, cgpa)
        frame[ht] = [name, cgpa, dis]
    except Exception as e:
        print(e)

driver.quit()
df = DataFrame(frame)
df = df.transpose()
print(df)
df.to_csv("vucse.csv")

