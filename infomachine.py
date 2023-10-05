import psutil
import platform
import os
from colorama import Fore

print(Fore.RED)

banner = r"""
                            ,-.                               
       ___,---.__          /'|`\          __,---,___          
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.       
  ,'        |           ~'\     /`~           |        `.      
 /      ___//              `. ,'          ,  , \___      \    
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |    
|   /          /\_  `   .    |    ,      _/\          \   |   
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /  
 \  \           | `._   `\\  |  //'   _,' |           /  /      
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'     
     ``       /     \    ,='/ \`=.    /     \       ''          
             |__   /|\_,--.,-.--,--._/|\   __|                  
             /  `./  \\`\ |  |  | /,//' \,'  \                  
            /   /     ||--+--|--+-/-|     \   \                 
           |   |     /'\_\_\ | /_/_/`\     |   |                
            \   \__, \_     `~'     _/ .__/   /            
             `-._,-'   `-._______,-'   `-._,-'
            Infomachine by github.com/pedrostyxx"""

def clearshell():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
clearshell()

def get_system_info():
    print(banner, '\n\n')

    system_info = {}

    # Informações gerais do sistema
    system_info["System"] = {
        "Boot Time": psutil.boot_time(),
        "OS": platform.system(),
        "OS Version": platform.release(),
        "CPU Architecture": platform.architecture(),
    }

    # Informações sobre a CPU
    system_info["CPU"] = {
        "Physical Cores": psutil.cpu_count(logical=False),
        "Logical Cores": psutil.cpu_count(logical=True),
        "CPU Usage (%)": psutil.cpu_percent(interval=1, percpu=True),
    }

    # Informações sobre a memória
    memory = psutil.virtual_memory()
    system_info["Memory"] = {
        "Total Memory (GB)": round(memory.total / (1024 ** 3), 2),
        "Available Memory (GB)": round(memory.available / (1024 ** 3), 2),
        "Used Memory (GB)": round(memory.used / (1024 ** 3), 2),
    }

    # Informações sobre os discos
    disks = psutil.disk_partitions()
    system_info["Disks"] = {}
    for disk in disks:
        disk_usage = psutil.disk_usage(disk.mountpoint)
        system_info["Disks"][disk.device] = {
            "Mount Point": disk.mountpoint,
            "File System Type": disk.fstype,
            "Total Space (GB)": round(disk_usage.total / (1024 ** 3), 2),
            "Used Space (GB)": round(disk_usage.used / (1024 ** 3), 2),
            "Free Space (GB)": round(disk_usage.free / (1024 ** 3), 2),
            "Space Used (%)": disk_usage.percent,
        }

    return system_info

if __name__ == "__main__":
    system_info = get_system_info()

    # Exibir informações
    for category, info in system_info.items():
        print(f"--- {category} ---")
        for key, value in info.items():
            print(f"{key}: {value}")
        print()
