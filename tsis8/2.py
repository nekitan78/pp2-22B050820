import pygame
import os
import random

pygame.init()
_songs = ['Die For You (256  kbps).mp3', 'INSTASAMKA - LIPSI HA (Премьера клипа, 2022, prod. realmoneyken) (256  kbps).mp3', 'INSTASAMKA - ЗА ДЕНЬГИ ДА (prod. realmoneyken) (256  kbps).mp3']

_currently_playing_song = None
next_song = random.choice(_songs)
SONG_END = pygame.USEREVENT + 1

cntsng = 0

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load('Die For You (256  kbps).mp3')
pygame.mixer.music.play()


def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

width = 600
height = 500

fps = 60

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Player")


snd = True


def main():
    global snd, _currently_playing_song, next_song, cntsng
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == SONG_END:
                play_a_different_song()
                cntsng += 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE and snd:
                    pygame.mixer.music.pause()
                    snd = False
                elif event.key == pygame.K_SPACE:
                    pygame.mixer.music.unpause()
                    snd = True
                if event.key == pygame.K_RIGHT:
                    cntsng += 1
                    pygame.mixer.music.load(_songs[cntsng])
                    pygame.mixer.music.play()
                if event.key == pygame.K_LEFT:
                    cntsng -= 1
                    pygame.mixer.music.load(_songs[cntsng])
                    pygame.mixer.music.play()


        win.fill((255, 255, 255))
        font = pygame.font.SysFont(None, 24)
        img = font.render(f'Current music is {_songs[cntsng]}', True, (0,0,255))
        win.blit(img, (width/2 - 200, height/2))

        info = font.render(" Press space to stop music" , True, (0,0,0))
        info1 = font.render(" Press arrow(R) to play next song" , True, (0,0,0))
        info2 = font.render(" Press arrow(L) to play prev song" , True, (0,0,0))
        
        win.blit(info, (20, 20))
        win.blit(info1, (20, 40))
        win.blit(info2, (20, 60))
        pygame.display.update()

    pygame.quit()


main()