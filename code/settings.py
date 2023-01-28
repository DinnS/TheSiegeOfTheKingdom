from file_manage import FileManage


class Settings:
    def __init__(self):
        self.file_manage = FileManage()
        self.settings_data = self.file_manage.load_file('../save/settings_data.json')

        self.window_width = self.settings_data["window_width"]
        self.window_height = self.settings_data["window_height"]
        self.full_screen = bool(self.settings_data["window_full_screen"])

    def update(self):
        self.settings_data = self.file_manage.load_file('../save/settings_data.json')
        self.window_width = self.settings_data["window_width"]
        self.window_height = self.settings_data["window_height"]


