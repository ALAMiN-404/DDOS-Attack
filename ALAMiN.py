import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support Tolls\033[1;37m")
    os.system('xdg-open https://facebook.com/groups/1017905562448002/')
if __name__ == "__main__":
	try:
		__import__("DDOS").login()
	except Exception as e:
		exit(str(e))
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
