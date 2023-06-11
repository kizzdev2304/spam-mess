import requests
import threading

def check_proxy(proxy):
    proxy_dict = {
        'http': proxy,
        'https': proxy
    }
    try:
        response = requests.get('https://api.myip.com', proxies=proxy_dict, timeout=5)
        if response.status_code == 200:
            print(f"Proxy {proxy} is alive")
        else:
            print(f"Proxy {proxy} is dead")
    except requests.exceptions.RequestException as e:
        print(f"Proxy {proxy} is die")

def process_line(line):
    proxy_items = line.strip().split(":")
    if len(proxy_items) == 4:
        userProxy = proxy_items[2]
        passwordProxy = proxy_items[3]
        ipProxy = proxy_items[0]
        portProxy = proxy_items[1]
        proxyFB = f'http://{userProxy}:{passwordProxy}@{ipProxy}:{portProxy}'
        check_proxy(proxyFB)

with open("proxy.txt", "r") as file:
    proxy_lines = file.readlines()

threads = []
def check():
    for proxy_line in proxy_lines:
        thread = threading.Thread(target=process_line, args=(proxy_line,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
