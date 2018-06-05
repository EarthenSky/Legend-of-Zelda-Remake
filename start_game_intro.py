'''In this file the user will be able to set if the game is full screen or not,
assign which keys do what (maybe even use a controller?), and might be given a small tip
about moving the story along (try to leave the town if you havn't played any pokemon games before.)
before being sent into the main intro loop.'''

import sys
import pygame

# Import the hidden main gameloop class.
# This calls the main functions in the gameloop, like update() or check_input().
sys.path.insert(0, 'src/')  # This line tells the importer where to look for the module.
import game_loop_hidden

# The asset manager helps render images.
sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import desc_manager

FPS = 60

pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie("resc/Videos/PokemonWaveBlueIntro.mpg")
SCREEN = pygame.display.set_mode(movie.get_size(), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
movie_screen = pygame.Surface(movie.get_size()).convert()
movie.set_display(movie_screen)
movie.play()

Oak = pygame.image.load('resc/images/prof_oak.png').convert_alpha()
player = ""
rival_name = ""

total_time = 0

playing = True

imgNaming = pygame.image.load("resc/images/main_characters.png").convert()
rival_background = pygame.image.load("resc/images/rival_background.png").convert()

import pygame as pg

def player_name():
    global player
    screen = pg.display.set_mode((960, 640))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(340, 288, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        player = text
                        text = ''
                        done = True
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        SCREEN.fill( (255,255,255,255) )
        SCREEN.blit(imgNaming, (0,0))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        SCREEN.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(SCREEN, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)


def naming_rival():
    global rival_name
    screen = pg.display.set_mode((960, 640))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(340, 288, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        rival_name = text
                        text = ''
                        done = True
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        SCREEN.fill( (255,255,255,255) )
        SCREEN.blit(rival_background, (0,0))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        SCREEN.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(SCREEN, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__names__':
    pg.init()
    main()
    pg.quit()


while playing:
    dt = clock.tick(FPS) / 1000.0
    total_time += dt
    print total_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False
        if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN and total_time > 1:
				movie.stop()
				playing = False


    SCREEN.blit(movie_screen,(0,0))
    pygame.display.update()

SCREEN = pygame.display.set_mode( (960, 640), pygame.FULLSCREEN )

SCREEN.fill( (255,255,255,255) )

SCREEN.blit(Oak,(300,50))

desc_manager.add_message_to_queue("Now, what is your name?", "")
desc_manager.add_message_to_queue("Become the best Pokemon", "trainer in the world!")
desc_manager.add_message_to_queue("Your objective:", "")
desc_manager.add_message_to_queue("Here, your story beings", "enjoy your adventure")
desc_manager.add_message_to_queue("So you must prepare", "and adapt to every enemy")
desc_manager.add_message_to_queue("As you become better,", "so will your enemies.")
desc_manager.add_message_to_queue("And they will grow", "stronger every battle.")
desc_manager.add_message_to_queue("You will form bonds with ", "your Pokemon")
desc_manager.add_message_to_queue("Battle against other trainers.", "")
desc_manager.add_message_to_queue("You are a trainer, you collect", "Pokemon to...")
desc_manager.add_message_to_queue("This world is inhabited by", "creatures known as Pokemon")
desc_manager.add_message_to_queue("Welcome to the world of Pokemon!", "My name is Professor Oak.")

desc_manager.check_queue( SCREEN )

player_name()

desc_manager.add_message_to_queue("What do you like calling", "him again?")
desc_manager.add_message_to_queue("You two are going to", "settle this debate many times.")
desc_manager.add_message_to_queue("He too aspires to be the", "greatest in the world")
desc_manager.add_message_to_queue("My grandson is also a", "Pokemon trainer")
desc_manager.add_message_to_queue("Nice to meet you", str(player) + "!")
desc_manager.add_message_to_queue("So, your name is", str(player) + "?")

desc_manager.check_queue( SCREEN )

naming_rival()

desc_manager.add_message_to_queue("Have fun you two!", "")
desc_manager.add_message_to_queue("in order to prevail over", "your cometing trainers.")
desc_manager.add_message_to_queue("and to form the strongest", "of bonds with your team")
desc_manager.add_message_to_queue("Remember to study", "the Pokemon you catch,")
desc_manager.add_message_to_queue("you to start the ", "adventure of a lifetime!")
desc_manager.add_message_to_queue("Well then, we're all set", "for the two of")
desc_manager.add_message_to_queue("So his name is", str(rival_name) + "?")

desc_manager.check_queue( SCREEN )


game_loop_hidden.start_gameloop()
