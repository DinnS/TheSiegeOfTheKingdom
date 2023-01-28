import sys
import json
import pygame

from create_button import CreateButton
from file_manage import FileManage
from settings import Settings
from notification import Notification


class GameManage:
    def __init__(self,display_surf,data):
        self.display_surface = display_surf

        self.menu_current_option = 'main'

        # Graphics object

        # menu buttons
        self.menu_level = 1

        self.menu_play_button = CreateButton(self.display_surface, (100, 200), 'Play')

        self.menu_settings_button = CreateButton(self.display_surface, (100, 300), 'Settings')
        self.settings_full_screen_button = CreateButton(self.display_surface, (100, 200), 'Full Screen')
        self.settings_back_button = CreateButton(self.display_surface, (100, 300), 'Back')



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
        self.settings_data = self.file.load_file('../save/settings_data.json')

        # other
        self.settings = Settings()

        self.is_notification = False



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

    def menu_settings(self):
        if self.click_button(self.menu_settings_button.button_rect):
            self.menu_current_option = 'settings'

    # menu settings

    def settings_full_screen(self):
        if self.click_button(self.settings_full_screen_button.button_rect):
            info_display = pygame.display.Info()
            display_x = info_display.current_w
            display_y = info_display.current_h
            self.notification = Notification(
                "You need to restart the game to apply the new settings",
                (display_x / 2,display_y / 2),
                self.display_surface
            )

            self.is_notification = True


            if not self.settings.full_screen:
                self.settings_data['window_width'] = 0
                self.settings_data['window_height'] = 0
                self.settings_data['window_full_screen'] = True
            elif self.settings.full_screen:
                self.settings_data['window_width'] = 1280
                self.settings_data['window_height'] = 720
                self.settings_data['window_full_screen'] = False
            self.file.save_file(self.settings_data, '../save/settings_data.json')

    def settings_back(self):
        keys = pygame.key.get_pressed()
        if self.click_button(self.settings_back_button.button_rect) or keys[pygame.K_ESCAPE]:
            self.menu_current_option = 'main'



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
            self.file.save_file(self.data, '../save/data.json')

    def pause_quit(self, game_state) :
        if self.click_button(self.pause_exit_button.button_rect):
            game_state['menu_game'] = True
            game_state['running_game'] = False
            game_state['pause_game'] = False
            self.file.save_file(self.data, '../save/data.json')



    # Update state and draw buttons

    def update(self,game_state, player):
        if game_state['menu_game']:
            if self.menu_current_option == 'main':
                self.menu_play_button.draw()
                self.menu_settings_button.draw()
                self.menu_quit_button.draw()

                self.menu_play(game_state)
                self.menu_settings()
                self.menu_quit(game_state)
            elif self.menu_current_option == 'settings':

                self.settings_full_screen_button.draw()
                self.settings_back_button.draw()

                self.settings_full_screen()

                self.settings_back()

                if self.is_notification:
                    self.is_notification = self.notification.draw()




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
