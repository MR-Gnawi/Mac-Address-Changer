import subprocess
import re
import optparse ## Ta9raa el khyrat
from termcolor import colored

def get_argumants():
    #الخيرات لي اادات
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface" ,dest="network_inte" , help="Specify the network interface")
    parser.add_option("-m","--mac",dest="mac_add" , help="Specify the MAC address")
    options , arguments = parser.parse_args()

    if not options.network_inte:
        parser.error(colored("Your fort to put Mac Address , type -h for help",'red', attrs=['bold']))
    if not options.mac_add:
        parser.error(colored("Your fort to put Mac Address , type -h for help",'red', attrs=['bold']))
    return options

def mac_changer(network_inte , mac_add):    #الاوامر التي سوفة تران على النطام  لي تغير mac address
    subprocess.call(f"ifconfig {network_inte} down", shell=True)
    subprocess.call(f"ifconfig {network_inte} hw ether {mac_add}" ,shell=True)
    subprocess.call(f"ifconfig {network_inte} up" , shell=True)
    print(f"[+] Changing MAC Address for  {network_inte}  To {mac_add}")

#الفلتر لي الحصول على mac address ومقرنته معا المتغير
def get_mac(network_inte , mac_add):
    ifconfig_result = subprocess.check_output(f"ifconfig {network_inte}" , shell=True).decode("UTF-8")
    mac = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac[0] == mac_add:
        print(colored(f"[+] Mac Address has changed successfully {mac_add}",'blue', attrs=['bold']))
    else:
        print(f"Something mert wrong....",'red', attrs=['bold'])

def main():
    op = get_argumants()
    mac_changer(op.network_inte , op.mac_add)
    get_mac(op.network_inte , op.mac_add)

if __name__ == "__main__":
    main() 