import string
import hashlib
import random
import gc
import sys
from itertools import product
import itertools
print("""

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[----]     [----]            ----               ---------- ^      [----]     [----]                         ^
[    ]     [    ]          /      \$         ^               ^    [    ]     [    ]                         ^
[    ]     [    ]         /   --   \*       ^      ------\    ^   [    ]     [    ]                         ^ 
[    ]     [    ]        /   /  \%  \;       \    \       ^ --    [    ]     [    ]                         ^ 
[    -------    ]       /   /    \#  \:      ^     ^---- ^        [    -------    ]                         ^
[               ]      /   /------\&  \^        ^           \%    [               ]                         ^
[    -------    ]     /                \~        ^  -----    ^    [    -------    ]                         ^
[    ]     [    ]    /    ----------    \=               ^    ^   [    ]     [    ]                         ^
[    ]     [    ]   /    /          \!   \-     ----------\    /  [    ]     [    ]                         ^
[    ]     [    ]  /    /            \(   \?   [              ^   [    ]     [    ]                         ^
[----]     [----]  ----/              \----     ----------- ^     [----]     [----]                         ^
        

                     ----------- \$           ^   -----------             ----            [---- \    [-----]
^                  ^              \$         /              /           /      \$         [      \   [     ]
^                ^      ------\    \$       ^     ----------           /   --   \*        [       \  [     ]
^               \     \         ^ --       ^     ^                    /   /  \%  \;       [        \ [     ]
^                ^     ^---- ^            /     /                    /   /    \#  \:      [         \      ]
^                 ^             \%        ^     ^                   /   /------\&  \^     [     \          ]
^                  ^  ------     \%       \     \                  /                \~    [    ] \         ]
^                           ^     ^        ^     ^                /     --------     \=   [    ]  \        ]
^                  ----------\     /        ^      ----------    /     /         \(   \-  [    ]   \       ]
^                 [                ^          \             \%  /     /           \)   \? [    ]    \      ] 
^                  -----------    ^             ^  ----------    ----/             \----  [----]     \ ----]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
@ build 2022 by Mode-Boot                                                     <Stop at scan time (Ctrl + C)>

       """)

class Hash_Scan:

    def __init__(self):

        self.word_date_low = str(string.ascii_lowercase)#abc~

        self.word_date_up = str(string.ascii_uppercase)#ABC~

        self.word_date_dig = str(string.digits)#012~

        self.word_date_pun = str(string.punctuation)#$%&~

        self.point = 0

        self.list_box = []

        self.chars = itertools.cycle(r'/-\|')

    def word_type(self,word_type_text):

        if word_type_text == "low":

            return self.word_date_low

        elif word_type_text == "upp":

            return self.word_date_up

        elif word_type_text == "dig":

            return str(self.word_date_dig)

        elif word_type_text == "pun":

            return str(self.word_date_pun)

        else:

            return ""

    def hash_scan_md5(self,word_type,target_hash):
        
        try:

            while True:

                self.point += 1

                for password_text in product(word_type,repeat=self.point):

                    password = "".join(password_text)

                    hash_date = hashlib.md5(password.encode()).hexdigest()

                    if hash_date == target_hash:

                        print(f"""\n

[$] Password : [  {password}  ] / Target_MD5 : [  {hash_date}  ] [$]                                
                        \n""")

                        sys.exit()

                    else:

                        sys.stdout.write("\r")

                        sys.stdout.write(f"Password... : {password} / MD5 {hash_date} ~ [{next(self.chars)}]")

                        sys.stdout.flush()

                        gc.collect()

        except KeyboardInterrupt:
            
            print("\nThe analysis has been completed, we are looking forward to the next analysis.")

            sys.exit()

    def hash_scan_sha1(self,word_type,target_hash):

        try:

            while True:

                self.point += 1

                for password_text in product(word_type,repeat=self.point):

                    password = "".join(password_text)

                    hash_date = hashlib.sha1(password.encode()).hexdigest()

                    if hash_date == target_hash:

                        print(f"""\n

[$] Password : [  {password}  ] / Target_SHA1 [  {hash_date}  ] [$]
                        \n""")

                        sys.exit()

                    else:

                        sys.stdout.write("\r")

                        sys.stdout.write(f"Password... : {password} / SHA1 {hash_date} ~ [{next(self.chars)}]")

                        sys.stdout.flush()

                        gc.collect()

        except KeyboardInterrupt:
            
            print("\nThe analysis has been completed, we are looking forward to the next analysis.")

            sys.exit()

    def hash_scan_sha224(self,word_type,target_hash):

        try:

            while True:

                self.point += 1

                for password_text in product(word_type,repeat=self.point):

                    password = "".join(password_text)

                    hash_date = hashlib.sha224(password.encode()).hexdigest()

                    if hash_date == target_hash:

                        print(f"""\n

[$] Password : [  {password}  ] / Target_SHA224 : [  {hash_date}  ] [$]
                        \n""")

                        sys.exit()

                    else:

                        sys.stdout.write("\r")

                        sys.stdout.write(f"Password... : {password} / SHA224 : {hash_date} ~ [{next(self.chars)}]")

                        sys.stdout.flush()

                        gc.collect()
                    
        except KeyboardInterrupt:

            print("\nThe analysis has been completed, we are looking forward to the next analysis.")

            sys.exit()
        
    def hash_scan_sha256(self,word_type,target_hash):

        try:

            while True:

                self.point += 1

                for password_text in product(word_type,repeat=self.point):

                    password = "".join(password_text)

                    hash_date = hashlib.sha256(password.encode()).hexdigest()

                    if hash_date == target_hash:

                        print(f"""\n

[$] Password : [  {password}  ] / Target_SHA256 : [  {hash_date}  ] [$]
                        \n""")

                        sys.exit()
                    
                    else:

                        sys.stdout.write("\r")

                        sys.stdout.write(f"Password... : {password} / SHA256 : {hash_date} ~ [{next(self.chars)}]")

                        sys.stdout.flush()

                        gc.collect()

        except KeyboardInterrupt:

            print("\nThe analysis has been completed, we are looking forward to the next analysis.")

            sys.exit()

    def hash_scan_sha512(self,word_type,target_hash):

        try:

            while True:

                self.point += 1

                for password_text in product(word_type,repeat=self.point):

                    password = "".join(password_text)

                    hash_date = hashlib.sha512(password.encode()).hexdigest()

                    if hash_date == target_hash:

                        print(f"""\n

[$] Password : [  {password}  ]  / Target_SHA : [  {hash_date}  ] [$]
                        \n""")

                        sys.exit()

                    else:

                        sys.stdout.write("\r")

                        sys.stdout.write(f"Password... : {password} / SHA512 : {hash_date} ~ [{next(self.chars)}]")

                        sys.stdout.flush()

                        gc.collect()

        except KeyboardInterrupt:

            print("\nThe analysis has been cmpleted, we are looking forward to the next analysis.")

            sys.exit()
    
    def hash_password_build(self,word_type,password_line,hash_type):

        for password_text in range(int(password_line)):

            random_word = random.choice(word_type)

            self.list_box.append(random_word)

        new_password = "".join(self.list_box)

        if hash_type == "md5":

            md5 = hashlib.md5(new_password.encode()).hexdigest()

            return f"NewPassword : {new_password} / MD5 : {md5}"

        elif hash_type == "sha1":

            sha1 = hashlib.sha1(new_password.encode()).hexdigest()

            return f"NewPassword : {new_password} / SHA1 : {sha1}"

        elif hash_type == "sha224":

            sha224 = hashlib.sha224(new_password.encode()).hexdigest()

            return f"NewPassword : {new_password} / SHA224 : {sha224}"

        elif hash_type == "sha256":

            sha256 = hashlib.sha256(new_password.encode()).hexdigest()

            return f"NewPassword : {new_password} / SHA256 : {sha256}"

        elif hash_type == "sha512":

            sha512 = hashlib.sha512(new_password.encode()).hexdigest()

            return f"NewPassword : {new_password} / SHA512 : {sha512}"

    def input_password_build(self,hash_type,password_date):

        if hash_type == "md5":

            md5 = hashlib.md5(password_date.encode()).hexdigest()

            return f"Input_Password : {password_date} / MD5 : {md5}"

        elif hash_type == "sha1":

            sha1 = hashlib.sha1(password_date.encode()).hexdigest()

            return f"Input_Password : {password_date} / SHA1 : {sha1}"

        elif hash_type == "sha224":

            sha224 = hashlib.sha224(password_date.encode()).hexdigest()

            return f"Input_Password : {password_date} / SHA224 : {sha224}"

        elif hash_type == "sha256":

            sha256 = hashlib.sha256(password_date.encode()).hexdigest()

            return f"Input_Password : {password_date} / SHA256 : {sha256}"

        elif hash_type == "sha512":

            sha512 = hashlib.sha512(password_date.encode()).hexdigest()

            return f"Input_Password : {password_date} / SHA512 : {sha512}"

