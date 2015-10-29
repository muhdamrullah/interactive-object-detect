import pygame.camera
import pygame.image
import subprocess
import os
import time
from SimpleCV import Image, Camera

def take_photo():
    pygame.camera.init()
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    img = cam.get_image()
    pygame.image.save(img, "photo.bmp")
    pygame.camera.quit()

def load_recognizer():
    subprocess.call("Find-Object.exe --console --object box.png --Camera/6useTcpCamera 'true' --Camera/8port 5000 --General/port 6000", shell=True)

def compare_photo():
    subprocess.call("find_object-tcpRequest.exe --json 'out.json' --scene photo.bmp --out 5000 --in 6000", shell=True)

def read_json():
    if os.path.isfile("out.json") == True:
	
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[14] = '    display: none;\n'

    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )
	    subprocess.call("DEL /F /S /Q /A out.json", shell=True)
    	    time.sleep(2)
    else:
	pass

#This is the main code
load_recognizer()
while True:
    take_photo()
    compare_photo()
    read_json()
