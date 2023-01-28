import sys
import pygame
from pytmx.util_pygame import load_pygame

from settings import Settings
from sprite import Sprite
from player import Player
from game_manage import GameManage,FileManage

class Game:
    def __init__(self):
        # base game
        pygame.init()
        self.settings = Settings()
        if self.settings.full_screen:
            self.display_surface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        else:
            self.display_surface = pygame.display.set_mode((self.settings.window_width, self.settings.window_height))


        pygame.display.set_caption('The Siege of the Kingdom')
        self.clock = pygame.time.Clock()


        # state game
        self.state = {
            'menu_game': True,
            'running_game': False,
            'pause_game': False,
        }


        # Groups
        self.ground_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()

        # Save/load manage
        self.data = FileManage().load_file('../save/data.json')

        # Manage states a game and manage all buttons in menu and pause
        self.game_manage = GameManage(self.display_surface, self.data)

        # Init other classes
        self.player = Player((self.data["player_position"]),self.player_group)


        self.setup()


    # create map
    def setup(self):

        tmx_map = load_pygame('../data/map.tmx')

        # tiles
        for x,y,surf in tmx_map.get_layer_by_name('Ground').tiles():
            Sprite(surf,(x * 64,y * 64),self.ground_group)


    def run(self):
        while True:
            # global event action
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # variable for fixing all game movemnt
            self.dt = self.clock.tick() / 1000

            # state game
            if self.state['running_game']:
                # draw display
                self.ground_group.draw(self.display_surface)
                self.player_group.draw(self.display_surface)

                # update
                self.player_group.update(self.dt)
                self.game_manage.update(self.state, self.player)


            elif self.state['menu_game']:
                # draw
                self.display_surface.fill('black')

                # update
                self.game_manage.update(self.state, self.player)

            elif self.state['pause_game']:

                # draw
                self.display_surface.fill('black')

                # update
                self.game_manage.update(self.state, self.player)


            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()