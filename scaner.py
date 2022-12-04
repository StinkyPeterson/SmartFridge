import requests
import json
def scan():
    url = 'https://proverkacheka.com/api/v1/check/get'
    token = '17639.WgFbE0Usn2HhAGg8e'
    t = "t=20220817t1644&s=431.94&fn=9960440302452937 &i=88432&fp=1230248284 &n=1"
    data = {
        'token': token,
        'qrraw': t
    }
    r = requests.post(url, data=data)
    with open("data.txt", "w") as file:
        file.write(r.text)
#scan()
def open_json():
    with open('data.json') as file:
        data = json.load(file)
    print(data['data']['json']['items'])
    products =data['data']['json']['items']
    for product in products:
        print(product['name'], product['sum']/100, product['quantity'])

dict = {}
with open('data.txt') as file:
    data = file.read()
dict = json.loads(data)
print(dict)



