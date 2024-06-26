#!/usr/bin/python3
# Code by Han

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import argparse
import sys
import time
from datetime import datetime
from colorama import init, Fore, Style
from slowprint.slowprint import *


global starttime

class ZeroScann():

    def __init__(self):
        self.scan()

    def scan(self):
        # argument parser like shit
        parser = argparse.ArgumentParser(prog="R1Px0x8.py, description="Simple Find Shell in Website")
        parser.add_argument("-u", dest="domain", help="your url")
        parser.add_argument("-w", dest="wordlist", help="your wordlsit")
        args = parser.parse_args()
        if not args.domain:
            sys.exit(f"{Fore.BLUE}Usage: {Fore.YELLOW}shellfinder.py{Fore.BLUE} -u{Fore.RED} example.com{Fore.BLUE} -w wordlist.txt")
        if not args.wordlist:
            sys.exit(f"{Fore.BLUE}Usage: {Fore.YELLOW}shellfinder.py{Fore.BLUE} -u{Fore.RED} example.com{Fore.BLUE} -w wordlist.txt")

        # handle url website format
        site = args.domain
        slowprint(Fore.RESET+"["+Fore.BLUE+"INFO"+Fore.RESET+"] Start Crawling...",0.3)
        slowprint(Fore.RESET+"["+Fore.BLUE+"INFO"+Fore.RESET+"] Wait a sec!\n",0.3)
        time.sleep(3)
        if not site.startswith("http://"):
            site = "http://"+site
        if not site.endswith("/"):
            site = site+"/"
        # load wordlist
        try:
            pathlist = args.wordlist
            wlist = open(pathlist, "r")
            wordlist = wlist.readlines()
        except FileNotFound as e:
            print("\033[91mUpss, Wordlist Not Found!\033[0m")
            exit()
        finally:
            try:
                wlist.close()
            except:
                print("\033[91mWordlist Can\'t Close!\033[0m")
        # user-agent
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        #list to hold the results we find
        found = []
        # respon code
        resp_codes = {403 : "Forbidden", 401 : "Unauthorized", 500 : "Initial Status Code"}
        # loop with join pathlist
        starttime = time.time()
        for psx in wordlist:
            try:
                psx = psx.replace("\n", "")
                url = site+psx
                req = Request(url, headers={"User-Agent": user_agent})
                time.sleep(0.1)
                try:
                    connection = urlopen(req)
                    print("["+"Fore.CYAN"+{0}+"{Fore.RESET}]".format(time.strftime("%H:%M:%S")),"{Fore.GREEN}Found:","\033[0m/"+psx)
                    found.append(url)

                except HTTPError as e:
                    if e.code == 404:
                        print(Fore.RESET+"[{0}{1}{2}] \033[91merror:\033[0m /{3}".format(Fore.CYAN, datetime.now().strftime("%H:%M:%S"), Fore.RESET, psx))
                    else:
                        print(Fore.RESET+"[{0}{1}{2}] {3}Info : \033[33m/{4}{5} status: {6}{7}".format(Fore.CYAN, datetime.now().strftime("%H:%M:%S"), Fore.RESET, Fore.GREEN, psx, Fore.RESET, Fore.GREEN, e.code, Fore.YELLOW, resp_codes[e.code], Fore.RESET))

                except URLError as e:
                    sys.exit("\033[31m[!] Upss, No Internet Connection")
                except Exception as er:
                    print("\n\033[93m[?] \033[0mYour Connection Is Bad")
                    print("\033[93m[!] \033[0mExit Program")
                    time.sleep(3)
                    exit()
            except KeyboardInterrupt as e:
                print("\n\033[96m[?] \033[0mCTRL+C Detected")
                print("\033[96m[!] \033[0mExit Program")
                time.sleep(2)
                exit()

        if found:
            print("\n\033[96m[+] \033[0mResult Found\033[92m")
            print("\n".join(found))
            print("\n\033[96m[?] \033[0mTime Elasped: \033[35m%.2f\033[0m Seconds" % float(time.time()-starttime))
        else:
            print("\n\033[96m[!] \033[0mCould Not Find Any Shell Backdoor")
            print("\033[96m[?] \033[0mTime Elasped: \033[33m%.2f\033[0m Seconds" % float(time.time()-starttime))

    def banner():
        # just the screen display like this
        info = f""" 
        
         LOADING amonuserland
▇▇▇▇▇▇▇▇▇▇▇▇▇▇▢
╭━╮╭━╮╭╮　 ╱
╰━┫╰━┫╰╯ ╱╭╮
╰━╯╰━╯　╱  ╰╯
COMPLETE 

t.me/R1Px0x8
t.me/xuserwww
         
         """
        return info
    print(banner())

if __name__ == '__main__':
    ZeroScann()