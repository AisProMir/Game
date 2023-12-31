import pygame

"""инициализация пушки"""
class Gun():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("image/pixil-frame-0.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    """Рисование пушки"""
    def out_put(self):
        self.screen.blit(self.image, self.rect)

    """обновление позиции пушки"""
    def update_up(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 3
        if self.mleft and self.rect.left > 0:
            self.center -= 3

        self.rect.centerx = self.center

        """размещает пушку по центру внизу"""
    def create_gun(self):
        self.center = self.screen_rect.centerx



