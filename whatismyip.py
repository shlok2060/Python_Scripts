#Simple program to know my public IP address
import json
import urllib3 as ul
#create a PoolManager
ip=ul.PoolManager()
r_ip=ip.request('GET',"http://httpbin.org/ip")
#htpbin.org/ip gives you your public IP address as a json
ip_json=json.loads(r_ip.data.decode('utf-8'))
print(ip_json['origin'])
#the key is called origin
