import pygame

class Game:
    def __init__(self):
        self.current_state = "menu"


        self.start_button = Button((250, 250), (100, 50), "Start", (255, 255, 255))
        self.pause_button = Button((250, 350), (100, 50), "Pause", (255, 255, 255))
        self.resume_button = Button((250, 350), (100, 50), "Resume", (255, 255, 255))

    def run_game(self):
        # Handle game logic and drawing here
        pass

    def show_menu(self):
        # Handle menu logic and drawing here
        self.start_button.draw(screen)
        if self.start_button.is_clicked():
            self.current_state = "running_game"

    def pause(self):
        # Handle pause logic and drawing here
        self.resume_button.draw(screen)
        if self.resume_button.is_clicked():
            self.current_state = "running_game"

    def handle_input(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.current_state == "running_game":
                    self.current_state = "pause"
                elif self.current_state == "pause":
                    self.current_state = "running_game"
            elif event.key == pygame.K_RETURN:
                if self.current_state == "menu":
                    self.current_state = "running_game"

    def run(self):
        pygame.init()
        while True:
            for event in pygame.event.get():
                self.handle_input(event)
            if self.current_state == "running_game":
                self.run_game()
            elif self.current_state == "menu":
                self.show_menu()
            elif self.current_state == "pause":
                self.pause()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
