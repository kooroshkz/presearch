#There are some changes you should do with your code after installing python on your PC.

import time
import random
#You can edit order repetition from the next line on range(1,x+1)
for z in range(1,33):
    import webbrowser
    url = f'https://engine.presearch.org/search?q=num{random.randint(1,100)}ber+{random.randint(1,100)}'
    webbrowser.register('edge',
    	None,
        #You should find out your chrome.exe location on your computer and paste it down here.
    	webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
    webbrowser.get('edge').open(url)
    #By changing 11 to Your considered time, orderes will take place after X seconds.
    time.sleep(17)
    print (z)

    #If you want to reduce memory usage you can delete the # before each line
    #if z%10 == 0:
        #import os
        #while 1 :
            #os.system("TASKKILL /F /IM msedge.exe")
            #time.sleep(6)
            #break
        

#             ┌────────────── •✧kooroshkz.com✧• ──────────────┐
#                     -Code By : Koorosh Komeilizadeh- 
#             └──────────────── •✧@kooroshkz✧• ───────────────┘
