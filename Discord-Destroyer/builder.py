import os
import sys
from colorama import init, Fore

init(autoreset=True)
user_home = os.path.expanduser("~")
pyinstaller_path = os.path.join(user_home, "AppData", "Local", "Programs", "Python", "Python311", "Scripts", "pyinstaller.exe")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    clear_screen()
    header = f"""{Fore.RED}
·▄▄▄▄  ▪  .▄▄ ·  ▄▄·       ▄▄▄  ·▄▄▄▄          ·▄▄▄▄  ▄▄▄ ..▄▄ · ▄▄▄▄▄▄▄▄         ▄· ▄▌▄▄▄ .▄▄▄  
██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▀▄ █·██▪ ██         ██▪ ██ ▀▄.▀·▐█ ▀. •██  ▀▄ █·▪     ▐█▪██▌▀▄.▀·▀▄ █·
▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌        ▐█· ▐█▌▐▀▀▪▄▄▀▀▀█▄ ▐█.▪▐▀▀▄  ▄█▀▄ ▐█▌▐█▪▐▀▀▪▄▐▀▀▄ 
██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌▐█•█▌██. ██         ██. ██ ▐█▄▄▌▐█▄▪▐█ ▐█▌·▐█•█▌▐█▌.▐▌ ▐█▀·.▐█▄▄▌▐█•█▌
▀▀▀▀▀• ▀▀▀ ▀▀▀.▀▀▀ ▀▀▀▀▀•  ▀▀▀ .▀  ▀▀▀▀▀▀•         ▀▀▀▀▀•  ▀▀▀  ▀▀▀▀  ▀▀▀ .▀  ▀ ▀█▄▀▪  ▀ •  ▀▀▀ .▀  ▀
▄▄▄▄· ▄• ▄▌▪  ▄▄▌  ·▄▄▄▄  ▄▄▄ .▄▄▄                                                               
▐█ ▀█▪█▪██▌██ ██•  ██▪ ██ ▀▄.▀·▀▄ █·                                                             
▐█▀▀█▄█▌▐█▌▐█·██▪  ▐█· ▐█▌▐▀▀▪▄▐▀▀▄                                                              
██▄▪▐█▐█▄█▌▐█▌▐█▌▐▌██. ██ ▐█▄▄▌▐█•█▌                                                             
·▀▀▀▀  ▀▀▀ ▀▀▀.▀▀▀ ▀▀▀▀▀•  ▀▀▀ .▀  ▀{Fore.RESET}
"""
    print(header)

def press_enter_to_continue():
    input(f"{Fore.GREEN}Press Enter to Continue...{Fore.RESET}")

def obfuscator():
    clear_screen()
    obf_file = "src/main.py"
    output_name = input(f"{Fore.YELLOW}What do you want the name of the output file to be (don't use a space in the name, use '-' instead): {Fore.RESET}")

    current_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.system(f'python src/OBF.py {obf_file} -o {output_name}.py')
    os.chdir(current_dir)

def py2exe():
    clear_screen()
    output_exe_name = input(f"{Fore.YELLOW}Enter the name of the output EXE file (don't use a space in the name, use '-' instead): {Fore.RESET}")
    file_name = output_exe_name
    add_icon = input(f"{Fore.YELLOW}Do you want to add an icon to the outputted file (y/n): {Fore.RESET}")
    clear_screen()

    current_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if add_icon == 'y':
        icon_file = input(f"{Fore.YELLOW}Drag the icon file onto the console and press enter: {Fore.RESET}")
        os.system(f'{pyinstaller_path} --onefile {file_name}.py --clean --noconsole -i "{icon_file}" -n {output_exe_name}')
    elif add_icon == 'n':
        os.system(f'{pyinstaller_path} --onefile {file_name}.py --noconsole --clean -n {output_exe_name}')
    else:
        print(f"{Fore.RED}Invalid input.{Fore.RESET}")

    os.chdir(current_dir)
    print(f"{Fore.GREEN}Done !{Fore.RESET}")
    os.system("start dist")

def main():
    display_header()
    press_enter_to_continue()
    obfuscator()
    py2exe()
    press_enter_to_continue()

if __name__ == "__main__":
    main()
