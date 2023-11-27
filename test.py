import requests

url = 'https://www.eton88.com'
myobj = {'left_fullname': 'Yina', 'employee_passwd': '01242023Etonict9483', 'left_inout': 'in', 'status_type': 'in'
}

x = requests.post(url, json = myobj)

print(x.text)