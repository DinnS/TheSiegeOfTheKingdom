import json

class FileManage:

    def save_file(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data