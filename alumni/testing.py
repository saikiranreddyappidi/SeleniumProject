import requests
import pandas
from random import randint

df = pandas.read_csv('industry-experts.csv')
k = 1
# max_ = len(df['Name'])
max_ = 90
print(max_)
# try:
while k < max_:
    print(k)
    name = df['Name'][k]
    aos = df['aos'][k]
    designation = df['Designation'][k]
    # print(emailStuff)
    # print(type(emailStuff))
    # if k < 50:
    #     k+=1
    #     continue
    doj= df['Date of Joining'][k]
    # phone = df['StudentMobile'][k]
    arr = ["Strongly+Agree", "Agree", "Neutral", "Disagree", "Strongly+Disagree"]

    # q1 = arr[randint(2, 4)]
    # q2 = arr[randint(2, 4)]
    # q3 = arr[randint(2, 4)]
    # q4 = arr[randint(2, 4)]
    # q5 = arr[randint(2, 4)]
    #
    q1 = arr[randint(0, 1)]
    q2 = arr[randint(0, 1)]
    q3 = arr[randint(0, 1)]
    q4 = arr[randint(0, 1)]
    q5 = arr[randint(0, 1)]

    # s=f'https://docs.google.com/forms/d/e/1FAIpQLScPQd3oj8aF-1CfwA8pb4MBRLKIKRgUD8dwCxwifWhBqGacmg/formResponse?entry.1173198640={name}&entry.707164091={reg_num}&entry.307041789={emailHead}%40{emailTail}&entry.466252956={phone}&entry.1151019366={batchStart}+-+{batchEnd}&entry.4787841={q1}&entry.345290997={q2}&entry.1408341271={q3}&entry.1404628021={q4}&entry.121652737={q5}&entry.1151019366_sentinel=&entry.4787841_sentinel=&entry.345290997_sentinel=&entry.1408341271_sentinel=&entry.1404628021_sentinel=&entry.121652737_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%222123858371835553932%22%5D&pageHistory=0&fbzx=2123858371835553932'
    # s=f'https://docs.google.com/forms/d/e/1FAIpQLSd8sQuAKz7HMNU8ltvHq0e92GXWXbtPDF9xuP4Q-lRsEqW5Iw/formResponse?entry.1173198640={name}&entry.707164091={reg_num}&entry.307041789={emailHead}%40{emailTail}&entry.466252956={phone}&entry.1151019366={batchStart}+-+{batchEnd}&entry.4787841={q1}&entry.345290997={q2}&entry.1408341271={q3}&entry.1404628021={q4}&entry.121652737={q5}&entry.1151019366_sentinel=&entry.4787841_sentinel=&entry.345290997_sentinel=&entry.1408341271_sentinel=&entry.1404628021_sentinel=&entry.121652737_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%22-8208370533811364271%22%5D&pageHistory=0&fbzx=-8208370533811364271'
    # s=f'https://docs.google.com/forms/d/e/1FAIpQLSdi3fYrPLjuZ1gTU8zaTtEwRDWryBw5OY22TjvcSq-ggmw0Pg/formResponse?entry.1173198640={name}&entry.707164091={reg_num}&entry.307041789={emailHead}%40{emailTail}&entry.466252956={phone}&entry.1151019366={batchStart}+-+{batchEnd}&entry.4787841={q1}&entry.345290997={q2}&entry.1408341271={q3}&entry.1404628021={q4}&entry.121652737={q5}&entry.1151019366_sentinel=&entry.4787841_sentinel=&entry.345290997_sentinel=&entry.1408341271_sentinel=&entry.1404628021_sentinel=&entry.121652737_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%223153473699181056369%22%5D&pageHistory=0&fbzx=3153473699181056369'
    # s=f'https://docs.google.com/forms/d/e/1FAIpQLSdxXlMp4Hg-h5EWaupG6BIFB8FruZeun4veWDiQCboEE8ORPQ/formResponse?entry.1173198640={name}&entry.707164091={aos}&entry.1151019366={designation}&entry.307041789={doj}&entry.4787841={q1}&entry.345290997={q2}&entry.1408341271={q3}&entry.1404628021={q4}&entry.121652737={q5}&entry.4787841_sentinel=&entry.345290997_sentinel=&entry.1408341271_sentinel=&entry.1404628021_sentinel=&entry.121652737_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%22103031598362694073%22%5D&pageHistory=0&fbzx=103031598362694073'
    # s=f'https://docs.google.com/forms/d/e/1FAIpQLSeZkVTPi6CV-SMG7w-6fFDlg-shi-JQmfXOrc247aauzv3mhw/formResponse?entry.1173198640={name}&entry.707164091={aos}&entry.1151019366={designation}&entry.307041789={doj}&entry.4787841={q1}&entry.1408341271={q2}&entry.345290997={q3}&entry.1404628021={q4}&entry.121652737={q5}&entry.4787841_sentinel=&entry.345290997_sentinel=&entry.1408341271_sentinel=&entry.1404628021_sentinel=&entry.121652737_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%225582963193652173185%22%5D&pageHistory=0&fbzx=5582963193652173185'
    s=f'https://docs.google.com/forms/d/e/1FAIpQLScLheDPxWWLqrlrLmQIoChC8FtkDLTHVJ_2BYRFBOftbul48w/formResponse?entry.1173198640=Amazon&entry.707164091=Cloud+Architect&entry.1918993734=Team+Lead&entry.4787841=Strongly+Agree&entry.345290997=Neutral&entry.1408341271=Neutral&entry.1404628021=Agree&entry.121652737=Disagree&entry.4787841_sentinel=&entry.345290997_sentinel=&entry.1408341271_sentinel=&entry.1404628021_sentinel=&entry.121652737_sentinel=&fvv=1&partialResponse=%5Bnull%2Cnull%2C%22-4990334048506797788%22%5D&pageHistory=0&fbzx=-4990334048506797788'
    r = requests.get(s)
    # print(s)
    print("Name: ", name)
    print("Designation: ",designation)
    print("AOS ", aos)
    print(f"stats code : {r.status_code}")
    print("Q1: ", q1, "Q2: ", q2, "Q3: ", q3, "Q4: ", q4, "Q5: ", q5)
    print("-------------------------------------------------------------")
    k += 1
