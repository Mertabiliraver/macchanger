import psutil
import os
from random import randint
import optparse
from time import sleep

def mac_changer(interface="eth0"):
    print("Started.")
    while True:
        
        for interf in interface:
            sartel1 = 0
            while sartel1 < 7:
                mac = ":".join([('0'+hex(randint(0,256))[2:])[-2:].upper() for _ in range(6)])
                print(f"??? MAC ADRESI DEGISTIRILIYOR:\ninterface-[{interf}] macadress-[{mac}]")
                os.system(f"ifconfig {interf} down")
                data = os.system(f"ifconfig {interf} hw ether {mac}")
                os.system(f"ifconfig {interf} up")
                if data == 0 or data == "0":
                    print("MAC ADRESI DEĞIŞTIRILDI [+]")
                    break
                else:
                    print("Bu mac kabul edilmedi [-] Tekrar deneniyor...\n\n")
                    sartel1 += 1
                    continue
        
        sleep(15)


def get_active_interfaces():
    active_interfaces = []
    all_interfaces = psutil.net_if_stats()
    for interface, stats in all_interfaces.items():
        if stats.isup:
            active_interfaces.append(interface)

    return active_interfaces

active_interfaces_list = get_active_interfaces()


    
mac_changer(active_interfaces_list)
