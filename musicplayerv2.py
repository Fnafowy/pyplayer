import os
import pygame
from tinytag import TinyTag
import datetime
os.system('cls')
pygame.mixer.init()

# direc = input('Paste in your music directory: ')
directory = 'C:\\Users\\Admin\\Music'
folders = os.listdir(directory)
def ChooseFolder():
    print("--- WELCOME TO TOMASHEWSKI'S MUSIC PLAYER V2 INTERNAL ---")
    actFolders = []
    for i in range(len(folders)):
        if os.path.isdir(directory+'\\'+folders[i]) == True:
            actFolders.append(folders[i])
    for i in range(len(actFolders)):
        print(f'[{i}] {actFolders[i]}')
    folderIndex = int(input('What folder do you want to scan for songs: '))
    return(actFolders[folderIndex])

def SongSelect():
    os.system('cls')
    songs = []
    folder = ChooseFolder()
    os.system('cls')
    files = os.listdir(directory+'\\'+folder)
    for i in range(len(files)):
        if files[i].lower().endswith(('.flac', '.mp3', '.wav','.m4a')) == True: 
            songs.append(files[i])
    for i in range(len(songs)):
        tag: TinyTag = TinyTag.get(directory+'\\'+folder+'\\'+songs[i])
        print(f'[{i}] {tag.title}')
    songChoice = int(input('Choose what song you want to play: '))
    return(directory+'\\'+folder+'\\'+songs[songChoice])

def PlaySong():
    chosenSong = SongSelect()
    pygame.mixer.music.load(chosenSong)
    pygame.mixer.music.play()
    return(chosenSong)

isPaused = 0
IsQueued = 0
newSong = str(PlaySong())

while True:
    tag: TinyTag = TinyTag.get(newSong)
    length = str(datetime.timedelta(seconds=round(tag.duration)))
    topMsg = f'{tag.title} - {tag.artist} : {length[2:]}\n'
    os.system('cls')
    if isPaused == 0:
        print('----- NOW PLAYING -----')
    elif isPaused == 1:
        topMsg = f"{tag.title} - {tag.artist} is paused...\n"
    print(topMsg)
    if IsQueued == 1:
        print(f'----- UP NEXT: ------\n{tagQueued.title} - {tagQueued.artist} : {lengthQueued[2:]}\n')
    print("Press enter to pause/unpause the music")
    print("Press 'v' to change volume")
    print("Press 'q' to add a file to the queue")
    if IsQueued == 1:
        print("Press 's' to skip the current song")
    print("Press 'e' to go back to folder selection")
    print("Press 'x' to exit the player")
    #take user input
    userInput = input("")
	
    if userInput == '':
        # Pause the music
        if isPaused>=1:
            pygame.mixer.music.unpause()
            isPaused=0
            topMsg = f'{tag.title} - {tag.artist} : {length[2:]}'
            os.system('cls')
        else:
            pygame.mixer.music.pause()	    
            isPaused += 1
            os.system('cls')
            
    elif userInput == 'v':
        # Change the volume
        os.system('cls')
        userVol = int(input('Set volume to (in %): '))
        pygame.mixer.music.set_volume(userVol/100)
        os.system('cls')

    elif userInput == 'e':
        os.system('cls')   
        newSong = PlaySong()
        topMsg = f'{tag.title} - {tag.artist} : {length[2:]}'

    elif userInput == 'q':
        queuedSongPath = SongSelect()
        pygame.mixer.music.queue(queuedSongPath)
        tagQueued: TinyTag = TinyTag.get(queuedSongPath)
        lengthQueued = str(datetime.timedelta(seconds=round(tagQueued.duration)))
        IsQueued = 1

    elif userInput == 's':
        pygame.mixer.music.set_pos((tag.duration*10)+2)
        IsQueued = 0
        os.system('cls')
        newSong = queuedSongPath

    elif userInput == 'x':
        os.system('cls')
        break
        
    else:
        os.system('cls')