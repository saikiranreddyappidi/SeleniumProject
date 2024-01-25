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
arr = {}
k = 0
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
        ai_points = driver.find_element(by=By.XPATH,
                                        value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td[4]")
        ai_grade = driver.find_element(by=By.XPATH,
                                       value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td[5]")
        cd = driver.find_element(by=By.XPATH,
                                 value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[3]/td[4]")
        cd_grade = driver.find_element(by=By.XPATH,
                                       value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[3]/td[5]")
        wt = driver.find_element(by=By.XPATH,
                                 value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[4]/td[4]")
        wt_grade = driver.find_element(by=By.XPATH,
                                       value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[4]/td[5]")
        dip = driver.find_element(by=By.XPATH,
                                  value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[5]/td[4]")
        dip_grade = driver.find_element(by=By.XPATH,
                                        value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[5]/td[5]")
        ope = driver.find_element(by=By.XPATH,
                                  value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[6]/td[4]")
        ope_grade = driver.find_element(by=By.XPATH,
                                        value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[6]/td[5]")
        ss = driver.find_element(by=By.XPATH,
                                 value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[7]/td[4]")
        ss_grade = driver.find_element(by=By.XPATH,
                                       value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[7]/td[5]")
        cgpa = (3 * float(ai_points.text) + 4 * float(cd.text) + 4 * float(wt.text) + 4 * float(dip.text) + 3 * float(
            ope.text) + float(ss.text)) / 19
        arr[k] = [ht, name, ai_points.text, ai_grade.text, cd.text, cd_grade.text, wt.text, wt_grade.text, dip.text,
                  dip_grade.text, ope.text, ope_grade.text, ss.text, ss_grade.text, cgpa]
        # print(name, ai_points.text, ai_grade.text, cd.text, cd_grade.text, wt.text, wt_grade.text, dip.text,
        #       dip_grade.text, ope.text, ope_grade.text, ss.text, ss_grade.text)
        print(name, cgpa)
        k += 1
    except Exception as e:
        print("Error", e)
        # time.sleep(10)
driver.quit()
df = DataFrame(arr)
df = df.transpose()
df.to_csv("vucse.csv")
print(df)
