import os
import sys

args = sys.argv
args.pop(0)

if len(args) == 0:
    args.append(None)

if args[0] in ["--version","-v"]:
    print("Ghost Package Manager for pacman and yay")
    print("Version: Dev 3")

elif args[0] in ["install","-S","-i"]:
    args.pop(0)
    os.system(f"sudo pacman -S {' '.join(args)}")
    
elif args[0] in ["upgrade","update","-u"]:
    args.pop(0)
    if args[0] == "ghost":
        os.system("rm -rf /tmp/ghostinstall")
        os.system("git clone https://github.com/MarcosLp69/ghost.git /tmp/ghostinstall")
        os.system("chmod +x /tmp/ghostinstall/install.sh")
        os.system("clear")
        os.system("/tmp/ghostinstall/install.sh")
    else:
        os.system(f"sudo pacman -Syu {' '.join(args)}")

elif args[0] in ["aur","-a","-aur"]:
    args.pop(0)
    os.system(f"yay -S {' '.join(args)}")

elif args[0] in ["remove","-R","--remove"]:
    args.pop(0)
    os.system(f"sudo pacman -R {' '.join(args)}")

else:
    print("Invalid Command")
