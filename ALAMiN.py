import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
    os.system('git pull')
    import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools")
    print("\n\x1b[1;92m Tool Make By Cyber ALAMiN")
    print(' Join Over Facebook Group For Any Help 😍 ')
    os.system('xdg-open https://www.facebook.com/groups/923481061680273/?ref=share');time.sleep(5)
    from DDOS import menu
    menu()
elif bit == '32bit':
    print("\x1b[1;92m Congratulations ! Your Device Support this Tools")
    print("\n\x1b[1;92m Tool Make By Cyber ALAMiN")
    print(' Join Over Facebook Group For Any Help 😍 ')
    os.system('xdg-open https://www.facebook.com/groups/923481061680273/?ref=share');time.sleep(5)
    from DDOS import menu
    menu()

 
