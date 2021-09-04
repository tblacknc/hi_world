import eyed3
import re
import time
import os
from os import walk

mypath = r'C:\Users\tblac\Desktop\iTunes Music\new'
mypath = r'C:\Users\tblac\Desktop\latest tunes\new'
mypath = r'C:\Users\tblac\Desktop\latest tunes'
error_dir = "NONE"
albm = ""
artist = "" 
titletag = ""

for (dirpath, dirnames, filenames) in walk(mypath):

    try :
        os.chdir(dirpath)
        
    except:
        print("must be in that dir")
        time.sleep(2)
        continue
        
    cwd = os.getcwd()
    
    for filename in filenames:
        
        dirs = cwd.split("\\")
        albm = dirs[-1]
        artist = dirs[-2]
                
        if re.findall("mp3$", filename):

            audiofile = eyed3.load(filename)
            titletag = re.sub("\.mp3", "", filename)

            titletag = re.sub("^[0-9.-]*[0-9]*", "", titletag)

            try:
                audiofile.tag.album = albm
                audiofile.tag.artist = artist                
                audiofile.tag.title = titletag
                               
                print("title ===== ", audiofile.tag.title)
                print("artist ===== ", audiofile.tag.artist)
                print("dirAlbum ===== ", audiofile.tag.album)
                print("*************************************************")           
            except:
                error_dir += "Error while writing __TAGS__" 
                error_dir += str(titletag) 
                error_dir += str(artist)
                error_dir += str(albm)
                error_dir += "--------------------------\n\n"
                                
                print("title = ", titletag)
                print("artist = ", artist)
                print("album = ", albm)
                print("==================================================")
                time.sleep(2)
            
            try:
                audiofile.tag.save()
            except:
                print("COULDN'T SAVE audiofile.tag.save...... DRATS")
                error_dir += "Error while writing __FILE__" 
                error_dir += str(titletag) 
                error_dir += str(artist)
                error_dir += str(albm)
                error_dir += "--------------------------\n\n"
                
                print("title = ", titletag)
                print("artist = ", artist)
                print("album = ", albm)
                print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
                time.sleep(2)
    print(error_dir)                