def main():

    hash_scan = Hash_Scan()

    try:

        hash_text = str(input("@ Hash_Scan[hs] or Hash_Build[hb] (hs / hb) : $ "))

        word_type0,word_type1,word_type2,word_type3 = str(input("Password_Word [ low <abc~> / upp <ABC~> / dig <012~> / pun <!#$~> / n <None> ] ([!]Be sure to enter 4!) : $ ")).split()

        word_date = f"{hash_scan.word_type(word_type0)}{hash_scan.word_type(word_type1)}{hash_scan.word_type(word_type2)}{hash_scan.word_type(word_type3)}"

        if hash_text == "hs":

            target_hash = str(input("# Target_Hash Input : $ "))

            if len(target_hash) == 32:

                hash_scan.hash_scan_md5(word_date,target_hash)

            elif len(target_hash) == 40:

                hash_scan.hash_scan_sha1(word_date,target_hash)

            elif len(target_hash) == 56:

                hash_scan.hash_scan_sha224(word_date,target_hash)

            elif len(target_hash) == 64:

                hash_scan.hash_scan_sha256(word_date,target_hash)

            elif len(target_hash) == 128:

                hash_scan.hash_scan_sha512(word_date,target_hash)

            else:

                print("Sorry... No Hash_Scan...")

                sys.exit()

        elif hash_text == "hb":

            password_type = str(input("% Password_Date [ rb <Random_Build> / ip <Input_Password> ] : $ "))

            if password_type == "rb":

                password_line = int(input("# Password_Line Input : $ "))

                hash_type = str(input("& Hash_Type [ md5 / sha1 / sha224 / sha256 / sha512 ] Input : $ "))

                print(f"""\n{hash_scan.hash_password_build(word_date,password_line,hash_type)}\n""")

            elif password_type == "ip":

                password_date = str(input("New_Password Input : $ "))

                hash_type = str(input("& Hash_Type [ md5 / sha1 / sha224 / sha256 / sha512 ] Input : $ "))

                print(f"""\n{hash_scan.input_password_build(hash_type,password_date)}\n""")

    except:

        print("\nStop because of some error or as a signal to end the program.")

        sys.exit()

if __name__ == "__main__":

    main()



