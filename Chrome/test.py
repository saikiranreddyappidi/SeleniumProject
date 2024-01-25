import numpy as np
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = r"C:\Drivers\ChromeDrivers\chromedriver119.0.6045.161.exe"
url = "https://vignan.ac.in/vuresultsr22/results.asp?exam=BTECH_R22_3YEAR_1SEM_REG_December_2023&ht={}"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(service=Service(path), options=chrome_options)
frame = {}
failed_i = set()
failed_r = set()
# subject={}
for i in range(4001, 4700):
    try:
        ht = '211FA0{}'.format(i)
        driver.get(url.format(ht))
        details = driver.find_element(by=By.XPATH, value="/html/body/table/tbody/tr[2]/td")
        details = list(details.text.split("\n"))
        name = details[1].split(":")[1]
        details = driver.find_element(by=By.XPATH, value="/html/body/table/tbody/tr[3]/td/table/tbody")
        details = list(details.text.split("\n"))
        each = []
        all = []
        cgpa = 0
        t_credits = 0
        fail = {'I', 'R'}
        for i in range(1, len(details)):
            each = details[i].split(" ")
            all.append(' '.join(each[1:-3]))
            all.append(each[-2])
            all.append(each[-1])
            if each[-1] in fail:
                if each[-1] == 'I':
                    failed_i.add(each[0])
                else:
                    failed_r.add(each[0])
            cgpa += float(each[-2]) * float(each[-3])
            t_credits += float(each[-3])
        cgpa = cgpa / t_credits
        frame[ht] = [name, cgpa] + all
        print(ht, name, cgpa)
    except Exception as e:
        print('Error')
        # pass
max_length = max(len(lst) for lst in frame.values())

for key in frame:
    while len(frame[key]) < max_length:
        frame[key].append(np.nan)

print(frame)
driver.quit()
df = DataFrame(frame)
df = df.transpose()
print(df)
df.to_csv("vucse.csv")
print('I', failed_i)
print('R', failed_r)
