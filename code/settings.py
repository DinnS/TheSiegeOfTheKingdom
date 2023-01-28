import pygame.display

from file_manage import FileManage


class Settings:
    def __init__(self):
        self.file_manage = FileManage()
        self.settings_data = self.file_manage.load_file('../save/settings_data.json')

        self.window_width = self.settings_data["window_width"]
        self.window_height = self.settings_data["window_height"]
        self.full_screen = bool(self.settings_data["window_full_screen"])

        # Fix full screen 0,0
        self.current_window_width = pygame.display.Info().current_w
        self.current_window_height = pygame.display.Info().current_h

        # Scaling screen
        self.base_width = 1280
        self.base_height = 720

    def set_scale_display(self):
        self.info_display = pygame.display.Info()
        self.width_scale = self.info_display.current_w / self.base_width
        self.height_scale = self.info_display.current_h / self.base_height


    def update(self):
        self.settings_data = self.file_manage.load_file('../save/settings_data.json')
        self.window_width = self.settings_data["window_width"]
        self.window_height = self.settings_data["window_height"]


