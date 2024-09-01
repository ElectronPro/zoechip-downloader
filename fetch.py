from mitmproxy import http

import requests as rq
import time
import os , sys , subprocess as sp
import compiler
import getpass
from threading import Thread

catch = ["720/index","1080/index"]

boom = ["watch-movie/"]

blocked_channels = ["123go"]

name = ''

# sys.stdout = open(os.devnull,"w")
# sys.stdin = open(os.devnull,"w")
# sys.stderr = open(os.devnull,"w")

argss = sys.argv


def do(thing,name):

    if "720" in thing:
         p = '720'
    if "1080" in thing:
         p = '1080'

    if os.path.exists(f"/home/{getpass.getuser()}/Videos/movie-files"):
            os.chdir(f"/home/{getpass.getuser()}/Videos/movie-files")
            atmp = f'{name}'
            os.system(f"mkdir {atmp}")
            aff = open(f"{atmp}/index{p}.m3u8","w")
            aff.write(rq.get(thing).content.decode('utf-8'))
            aff.close()
            os.system('killall chromium')
    else:
            os.system(f"mkdir /home/{getpass.getuser()}/Videos/movie-files")
            os.chdir(f"/home/{getpass.getuser()}/Videos/movie-files")
            atmp = f'{name}'
            os.system(f"mkdir {atmp}")
            aff = open(f"{atmp}/index{p}.m3u8","w")
            aff.write(rq.get(thing).content.decode('utf-8'))
            aff.close()
            os.system('killall chromium')

    if "--download" in argss:
         os.chdir(os.path.abspath(atmp))
         if "--progress" in argss:
              Thread(target=compiler.withprogress,args=((f"index{p}.m3u8"),(f"{name}"))).start()
         else:
              Thread(target=compiler.download,args=((f"index{p}.m3u8"),(f"{name}"))).start()
          
         os.system(f"export VLC_VERBOSE=0 && vlc 'index{p}.m3u8' &")

    else:
         os.system(f"export VLC_VERBOSE=0 && vlc '{atmp}/index{p}.m3u8' &")
         sys.exit(0)
    


def request(flow: http.HTTPFlow) -> None:
    if any(x in flow.request.pretty_url for x in boom):
         global name
         fgs = flow.request.pretty_url
         expit = fgs.count("/")
         dfg = fgs.split("/")[expit]
         name = dfg

    if any(keyword in flow.request.pretty_url for keyword in catch):
        do(thing=flow.request.pretty_url,name=name)
        



