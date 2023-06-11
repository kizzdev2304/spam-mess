import threading
import loginFB
import mess
import __fbTools
import getmess
import time
import re
import random
code_array = []
code_array1 = []
list_proxy_die = []
list_id_die=[]
idfage1 = 106139704759413
with open("proxy.txt", "r") as file:
    proxy_lines = file.readlines()
with open("additional_data.txt", "r") as file:
    lines = file.readlines()
def process_line(line,proxy_line):
    items = line.strip().split("|")
    proxy_items = proxy_line.strip().split(":")
    if items and len(proxy_items) >= 0:
        user = items[0]
        password = items[1]
        verify = items[2]
        userProxy = proxy_items[2]
        passwordProxy = proxy_items[3]
        ipProxy = proxy_items[0]
        portProxy = proxy_items[1]
        proxyFB = f'{userProxy}:{passwordProxy}@{ipProxy}:{portProxy}'
        
        print(user, "|", password, "|", verify)
        # Get cookie    
        checklog = loginFB.loginFacebook(user, password, verify, proxyFB)
        print(checklog)
        if checklog["statusCode"] == 404:
            die_proxy = f'{ipProxy}:{portProxy}'
            list_proxy_die.append(die_proxy)
            return print(f'status: proxy spam')        
        cookie = checklog["success"]["setCookies"]
        # Send data page
        data = __fbTools.dataTools.dataGetHome(cookie)
        if data["status"] == 404:
            list_id_die.append(user)
            return print(f'status: {user} die')
        headers = __fbTools.Headers(cookie)
        for i in range(2):
            sendNew = mess.api.sendUser(data, "code", headers, idfage1, cookie, proxyFB)
        # Get message
        time.sleep(10)
        getNew1 = getmess.onMessenger.getListMessenger(threadID=idfage1, setCookies=cookie)
        print(getNew1)
        if getNew1["status"] == 'error':
            return print(f'status: {sendNew} die')
        cont1 = getNew1["results"]["contents_text"]
        print(cont1)
        code_pattern = r"CODE : (\w+)" 
        code_pattern1 = r"\b([a-zA-Z0-9]+)\b"
        matches1 = re.findall(code_pattern1, cont1)
        if matches1:
            codeFage = matches1[0]
            code_array1.append(codeFage)
            print(codeFage)
threads = []
for i in range(min(len(proxy_lines), len(lines))):
    line = lines[i]
    proxy_line = random.choice(proxy_lines)
    thread = threading.Thread(target=process_line, args=(line, proxy_line))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()
    
print(code_array)
print(code_array1)
dataCode=code_array+code_array1
for code1 in dataCode:
    print(code1)
    with open("code.txt", "r") as file:
        existing_code = file.read().strip()
        updated_code = existing_code + "\n" + code1
    with open("code.txt", "w") as file:
        file.write(updated_code)
for proxy_diea in list_proxy_die:
    print(proxy_diea)
    with open("list_die_proxy.txt", "r") as file:
        existing_code1 = file.read().strip()
        updated_code1 = existing_code1 + "\n" + proxy_diea
    with open("list_die_proxy.txt", "w") as file:
        file.write(updated_code1)
for idacc in list_id_die:
    print(idacc)
    with open("list_die_acc.txt", "r") as file:
        existing_code1 = file.read().strip()
        updated_code1 = existing_code1 + "\n" + idacc
    with open("list_die_acc.txt", "w") as file:
        file.write(updated_code1)
print(list_id_die)
print(list_proxy_die)
print("Updated code saved to code.txt file.")
print("All tasks completed.")
