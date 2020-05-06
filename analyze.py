import os
import sys

path = os.path.dirname(os.path.realpath(__file__))

files = []
if len(sys.argv) > 1:
    fonksiyon = [sys.argv[1]]
else:
    fonksiyon = [" system("," exec("," passthru("," shell_exec("," eval("," popen("," pcntl_exec("," create_function(","mysql_execute("]

degisken = ["$_GET","$_POST","$_REQUEST","$_SERVER","$_COOKIE","$_FILES","$_ENV","$_HTTP_COOKIE_VARS","$_HTTP_ENV_VARS","$_HTTP_GET_VARS","$_HTTP_POST_FILES","$_HTTP_POST_VARS","$_HTTP_SERVER_VARS"]


for r, d, f in os.walk(path):
    for file in f:
        if '.php' in file:
            files.append(os.path.join(r, file))
for f in files:
    dosya = open(f,"r")
    if("phpmailer" not in f):
            try:
                for index,content in enumerate(dosya.readlines()):
                    for fun in fonksiyon:
                        if(fun in content):
                            print(f+" Dosyasi "+fun+" fonksiyonu ",index+1," nolu satirda saptandi")
                            for d in degisken:
                                if(d in content):
                                    print(d+" Mevcut")

            except:
                pass