import time 
import sys 
import os 
  
def load_animation(): 

    print("You have some limit in the program because the ipapi.co have some security shit and blocked you!")
    print("")
    time.sleep(5)
    load_str = "loading..."
    ls_len = len(load_str) 
  
    animation = "|/-\\"
    anicount = 0
      
    counttime = 0        
      
    i = 0                     
  
    while (counttime != 30): 
          
        time.sleep(0.075)  
                              
        load_str_list = list(load_str)  
          
        x = ord(load_str_list[i]) 
          
        y = 0                             

        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        load_str = res 
       
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
      
    if os.name =="nt": 
        os.system("cls") 
          
    else: 
        os.system("clear") 
  
if __name__ == '__main__':  
    load_animation() 

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 


import time
import sys
import os

WARNING = '\033[93m'
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 


prGreen(" <1> Ip Address Lookup  ")
prGreen(" <2> Exit  ")
print("")
option = input(''' ┌─[ select one ]─[~]
 └──╼ # ''')



while True:
  if option == "1":

      from requests import get
      print("")
      ip = input("Enter Ip Address Here: ")
      print("")
      track = get(f'https://ipapi.co/{ip}/json/')
      print("")
      print(track.json())
      # auto exit
      import sys
      time.sleep(9.5)
      sys.exit()
  if option == '2':

      prRed("Closing....")
      sys.exit()
      
