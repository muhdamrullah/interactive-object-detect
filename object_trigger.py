import pygame.camera
import pygame.image
import subprocess
import os
import time
import random

qty3 = 6
qty4 = 50
qty5 = 50
qty6 = 50
qty7 = 20

def take_photo():
    pygame.camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    img = cam.get_image()
    pygame.image.save(img, "photo.png")
    pygame.camera.quit()

def load_recognizer():
    recognizer = subprocess.check_output('"C:\\Program Files\\Find-Object\\bin\\Find-Object.exe" --console --object "C:\\Users\\AW Alpha\\Python\\object-dir\\object_20.png" --Camera/6useTcpCamera "true" --Camera/8port 5000 --General/port 6000', shell=True)
    print recognizer

def compare_photo():
    output = subprocess.check_output('''"C:\\Program Files\\Find-Object\\bin\\find_object-tcpRequest.exe" --json "out.json" --scene photo.png --out 5000 --in 6000''', shell=True)
    print output
    
def file_len(fname):
    with open(fname) as f:
        for i,l in enumerate(f):
            pass
        return i+1

def read_json():
    randomNo = random.randint(1,20)
    print randomNo
    readvar = file_len("out.json")
    if not readvar == 1 and (randomNo == 1 or randomNo == 2 or randomNo == 3 or randomNo == 4 or randomNo == 5 or randomNo == 6 or randomNo == 7):
	
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: none;\n'
    	    data[28] = '    display: block;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )
    	    time.sleep(10)                
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: block;\n'
    	    data[28] = '    display: none;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )

    if not readvar == 1 and (randomNo == 8):
        global qty3
        qty3 = qty3 - 1	
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: none;\n'
    	    data[43] = '    display: block;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )
                
    	    time.sleep(10)                
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: block;\n'
    	    data[43] = '    display: none;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )
 	
    if not readvar == 1 and not qty3 < 1 and (randomNo == 9 or randomNo == 10 or randomNo == 11):
        global qty4
        qty4 = qty4 - 1
	
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: none;\n'
    	    data[58] = '    display: block;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )
                
    	    time.sleep(10)                
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: block;\n'
    	    data[58] = '    display: none;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )

    if not readvar == 1 and not qty4 < 1 and (randomNo == 12 or randomNo == 13 or randomNo == 14):
        global qty5
        qty5 = qty5 - 1
	
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: none;\n'
    	    data[73] = '    display: block;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )
                
    	    time.sleep(10)                
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: block;\n'
    	    data[73] = '    display: none;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )
   
    if not readvar == 1 and not qty5 < 1 and (randomNo == 15 or randomNo == 16 or randomNo == 17):
        global qty6
        qty6 = qty6 - 1
	
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: none;\n'
    	    data[88] = '    display: block;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )
    	    time.sleep(10)                
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: block;\n'
    	    data[88] = '    display: none;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )

    if not readvar == 1 and not qty6 < 1 and (randomNo == 18 or randomNo == 19 or randomNo == 20):
        global qty7
        qty7 = qty7 - 1
	
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: none;\n'
    	    data[103] = '    display: block;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )
                
    	    time.sleep(10)                
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: block;\n'
    	    data[103] = '    display: none;\n'
    	    
    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )
       
    else:
	pass

#This is the main code
#load_recognizer()
while True:
  try:
    #take_photo()
    compare_photo()
    read_json()
    time.sleep(1)
  except (TypeError, subprocess.CalledProcessError) as e :
    pass
