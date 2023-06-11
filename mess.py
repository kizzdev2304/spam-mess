try:
 from re import search as regex
 from time import sleep
 from datetime import datetime
 import requests
 from requests.sessions import Session
 from concurrent.futures import ThreadPoolExecutor
 from threading import Thread,local
 import __fbTools
except ImportError:
 pass
try:
  thread_local = local()
  def getSessionRequests() -> Session:
      if not hasattr(thread_local,'session'):
          thread_local.session = requests.Session()
      return thread_local.session

  def POST(url:str, headers, data,proxies):
      session = getSessionRequests()
      with session.post(url, headers=headers, data=data,proxies=proxies) as response:
          return {
            "contentsWebsite": response.text,
            "statusCode": response.status_code,
            "urlLocate": response.url,
            "timeRequests": response.elapsed.total_seconds()
          }
  def replyRequests(url, headers, data,proxies) -> None:
      with ThreadPoolExecutor(max_workers=10) as executor:
          var = POST(url, headers=headers, data=data,proxies=proxies)
          return var
  class api():
    def sendUser(threadData:str,
                  threadContents:str,
                  threadHeaders:str,
                  UserID:str,
                  setCookies:str,proxyFB=None):
      proxy_with_auth = f'http://{proxyFB}'
      proxies={'http': proxy_with_auth, 'https': proxy_with_auth}
      idUser = setCookies.split("user=")[1].split(";")[0]
      postForm = {}
      postForm["tids"] = "cid.c."+str(idUser)+":"+str(UserID)
      postForm["ids["+str(UserID)+"]"] = str(UserID)
      postForm["body"] = threadContents
      postForm["fb_dtsg"] = threadData["fb_dtsg"]
      postForm["jazoes"] = threadData["jazoest"]
      postForm["__user"] = idUser
      sendingPost = replyRequests("https://m.facebook.com/messages/send/?", headers=threadHeaders, data=postForm,proxies=proxies)
      print(idUser,proxyFB)
except Exception as errLog:
  print(str(errLog))


