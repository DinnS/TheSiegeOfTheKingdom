import sys
import json
import pygame

from create_button import CreateButton
from file_manage import FileManage


class GameManage:
    def __init__(self,display_surf,data):
        self.display_surface = display_surf

        # Graphics object

        # menu buttons
        self.menu_level = 1

        self.menu_play_button = CreateButton(self.display_surface, (100, 200), 'Play')

        self.menu_settings_button = CreateButton(self.display_surface, (100, 300), 'Settings')

        self.menu_quit_button = CreateButton(self.display_surface, (100, 400), 'Quit')



        # pause buttons
        self.pause_resume_button = CreateButton(self.display_surface, (100, 200), 'Resume')

        self.pause_save_button = CreateButton(self.display_surface, (100, 300), 'Save')

        self.pause_exit_button = CreateButton(self.display_surface, (100, 400), 'Exit')

        # Cooldown click button
        self.last_click_time = 0
        self.cooldown_click = 400

        # Save/load manage
        self.file = FileManage()
        self.data = data

    def click_button(self, button_rect):
        current_click_time = pygame.time.get_ticks()
        if current_click_time - self.last_click_time > self.cooldown_click:
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    self.last_click_time = current_click_time
                    return True

        return False


    # Menu function

    def menu_play(self, game_state):
        if self.click_button(self.menu_play_button.button_rect) and game_state['menu_game']:
            game_state['menu_game'] = False
            game_state['running_game'] = True
            game_state['pause_game'] = False


    def menu_quit(self, game_state) :
        if self.click_button(self.menu_quit_button.button_rect) and game_state['menu_game']:
            pygame.quit()
            sys.exit()

    # Game function

    def game_pause(self, game_state):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and game_state['running_game']:
            game_state['menu_game'] = False
            game_state['running_game'] = False
            game_state['pause_game'] = True

    # Pause function

    def pause_resume(self, game_state):
        if self.click_button(self.pause_resume_button.button_rect):
            game_state['menu_game'] = False
            game_state['running_game'] = True
            game_state['pause_game'] = False


    def pause_save(self):
        if self.click_button(self.pause_save_button.button_rect):
            self.file.save_game(self.data, '../save/data.json')

    def pause_quit(self, game_state) :
        if self.click_button(self.pause_exit_button.button_rect):
            game_state['menu_game'] = True
            game_state['running_game'] = False
            game_state['pause_game'] = False
            self.file.save_game(self.data, '../save/data.json')



    # Update state and draw buttons

    def update(self,game_state, player):
        if game_state['menu_game']:

            self.menu_play_button.draw()
            self.menu_settings_button.draw()
            self.menu_quit_button.draw()


            self.menu_play(game_state)
            self.menu_quit(game_state)


        if game_state['pause_game']:
            self.pause_resume_button.draw()
            self.pause_save_button.draw()
            self.pause_exit_button.draw()


            self.pause_resume(game_state)
            self.pause_save()
            self.pause_quit(game_state)


        if game_state['running_game']:
            self.game_pause(game_state)

            self.data['player_position'] = [player.pos.x, player.pos.y]
