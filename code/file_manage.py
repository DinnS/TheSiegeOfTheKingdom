import json

class FileManage:

    def save_game(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_game(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data