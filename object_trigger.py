import pygame.camera
import pygame.image
import subprocess
import os
import time

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
    readvar = file_len("out.json")
    if not readvar == 1:
	
        with open('video.css', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
    	    # now change the 14th line
    	    data[13] = '    display: none;\n'

    	    # and write everything back
    	    with open('video.css', 'w') as file:
                file.writelines( data )
	    subprocess.call("DEL /F /S /Q /A out.json", shell=True)
    	    time.sleep(2)
    else:
	pass

#This is the main code
#load_recognizer()
while True:
#    take_photo()
    compare_photo()
    read_json()
    time.sleep(1)
