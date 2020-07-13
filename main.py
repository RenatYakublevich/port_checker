import socket
from colored import fg, bg, attr
import os
import time
import logging
import sys
#scanner.io version alpha 0.1 by Renat Yakublevich aka helloworldbastard



sock = socket.socket()

popular_port = [8080,80,443,3128,53,21,20,587,995,993,3306]

localhost_port = [1,5,7,9,11,13,17,18,19,20,21,22,23,25,37,8080,80,443,3128,53,42,63,67,101,95,102,119,123,113,995,994,993]

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def main():
    try:
        print('-' * 50)
        menu = input('Hello, it`s scanner.io\n\n1 - scan port\n2 - scan all popular port\n3 - scan all localhost port\n\nFor quit write command exit ')
        print('-' * 50)
        if menu == '1':
            scan_definite_port()
        elif menu == '2':
            scan_all_popular_port()
        elif menu == '3':
            scan_localhost_port()
        elif menu == 'exit':
            print('Bye!')
            time.sleep(0.8)
            sys.exit()
        else:
            raise Exception
            
    except Exception as e:
        print('There is no such menu number or something went wrong, restarting the program ...')
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear') #clean console feed
        main()

def scan_definite_port():
    try:
        print('For default request use command default')
        host_url = input('Write host url --> ')
        if host_url == 'default':
            host_url = 'google.com'
            port = 80
        else:
            port = input('Write port --> ')
        sock.settimeout(1)
        sock.connect((host_url,int(port)))
        color = fg('white')
        print(f'Host - {host_url}\nPort - {port} OPEN PORT')
    except socket.error:
        print(f'Host - {host_url}\nPort - {port} CLOSE PORT')
    except Exception as e:
        print('woops')
        logging.error("Exception occurred", exc_info=True)
        main()
    finally:
        time.sleep(1)
        main()

def scan_all_popular_port():
    '''Scan all popular ports for url'''
    try:
        host_url = input('Write host url --> ')
        print(f'Port for this url - {host_url}\n')
        for all_port in popular_port:
            try:
                scan = socket.socket()
                scan.settimeout(0.5)
                scan.connect((host_url, all_port))
            except socket.error:
                print(f'PORT {all_port} CLOSE')
            else:
                print(f'PORT {all_port} OPEN')
    except Exception as e:
        print('oops..')
    finally:
        time.sleep(1)
        main()

def scan_localhost_port():
    '''Scan all popular local host ports'''
    try:
        print('Port for localhost:')
        for all_port in localhost_port:
            try:
                scan = socket.socket()
                scan.settimeout(0.5)
                scan.connect(('localhost', all_port))
            except socket.error:
                print(f'PORT {all_port} CLOSE')
            else:
                print(f'PORT {all_port} OPEN')
    except Exception as e:
        print('oops..')
    finally:
        time.sleep(1)
        main()


main()

    