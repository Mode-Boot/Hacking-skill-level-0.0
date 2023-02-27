import hashlib,itertools,sys,argparse,time

class List_Hash_Scan:

    def __init__(self,target_hash,pass_list):

        self.target_hash = target_hash
        self.pass_list = pass_list
        #As long as it's CUI, this cycle will always come with my code!!
        self.cycle = itertools.cycle(r"/-\|")
        self.time = 0.1

    def list_scan(self):

        try:

            if len(self.target_hash) == 32:

                password_list = open(self.pass_list,"r",encoding="utf-8")

                for password in password_list.readlines():
                    time.sleep(self.time)
                    hash_date = hashlib.md5((password.strip("\n")).encode()).hexdigest()

                    sys.stdout.write("\r")
                    sys.stdout.write(f"Hash_MD5 [{hash_date}] -- {next(self.cycle)}")
                    sys.stdout.flush()

                    if self.target_hash == hash_date:

                        sys.stdout.write(f"\nHash_MD5 [{hash_date}] >>> Password ... {password}\n")
                        sys.exit()

            elif len(self.target_hash) == 40:

                password_line = open(self.pass_list,"r",encoding="utf-8")

                for password in password_line.readlines():
                    time.sleep(self.time)
                    hash_date = hashlib.sha1((password.strip("\n")).encode()).hexdigest()

                    sys.stdout.write("\r")
                    sys.stdout.write(f"Hash_SHA1 [{hash_date}] -- {next(self.cycle)}")
                    sys.stdout.flush()

                    if self.target_hash == hash_date:

                        sys.stdout.write(f"\nHash_SHA1 [{hash_date}] >>> Password ... {password}\n")
                        sys.exit()

            elif len(self.target_hash) == 64:

                password_line = open(self.pass_list,"r",encoding="utf-8")

                for password in password_line.readlines():
                    time.sleep(self.time)
                    hash_date = hashlib.sha224((password.strip("\n")).encode()).hexdigest()

                    sys.stdout.write("\r")
                    sys.stdout.write(f"Hash_SHA224 [{hash_date}] -- {next(self.cycle)}")
                    sys.stdout.flush()

                    if self.target_hash == hash_date:

                        sys.stdout.write(f"\nHash_SHA224 [{hash_date}] >>> Password ... {password}\n")
                        sys.exit()

            elif len(self.target_hash) == 128:

                password_line = open(self.pass_list,"r",encoding="utf-8")

                for password in password_line.readlines():
                    time.sleep(self.time)
                    hash_date = hashlib.sha256((password.strip("\n")).encode()).hexdigest()

                    sys.stdout.write("\r")
                    sys.stdout.write(f"Hash_SHA256 [{hash_date}] -- {next(self.cycle)}")
                    sys.stdout.flush()

                    if self.target_hash == hash_date:

                        sys.stdout.write(f"\nHash_SHA256 [{hash_date}] >>> Password ... {password}\n")
                        sys.exit()

            elif len(self.target_hash) == 256:

                password_line = open(self,pass_list,"r",encoding="utf-8")

                for password in password_line.readlines():
                    time.sleep(self.time)
                    hash_date = hashlib.sha512((password.strip("\n")).encode()).hexdigest()

                    sys.stdout.write("\r")
                    sys.stdout.write(f"Hash_SHA512 [{hash_date}] -- {next(self.cycle)}")
                    sys.stdout.flush()

                    if self.target_hash == hash_date:

                        sys.stdout.write(f"\nHash_SHA512 [{hash_date}] >>> Password ... {password}\n")
                        sys.exit()
            else:

                sys.stdout.write(f"\nHash_Not_Type Finish!!\n")
                sys.exit()

        except KeyboardInterrupt:

            sys.stdout.write("\nList_Hash_Scan_Stop!! and Finish!!\n")
            sys.exit()

def main():

    parser_date = """
    *****************
    <--List_Hash_Scan--->
    *****************
    (Version 0.5)
    """
    arg = argparse.ArgumentParser(description=parser_date)

    arg.add_argument("-th",type=str,help="Target_Hash <md5> <sha1> ....")
    arg.add_argument("-path",type=str,help="Password_List_Path")

    parse = arg.parse_args()

    List_Hash_Scan(parse.th,parse.path).list_scan()

if __name__ == "__main__":

    main()

