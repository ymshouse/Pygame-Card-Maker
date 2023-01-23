
import pygame, sys
from pygame.locals import QUIT
import random
def int_screen():
    # inital Screen

    pygame.init()
    size = (640, 480)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Enter numbers from 1-3 to see different images. ")
    background = pygame.Surface(size).convert()
    background.fill((255, 0, 0))
    clock = pygame.time.Clock()
    full_size = (640, 480)
    background = pygame.Surface(full_size).convert()
    red_bar = pygame.Surface(size).convert()
    red_bar.fill((255, 0, 0))
    screen = pygame.display.set_mode(full_size)
    img = pygame.image.load("E.jpg")
    screen.blit(img, (0, 0))
    pygame.display.set_caption("Select from 1-3")
    pygame.display.flip()

    user_input = user_key_input()

    if user_input == '2':
        return 2
    elif user_input == '3':
        return 3
    else:
        card = card_selection_screen()
        return card
    make_card_screen()


def card_selection_screen():
    full_size = (640, 480)
    screen = pygame.display.set_mode(full_size)
    songs = {
        "1": "kiki.mp3",
        "2": "canada.mp3",
        "3": "happybirthday.mp3"
    }
    images = {
        "1": "CLB.jpg",
        "2": "canada.jpg",
        "3": "Ford-Bee.jpg"
    }
    img = pygame.image.load("Menu.jpg")
    screen.blit(img, (0, 0))
    pygame.display.flip()
    image_index = user_key_input()
    card = make_card_screen(images.get(image_index),songs.get(image_index))
    return card


def picture_resize(pic_name):
    picture = pygame.image.load(pic_name)
    picture = pygame.transform.scale(picture, (200, 200))
    return picture


def make_card_screen(image_name,song_name):
    full_size = (640, 480)
    screen = pygame.display.set_mode(full_size)
    print(image_name)
    print(song_name)
    bg_image = pygame.image.load(image_name)
    screen.blit(bg_image, (0, 0))

    #playing songs
    song = pygame.mixer.Sound(song_name)
    song.set_volume(0.3)
    song.play()
    # creating sender box
    sender_value = "To:"
    sender_field_surf = pygame.Surface((300, 50)).convert()
    sender_field_surf.fill((255, 255, 255))
    sender_font = pygame.font.SysFont("helvetica", 20)

    sender_field = sender_font.render(sender_value, True, (0, 0, 0))

    screen.blit(sender_field_surf, (25, 25))
    screen.blit(sender_field, (60, 40))

    # creating greeting box
    greetings_field_surf = pygame.Surface((300, 50)).convert()
    greetings_field_surf.fill((255, 255, 255))
    greeting_font = pygame.font.SysFont("helvetica", 20)
    greeting_value = ""
    greeting_field = greeting_font.render(greeting_value, True, (0, 0, 0))

    screen.blit(greetings_field_surf, (25, 125))
    screen.blit(greeting_field, (60, 40))

    # creating receiver box
    receiver_field_surf = pygame.Surface((300, 50)).convert()
    receiver_field_surf.fill((255, 255, 255))
    receiver_font = pygame.font.SysFont("helvetica", 20)
    receiver_value = "From:"
    receiver_field = receiver_font.render(receiver_value, True, (0, 0, 0))

    screen.blit(receiver_field_surf, (25, 225))
    screen.blit(receiver_field, (60, 40))

    pygame.display.flip()

    do_sender = True
    while do_sender:

        clock = pygame.time.Clock()
        clock.tick(10)
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    do_sender = False
                elif ev.key == pygame.K_BACKSPACE and len(sender_value):
                    sender_value = sender_value[:-1]
                    sender_field = sender_font.render(sender_value, True, (0, 0, 0))
                elif ev.unicode.isalnum() or ev.key == pygame.K_SPACE:
                    sender_value += ev.unicode
                    sender_field = sender_font.render(sender_value, True, (0, 0, 0))

        screen.blit(sender_field_surf, (50, 25))
        screen.blit(sender_field, (35, 40))
        pygame.display.flip()

    do_greeting = True
    while do_greeting:

        clock = pygame.time.Clock()
        clock.tick(10)
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    do_greeting = False
                elif ev.key == pygame.K_BACKSPACE and len(greeting_value):
                    greeting_value = greeting_value[:-1]
                    greeting_field = greeting_font.render(greeting_value, True, (0, 0, 0))
                elif ev.unicode.isalnum() or ev.key == pygame.K_SPACE:
                    greeting_value += ev.unicode
                    greeting_field = greeting_font.render(greeting_value, True, (0, 0, 0))

        screen.blit(greetings_field_surf, (50, 125))
        screen.blit(greeting_field, (60, 140))
        pygame.display.flip()

    do_receiver = True
    while do_receiver:

        clock = pygame.time.Clock()
        clock.tick(10)
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    do_receiver = False
                elif ev.key == pygame.K_BACKSPACE and len(receiver_value):
                    receiver_value = receiver_value[:-1]
                    receiver_field = receiver_font.render(receiver_value, True, (0, 0, 0))
                elif ev.unicode.isalnum() or ev.key == pygame.K_SPACE:
                    receiver_value += ev.unicode
                    receiver_field = receiver_font.render(receiver_value, True, (0, 0, 0))

        screen.blit(receiver_field_surf, (50, 225))
        screen.blit(receiver_field, (60, 240))
        pygame.display.flip()

    if user_return_key():
        # cards = (image_name, sender_value, greeting_value, receiver_value)
        card = (image_name, sender_value, greeting_value, receiver_value)
        # cards.append(card)
        print(card)
        song.stop()
        return card
        # view_card(image_name, sender_value, greeting_value, receiver_value)


def view_card(cards):
    print("View cards")
    for items in cards:
        print(items[0])
        print(items[1])
        print(items[2])
        print(items[3])

        full_size = (640, 480)
        pygame.display.set_caption("View Cards: press any key to see cards and enter to return to main menu")
        background = pygame.Surface(full_size).convert()
        background.fill((255, 255, 255))
        screen = pygame.display.set_mode(full_size)
        bg_image = pygame.image.load(items[0])

        background.blit(bg_image, (0, 0))
        sender_font = pygame.font.SysFont("helvetica", 20)
        sender_field = sender_font.render(items[1], True, (255, 255, 255))
        background.blit(sender_field, (60, 40))

        greeting_font = pygame.font.SysFont("helvetica", 20)
        greeting_field = greeting_font.render(items[2], True, (255, 255, 255))
        background.blit(greeting_field, (60, 80))

        receiver_font = pygame.font.SysFont("helvetica", 20)
        receiver_field = receiver_font.render(items[3], True, (255, 255, 255))
        background.blit(receiver_field, (60, 300))

        
        screen.blit(background, (0,0))

        pygame.display.flip()

        user_key_input()

    print("Before main screen")
    if user_return_key():
        int_screen()


def user_key_input():
    clock = pygame.time.Clock()
    while True:
        clock.tick(10)
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                return ev.unicode


def user_return_key():
    clock = pygame.time.Clock()
    while True:
        clock.tick(10)
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    return True


def user_mouse_input():
    clock = pygame.time.Clock()
    print("Mouse Click")
    while True:
        clock.tick(10)
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # right click
                print(ev.button)
                if ev.button == 3:
                    print("Right Click")
                    return False
                elif ev.button == 1:
                    print("Left  Click")
                    return True


def main():
    cards = []
    while True:

        user_response = int_screen()
        print(user_response)
        if user_response == 2:
            view_card(cards)
        elif user_response == 3:
            break
        elif type(user_response) is tuple:
            cards.append(user_response)
            print(cards)


main()
