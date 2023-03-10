import pygame
from settings import Settings
class CreateButton:
    def __init__(self,display,pos,text):
        self.display_surface = display
        self.settings = Settings()
        self.settings.set_scale_display()
        self.font = pygame.font.SysFont('Calibri', int((42 * self.settings.width_scale) + (42 * self.settings.height_scale) / 4) )

        self.button = pygame.Surface((400 * self.settings.width_scale, 80 * self.settings.height_scale), pygame.SRCALPHA)
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
