import eyed3
import re
import time
import os
from os import walk


mypath = r'C:\Users\tblac\Desktop\latest tunes\new'
#mypath = r'C:\Users\tblac\Desktop\latest tunes'
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
        
        #dirs = cwd.split("\\")
        
        txt = cwd
        x = re.split('\\\\', txt)

        albm = x[-1]
        artist = x[-2]
                
        if re.findall("mp3$", filename):

            audiofile = eyed3.load(filename)
            titletag = re.sub("\.mp3", "", filename)

            titletag = re.sub("^[0-9.-]*[0-9]*", "", titletag)
            track = re.search("^[0-9]*", filename)
            trackNum = track.group()
            
            try:
                audiofile.tag.album = albm
                audiofile.tag.artist = artist                
                audiofile.tag.title = titletag
                audiofile.tag.track_num = trackNum
                
                               
                print("title ===== ", audiofile.tag.title)
                print("artist ===== ", audiofile.tag.artist)
                print("dirAlbum ===== ", audiofile.tag.album)
                print("song name ===== ", filename)
                print("track num ====== ", audiofile.tag.track_num)
                print("*************************************************")           
            except:
                error_dir += "tags " 
                error_dir += str(titletag) 
                error_dir += str(artist)
                error_dir += str(albm)
                error_dir += str(trackNum)
                error_dir += "--------------------------\n\n"
                #error_dir += "tags____", str(artist), "____", str(albm)
                                
                print("title = ", titletag)
                print("artist = ", artist)
                print("album = ", albm)
                print("song name = ", filename)
                print("trackNum = ", trackNum)
                print("==================================================")
                time.sleep(1)
            
            try:
                audiofile.tag.save()
            except:
                print("COULDN'T SAVE audiofile.tag.save...... DRATS")
                error_dir += "Files " 
                error_dir += str(titletag) 
                error_dir += str(artist)
                error_dir += str(albm)
                error_dir += str(trackNum)
                error_dir += "--------------------------\n\n"
                
                print("title = ", titletag)
                print("artist = ", artist)
                print("album = ", albm)
                print("song name = ", filename)
                print("trackNum = ", trackNum)
                print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
                time.sleep(1)
    print(error_dir)                
