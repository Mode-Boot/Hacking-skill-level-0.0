import requests,pathlib
from bs4 import BeautifulSoup

class Request:

    def __init__(self):
        self.proxy_url,self.ua_url,self.referer_url = "https://free-proxy-list.net/","https://www.useragentstring.com/pages/All/","https://www.cyberghostvpn.com/en_US/privacyhub/what-are-onion-sites/"
        self.proxy_ua_referer_path = "Proxy_UA_Referer"
        pathlib.Path(self.proxy_ua_referer_path).mkdir(exist_ok=True)
        self.proxy_file,self.ua_file,self.referer_file= "proxy.txt","ua.txt","referer.txt"

    def proxy_list_build(self):
        res = requests.get(self.proxy_url,timeout=10)
        soup = BeautifulSoup(res.text,"html.parser")
        with open(f"{self.proxy_ua_referer_path}/{self.proxy_file}","w+",encoding="utf-8")as proxy_file:
            proxy_file.write(soup.textarea.text)

        return f"{self.proxy_ua_referer_path}/{self.proxy_file}"

    def ua_list_build(self):
        res = requests.get(self.ua_url,timeout=10)
        soup = BeautifulSoup(res.text,"html.parser")
        with open(f"{self.proxy_ua_referer_path}/{self.ua_file}","w+",encoding="utf-8")as ua_file:
            for soup_tag in soup.find_all("li"):
                ua_file.write((soup_tag.text) + "\n")

        return f"{self.proxy_ua_referer_path}/{self.ua_file}"

    def referer_list_build(self):
        res = requests.get(self.referer_url,timeout=10)
        soup = BeautifulSoup(res.text,"html.parser")
        with open(f"{self.proxy_ua_referer_path}/{self.referer_file}","w+",encoding="utf-8")as referer_file:
            for soup_tag in soup.find_all("em"):
                referer_file.write((soup_tag.text) + "\n")

        return f"{self.proxy_ua_referer_path}/{self.referer_file}"

    def main(self):
        request = Request()
        request.proxy_list_build()
        request.ua_list_build()
        request.referer_list_build()

if __name__ == "__main__":
    
    Request().main()
