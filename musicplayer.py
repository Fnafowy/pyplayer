import os
import pygame
from tinytag import TinyTag
import datetime
pygame.mixer.init()
print("--- WELCOME TO TOMASHEWSKI'S MUSIC PLAYER ---")
# direc = input('Paste in your music directory: ')
direc = 'C:\\Users\\Admin\\Music'
folders = os.listdir(direc)
def MusicSelect():
    os.system('cls')
    for i in range(len(folders)-1):
        print(f'[{i}] {folders[i+1]}')
    x = int(input('Choose which directory to scan for music: '))
    os.system('cls')  
    files = os.listdir(direc+"\\"+folders[x+1])
    for i in range(len(files)):
        print(f'[{i}] {files[i]}')
    mp3 = int(input('What do ya wanna play: '))
    if files[mp3].lower().endswith(('.flac', '.mp3', '.wav','.m4a')) != True:
          os.system('cls')
          for i in range(len(files)):
            print(f'[{i}] {files[i]}')
          print('!CHOOSE A CORRECT FILE TYPE!')
          mp3 = int(input('What do ya wanna play: '))
    tag: TinyTag = TinyTag.get(direc+"\\"+folders[x+1]+'\\'+files[mp3])
    length = str(datetime.timedelta(seconds=round(tag.duration)))
    songInfo = [folders[x+1],files[mp3],(tag.title+' - '+tag.artist),length[2:],round(tag.duration)]
    return(songInfo)

qued = 0
def MusicQueue():
    os.system('cls')
    for i in range(len(folders)-1):
        print(f'[{i}] {folders[i+1]}')
    x = int(input('Choose which directory to scan for music: '))
    os.system('cls')  
    files = os.listdir(direc+"\\"+folders[x+1])
    for i in range(len(files)):
        print(f'[{i}] {files[i]}')
    mp3 = int(input('What do ya wanna play: '))
    if files[mp3].lower().endswith(('.flac', '.mp3', '.wav','.m4a')) != True:
          os.system('cls')
          for i in range(len(files)):
            print(f'[{i}] {files[i]}')
          print('!CHOOSE A CORRECT FILE TYPE!')
          mp3 = int(input('What do ya wanna play: '))
    tag: TinyTag = TinyTag.get(direc+"\\"+folders[x+1]+'\\'+files[mp3])
    length = str(datetime.timedelta(seconds=round(tag.duration)))
    songInfo = [folders[x+1],files[mp3],(tag.title+' - '+tag.artist),length[2:],round(tag.duration)]
    return(songInfo)
            
songInfo = MusicSelect()
topMsg = activeSong = f'Now playing {songInfo[2]} : {songInfo[3]}'
def PlaySong():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(direc+"\\"+songInfo[0]+'\\'+songInfo[1])
    os.system('cls')
    pygame.mixer.music.play()
    print(activeSong)

PlaySong()
x=0
while True: 
    print(topMsg)
    print("Press enter to pause/unpause the music")
    print("Press 'v' to change volume")
    print("Press 'q' to add a file to the queue")
    print("Press 's' to skip the current song")
    print("Press 'e' to go back to folder selection")
    print("Press 'x' to exit the player")
    #take user input
    userInput = input("")
	
    if userInput == '':
        # Pause the music
        if x>=1:
            pygame.mixer.music.unpause()
            os.system('cls')
            x=0
        else:
            os.system('cls')
            pygame.mixer.music.pause()	    
            left = str(datetime.timedelta(seconds=round(songInfo[4]-(round(int(pygame.mixer.music.get_pos())/1000)))))
            topMsg = (f"{songInfo[2]} is paused ({left[2:]} left)....")
            x += 1
            
    elif userInput == 'v':
        # Change the volume
        os.system('cls')
        userVol = int(input('Set volume to (in %): '))
        pygame.mixer.music.set_volume(userVol/100)
        os.system('cls')

    elif userInput == 'e':
        os.system('cls')   
        songInfo=MusicSelect()
        pygame.mixer.music.unload()
        activeSong = f'Now playing {songInfo[2]} : {songInfo[3]}'
        PlaySong()

    elif userInput == 's':
        pygame.mixer.music.set_pos((songInfo[4]*10)+1)
        os.system('cls')
        

    elif userInput == 'q':
        if qued == 1:
            songInfo = MusicQueue()
            pygame.mixer.music.queue(direc+"\\"+songInfo[0]+'\\'+songInfo[1])
            os.system('cls')
        elif qued == 0:
            songInfo2 = MusicQueue()
            pygame.mixer.music.queue(direc+"\\"+songInfo2[0]+'\\'+songInfo2[1])
            activeSong2 = f'Now playing {songInfo2[2]} : {songInfo2[3]}'
            os.system('cls')
            qued = 1
        
        
    elif userInput == 'x':
        break

    else:
        os.system('cls')