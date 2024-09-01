#!/bin/python3


import os , time , subprocess as sp , sys , json
from threading import Thread
from mitmproxy.tools import main
import random , getpass

version="Zoechip-Downloader v1 2024 Linux"


if "--version" in sys.argv:
    print(version)
    sys.exit(0)
 

if "--delete" in sys.argv:
    # os.system(f"sleep 5 && sh -c 'sudo rm -rf {sys.executable}' ")
    print(sys.executable)
    exit(0)


# sys.stdout=open(os.devnull,"w")
# sys.stderr=open(os.devnull,"w")
# sys.stdin=open(os.devnull,"w")

er = random.randint(4000,6509)

os.chdir(f"/home/{getpass.getuser()}/Documents/pyprograms/python/zoechip-downloader/final-version/")

def run():
    sp.run(f"chromium --user-data-dir=$PWD/chrome-profile/shikigai --proxy-server='http://127.0.0.1:{er}' www3.zoechip.com &",shell=True,stdin=open(os.devnull,"w"),stderr=open(os.devnull,"w"),stdout=open(os.devnull,"w"))


Thread(target=run,args=(())).start()

if "--download" in sys.argv:
    if "--progress" in sys.argv:
        asf = Thread(target=main.mitmweb,args=((["-s",f"{os.getcwd()}/fetch.py",'-q','--set',f'confdir={os.getcwd()}/cert-file','--set',f"web_port={er+2}",'--no-web-open-browser',"--set","download=1",'--listen-port',f"{str(er)}",'--ssl-insecure',"--set","progress"]),))
    else:
        asf = Thread(target=main.mitmweb,args=((["-s",f"{os.getcwd()}/fetch.py",'-q','--set',f'confdir={os.getcwd()}/cert-file','--set',f"web_port={er+2}",'--no-web-open-browser',"--set","download=1",'--listen-port',f"{str(er)}",'--ssl-insecure']),))


else:
    asf = Thread(target=main.mitmweb,args=((["-s",f"{os.getcwd()}/fetch.py",'-q','--set',f'confdir={os.getcwd()}/cert-file','--set',f"web_port={er+2}",'--no-web-open-browser','--listen-port',f"{str(er)}",'--ssl-insecure']),))



asf.name = 'downloader'
asf.daemon = True
asf.run()

