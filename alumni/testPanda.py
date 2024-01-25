import requests
import pandas
from random import randint

df = pandas.read_excel('alumin_data.xlsx', '2018-22')
k = 170
# max_ = len(df['Name'])
max_ = 200
print(max_)
# try:
while k < max_:
    print(k)
    name = df['Name'][k]
    reg_num = df['Reg No'][k]
    batchStart = "2018"
    batchEnd = "2022"
    emailStuff = df['email'][k]
    print(emailStuff)
    print(type(emailStuff))
    # if k < 50:
    #     k+=1
    #     continue
    try:
        emailHead = emailStuff.split('@')[0]
        emailTail = emailStuff.split('@')[1]
    except:
        k += 1
        continue
    phone = df['StudentMobile'][k]
    arr = ["Strongly+Agree", "Agree", "Neutral", "Disagree", "Strongly+Disagree"]

    q1 = arr[randint(0, 1)]
    q2 = arr[randint(0, 1)]
    q3 = arr[randint(0, 1)]
    q4 = arr[randint(0, 1)]
    q5 = arr[randint(0, 1)]
    #
    # q1 = arr[randint(3, 4)]
    # q2 = arr[randint(3, 4)]
    # q3 = arr[3]
    # q4 = arr[randint(3, 4)]
    # q5 = arr[randint(3, 4)]
    s=f'https://docs.google.com/forms/d/e/1FAIpQLSeJuM9ssJqFSM26BRCOGlSQJ2d6_CfZU0vYC-chqSqmhBj8rw/formResponse?entry.1173198640={name}&entry.707164091={reg_num}&entry.307041789={emailHead}%40{emailTail}&entry.466252956={phone}&entry.1151019366={batchStart}+-+{batchEnd}&entry.4787841={q1}&entry.345290997={q2}&entry.1408341271={q3}&entry.1404628021={q4}&entry.121652737={q5}&entry.1151019366_sentinel=&entry.4787841_sentinel=&entry.345290997_sentinel=&entry.1408341271_sentinel=&entry.1404628021_sentinel=&entry.121652737_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%226257099696651323519%22%5D&pageHistory=0&fbzx=6257099696651323519'
    r = requests.get(s)
    # print(s)
    print("Name: ", name)
    print("Reg No: ", reg_num)
    print("Batch: ", batchStart, "-", batchEnd)
    print("Email: ", emailHead, "@", emailTail)
    print("Phone: ", phone)
    print(f"stats code : {r.status_code}")
    print("Q1: ", q1, "Q2: ", q2, "Q3: ", q3, "Q4: ", q4, "Q5: ", q5)
    print("-------------------------------------------------------------")
    k += 1
