import pygame
from settings import Settings
class Notification:
    def __init__(self, text, pos, display, notifications_color = (194, 217, 255)):
        self.display = display
        self.settings = Settings()
        self.settings.set_scale_display()

        self.font = pygame.font.SysFont('Calibri', int((30 * self.settings.width_scale) + (30 * self.settings.height_scale) / 4))

        # notification box
        self.surface = pygame.surface.Surface((400 * self.settings.width_scale,400 * self.settings.height_scale))
        self.surface.fill((51, 51, 51))
        self.surface_rect = self.surface.get_rect(center = pos)

        # button for accept notification and text
        self.button = pygame.surface.Surface((120 * self.settings.width_scale,60 * self.settings.height_scale))
        self.button.fill((255, 230, 230))
        self.button_rect = self.button.get_rect(midbottom = (self.surface_rect.center[0],(self.surface_rect.midbottom[1] - (60 * self.settings.height_scale)) ))
        self.button_text = self.font.render('OK',True, 'Red')
        self.button_text_rect = self.button_text.get_rect(center = self.button_rect.center)

        # wrap the notifications
        self.notifications_color = notifications_color
        self.text = text
        self.text_lines = []
        self.line = ""
        for word in self.text.split():
            if self.font.size(self.line + " " + word)[0] <= self.surface.get_width():
                self.line += " " + word
            else:
                self.text_lines.append(self.line)
                self.line = word
        self.text_lines.append(self.line)

        self.notifications = [self.font.render(self.line, True, self.notifications_color) for self.line in self.text_lines]
        self.notifications_rect =[self.notification.get_rect() for self.notification in self.notifications]

        # Center each text
        for i, notification_rect in enumerate(self.notifications_rect):
            notification_rect.centerx = self.surface_rect.center[0]
            notification_rect.centery = self.surface_rect.midtop[1] +  (i * 60) + (80 * self.settings.height_scale)

    def check_button(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return False
        return True

    def draw(self):
        if self.check_button():
            self.display.blit(self.surface, self.surface_rect)
            self.display.blit(self.button,self.button_rect)

            for notification, notification_rect in zip(self.notifications,self.notifications_rect):
                self.display.blit(notification, notification_rect)

            self.display.blit(self.button_text, self.button_text_rect)
            return True
        else:
            return False


