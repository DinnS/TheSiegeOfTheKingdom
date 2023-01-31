import pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self , display):
        super().__init__()
        self.display_surface = display

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2



        # ground
        self.ground_surf = pygame.image.load('../graphics/map.png').convert()
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))

    def center_target_camera(self, target):
        if 0 < target.rect.centerx - self.half_w < self.ground_surf.get_width() - (self.half_w * 2):
            self.offset.x = target.rect.centerx - self.half_w
        if 0 < target.rect.centery - self.half_h < self.ground_surf.get_height() - (self.half_h * 2):
            self.offset.y = target.rect.centery - self.half_h



    def custom_draw(self, player):
        self.center_target_camera(player)

        # ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf,ground_offset)


        #Active element   Ysort camera
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

