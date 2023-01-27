import sys
import json
import pygame

class Button:
    def __init__(self,display,pos,text):
        self.display_surface = display
        self.font = pygame.font.SysFont('Calibri', 60)

        self.button = pygame.Surface((400, 80), pygame.SRCALPHA)
        self.button_rect = self.button.get_rect(topleft=pos)

        self.button_text = self.font.render(text, True, 'white')
        self.button_text_rect = self.button_text.get_rect(midleft=(
            self.button_rect.left + 20,
            self.button_rect.centery
        ))


    def draw_rect_alpha(self, color, rect):
        surface = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(surface, color, surface.get_rect(), border_radius=10)
        self.display_surface.blit(surface, rect)

    def draw(self):
        self.display_surface.blit(self.button, self.button_rect)
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.draw_rect_alpha((65, 185, 245, 80), self.button_rect)
        self.display_surface.blit(self.button_text, self.button_text_rect)

class FileManage:
    def __init__(self):
        pass

    def save_game(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)
        print('Save data ...')

    def load_game(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        print('Load data ...')
        return data

class GameManage:
    def __init__(self,display_surf,data):
        self.display_surface = display_surf

        # Graphics object

        # text for buttons
        self.font = pygame.font.SysFont('Calibri', 60)

        # menu buttons
        self.menu_level = 1

        self.menu_play_button = Button(self.display_surface, (100, 200), 'Play')

        self.menu_settings_button = Button(self.display_surface, (100, 300), 'Settings')

        self.menu_quit_button = Button(self.display_surface, (100, 400), 'Quit')




        # pause buttons
        self.pause_resume_button = Button(self.display_surface, (100, 200), 'Resume')

        self.pause_save_button = Button(self.display_surface, (100,300), 'Save')

        self.pause_exit_button = Button(self.display_surface, (100,400), 'Exit')



        # Timer button
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
            self.file.save_game(self.data, '../data/data.json')

    def pause_quit(self, game_state) :
        if self.click_button(self.pause_exit_button.button_rect):
            game_state['menu_game'] = True
            game_state['running_game'] = False
            game_state['pause_game'] = False



    # Update state and draw buttons

    def update(self,game_state):
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