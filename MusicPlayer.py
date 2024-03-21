import pygame as pg

pg.init()

screen = pg.display.set_mode((400,300))
pg.display.set_caption("MusicPlayer!")
icon = pg.display.set_icon(pg.image.load('images/icon.png'))
done = False

def play_next():
    global current_music, songs, current_index
    next_song_index = (current_index + 1) % len(songs)
    current_music = songs[next_song_index]
    pg.mixer.music.load(current_music)
    pg.mixer.music.play()
    current_index = next_song_index
    
def play_previous():
    global current_music, songs, current_index
    previous_song_index = (current_index - 1) % len(songs)
    current_music = songs[previous_song_index]
    pg.mixer.music.load(current_music)
    pg.mixer.music.play()
    current_index = previous_song_index

def play_pause():
    if pg.mixer.music.get_busy():
        pg.mixer.music.pause()
    else:
        pg.mixer.music.unpause()

def stop():
    pg.mixer.music.stop()

songs = ['sounds/BlackHole.mp3', 'sounds/Daylight.mp3', 'sounds/ShootingStars.mp3']
current_index = 0
current_music = songs[current_index]
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:    
            if event.key == pg.K_SPACE:
                screen.fill('blue')
                play_pause()
            if event.key == pg.K_RIGHT:
                screen.fill('green')
                play_next()
            if event.key == pg.K_LEFT:
                screen.fill('green')
                play_previous()
            if event.key == pg.K_s:
                screen.fill('red')
                stop()
    pg.display.flip()
pg.quit()