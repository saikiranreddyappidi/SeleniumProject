import requests
import json

url = "https://ap-south-1.aws.data.mongodb-api.com/app/data-brawp/endpoint/data/v1/action/find"

dbname = 'blog'
collection = 'posts'
apiKey='CH983uyGeCrMHiFsOMuxJwoTPtt0lvn7nN81iRjbzWlPO6r7Hc154dyqhAGZSpFf'
payload = json.dumps({
    "collection": collection,
    "database": dbname,
    "dataSource": "Cluster0",
    "projection": {
        "_id": 0,
    },
    "limit": 10
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': apiKey,
}

response = requests.request("POST", url, headers=headers, data=payload)
for i in response.json():
    print(i, end='')
