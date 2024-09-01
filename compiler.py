#!/bin/python3

def download(load,name):

    import os , json , requests as rq , re , time , subprocess as sp , sys


    links = []

   
    link = load

    if os.path.exists(link):
        if os.path.isfile(link):
            sgd = open(link,"r").readlines()
        else:
            print("File not found :(")

    else:
        rtw = rq.get(link)
        sgd = open("src.txt","w")
        sgd.write(rtw.content)
        sgd = open("src.txt","r").readlines()

    reg = r'\bhttps:\/\/+[^ ]*\b'

    for i in range(len(sgd)):
        if sgd[i].startswith("https"):
            links.append(sgd[i].replace("\n",""))

    # for m in links:
    #     print(m)

    sd = open(f"{name}.mp4","wb")

    os.system(f"notify-send -a 'Zoechip Downloader' 'Started Downloading {name} {os.getcwd()}' -i '/home/electro/Documents/pyprograms/python/zoechip-downloader/chip.png'")

    for i in range(len(links)):
        sd.close()
        sd = open(f"{name}.mp4","ab")
        fall = rq.get(url=links[i])
        sd.write(fall.content)
        sd.close()

    os.system(f"notify-send  -u critical -a 'Zoechip Downloader' 'Done Downloading {name}' -i '/home/electro/Documents/pyprograms/python/zoechip-downloader/chip.png'")
    sys.exit(0)

def withprogress(load,name):

    import os , json , requests as rq , re , time , subprocess as sp , sys


    links = []

    
    link = load

    if os.path.exists(link):
        if os.path.isfile(link):
            sgd = open(link,"r").readlines()
        else:
            print("File not found :(")

    else:
        rtw = rq.get(link)
        sgd = open("src.txt","w")
        sgd.write(rtw.content)
        sgd = open("src.txt","r").readlines()

    reg = r'\bhttps:\/\/+[^ ]*\b'

    for i in range(len(sgd)):
        if sgd[i].startswith("https"):
            links.append(sgd[i].replace("\n",""))

    # for m in links:
    #     print(m)

    sd = open(f"{name}.mp4","wb")
        
    os.system(f"notify-send -a 'Zoechip Downloader' 'Started Downloading {name} {os.getcwd()}' -i '/home/electro/Documents/pyprograms/python/zoechip-downloader/chip.png'")


    for i in range(len(links)):
        sd.close()
        print(f"Part {i} out of {len(links)} Downloaded")
        fall = os.system(f'curl -#  "{links[i]}" >> {name}.mp4')
        os.system("clear")

    os.system(f"notify-send  -u critical -a 'Zoechip Downloader' 'Done Downloading {name}' -i '/home/electro/Documents/pyprograms/python/zoechip-downloader/chip.png'")
    sys.exit(0)
        