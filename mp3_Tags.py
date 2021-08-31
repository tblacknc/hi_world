import eyed3
import re
import time
import os
from os import walk

mypath = r'C:\Users\tblac\Desktop\iTunes Music\new'

for (dirpath, dirnames, filenames) in walk(mypath):

    os.chdir(dirpath)
    cwd = os.getcwd()
    
    for filename in filenames:
        
        dirs = cwd.split("\\")
        
        albm = dirs[-1]
        artist = dirs[-2]
                
        if re.findall("mp3$", filename):

            audiofile = eyed3.load(filename)

            try:
                audiofile.tag.album = albm
                audiofile.tag.artist = artist                
                audiofile.tag.title = titletag
                               
                print("title ===== ", audiofile.tag.title)
                print("artist ===== ", audiofile.tag.artist)
                print("dirAlbum ===== ", audiofile.tag.album)
                print("*************************************************")           

            except:
                error_dir = error_dir ,"\n", dirpath, "\n", filename
                print("title ===== ", audiofile.tag.title)
                print("artist ===== ", audiofile.tag.artist)
                print("dirAlbum ===== ", audiofile.tag.album)
                print("*************************************************")
                time.sleep(2)
            
            try:
                audiofile.tag.save()
            except:
                print("COULDN'T SAVE audiofile.tag.save...... DRATS")
                print("title ===== ", audiofile.tag.title)
                print("artist ===== ", audiofile.tag.artist)
                print("dirAlbum ===== ", audiofile.tag.album)
                print("*************************************************")
                time.sleep(2)
                
