import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pandas import DataFrame

path = r"../Drivers/chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(service=Service(path), options=chrome_options)
sub = ["22SA202", "22TP203", "22TP204", "22CS205", "22CS206", "22CS207", "22CS208"]
arr = {"Reg.No": 0, "Name": "", "22SA202": {"points": 0.0, "grade": ""}, "22TP203": {"points": 0.0, "grade": ""},
       "22TP204": {"points": 0.0, "grade": ""}, "22CS205": {"points": 0.0, "grade": ""},
       "22CS206": {"points": 0.0, "grade": ""}, "22CS207": {"points": 0.0, "grade": ""},
       "22CS208": {"points": 0.0, "grade": ""}}
info=[]
p = 0
for i in range(4376, 4700):
    hall = '211FA0' + str(i)
    arr={}
    try:
        driver.get(
            "https://www.vignan.ac.in/vuresultsr22/results.asp?exam=BTECH_R22_2YEAR_2SEM_REG_May_2023&ht={}".format(
                hall))
        # time.sleep(0.5)
        name = driver.find_element(by=By.XPATH,
                                   value="/html/body/table/tbody/tr[2]/td[1]")
        arr["Reg.No"] = name.text.split("\n")[0].split(":")[1].strip()
        arr["Name"] = name.text.split("\n")[1].split(":")[1].strip()
        for j in range(2, 10):
            code = driver.find_element(by=By.XPATH,
                                       value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[{}]/td[1]".format(j))
            subname = driver.find_element(by=By.XPATH,
                                       value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[{}]/td[2]".format(j))
            points = driver.find_element(by=By.XPATH,
                                       value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[{}]/td[4]".format(j))
            letter = driver.find_element(by=By.XPATH,
                                       value="/html/body/table/tbody/tr[3]/td/table/tbody/tr[{}]/td[5]".format(j))
            arr[code.text]={"Sub":subname.text,"Points":points.text,"Grade":letter.text}

    except Exception as e:
        pass
        # print("Error", e)

    print(arr)
    info.append(arr)
    p += 1

driver.quit()
print(arr)
df = DataFrame(info)
# df = df.transpose()
print(df)
df.to_csv("results1.csv")

# /html/body/table/tbody/tr[3]/td/table/tbody/tr[2]/td[4]
# /html/body/table/tbody/tr[2]/td/text()[2]
# /html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td[1]
# /html/body/table/tbody/tr[2]/td/text()[2]
