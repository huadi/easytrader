

from easytrader import remoteclient
user= remoteclient.use('ths', '127.0.0.1')
user.prepare()
print(user.balance)