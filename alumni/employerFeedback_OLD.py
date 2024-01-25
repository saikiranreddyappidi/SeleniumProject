import requests
import pandas
from random import randint

df = pandas.read_csv('employerFeedbackBatch14.csv')
k = 18
# max_ = len(df['Name'])
max_ = 60
print(max_)
# try:
while k < max_:
    print(k)
    companyName = df['Name of the Company'][k]
    expertName = df['Name of the Expert'][k]
    designation = df['Designation'][k]
    # batchEnd = "2019"
    # emailStuff = df['email'][k]
    # print(emailStuff)
    # print(type(emailStuff))
    # if k < 50:
    #     k+=1
    #     continue
    # try:
    #     emailHead = emailStuff.split('@')[0]
    #     emailTail = emailStuff.split('@')[1]
    # except:
    #     k += 1
    #     continue
    # phone = df['StudentMobile'][k]
    arr = ["Strongly+Agree", "Agree", "Neutral", "Disagree", "Strongly+Disagree"]

    q1 = arr[randint(1, 3)]
    q2 = arr[randint(1, 3)]
    q3 = arr[randint(1, 3)]
    q4 = arr[randint(1, 3)]
    q5 = arr[randint(1, 3)]
    #
    # q1 = arr[randint(3, 4)]
    # q2 = arr[randint(3, 4)]
    # q3 = arr[randint(3, 4)]
    # q4 = arr[randint(3, 4)]
    # q5 = arr[randint(3, 4)]

    s=f"https://docs.google.com/forms/d/e/1FAIpQLScLheDPxWWLqrlrLmQIoChC8FtkDLTHVJ_2BYRFBOftbul48w/formResponse?entry.1173198640={companyName}&entry.707164091={expertName}&entry.1918993734={designation}&entry.4787841={q1}&entry.345290997={q2}&entry.1408341271={q3}&entry.1404628021={q4}&entry.121652737={q5}&entry.4787841_sentinel=&entry.345290997_sentinel=&entry.1408341271_sentinel=&entry.1404628021_sentinel=&entry.121652737_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%22-3450535942102597468%22%5D&pageHistory=0&fbzx=-3450535942102597468"

    r = requests.get(s)
    print("Organization: ", companyName)
    print("Name: ", expertName)
    print("Designation: ", designation)
    # print("Reg No: ", reg_num)
    # print("Batch: ", batchStart, "-", batchEnd)
    # print("Email: ", emailHead, "@", emailTail)
    # print("Phone: ", phone)
    print(f"stats code : {r.status_code}")
    print("-------------------------------------------------------------")
    k += 1
