import threading
import mess
import __fbTools
import getmess
import time
import re
code_array = []
code_array1 = []
idfage1 = 106139704759413
with open("proxy.txt", "r") as file:
    proxy_lines = file.readlines()
with open("cookie.txt", "r") as file:
    cookies = file.readlines()
def process_line(proxy_line, cookie):
    proxy_items = proxy_line.strip().split(":")
    cookie = cookie.strip().split("\n")
    if cookie and len(proxy_items) >= 0:
        userProxy = proxy_items[2]
        passwordProxy = proxy_items[3]
        ipProxy = proxy_items[0]
        portProxy = proxy_items[1]
        proxyFB = f'{userProxy}:{passwordProxy}@{ipProxy}:{portProxy}'
        cookie=cookie[0]
        # Send data page
        data = __fbTools.dataTools.dataGetHome(cookie)
        if data["status"] == 404:
            return print(f'status: die')
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
        code_pattern1 = r"\b([a-zA-Z0-9]+)\b"
        matches1 = re.findall(code_pattern1, cont1)
        if matches1:
            codeFage = matches1[0]
            code_array1.append(codeFage)
            print(codeFage)
threads = []
for i in range(min(len(proxy_lines), len(cookies))):
    proxy_line = proxy_lines[i]
    cookie = cookies[i]
    thread = threading.Thread(target=process_line, args=(proxy_line, cookie))
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
print("Updated code saved to code.txt file.")
print("All tasks completed.")
