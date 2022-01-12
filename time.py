#libraries
import time 
from datetime import datetime as dt

#windows host file
hosts_paths=r"C:\Windows\Systems32\drivers\etc\hosts"
redirect="127.0.0.1"

#websites in blocklist
websites=["www.yahoo.com","yahoo.com","www.bing.com","bing.com"]

#start whoile loop
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
        print("sorry not allowed")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect+""+site+"\n")
    else:
        with open(host_path,'r') as file:
            content-file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
            
                    

        
  
  
