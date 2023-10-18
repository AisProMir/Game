import pygame

class Bullet(pygame.sprite.Sprite):
    """создаю пули в текущей позиции пушки"""
    def __init__(self, screen, ginn):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 100, 12)
        self.color = 139, 195, 74
        self.speed = 4.5
        self.rect.centerx = ginn.rect.centerx
        self.rect.top = ginn.rect.top
        self.y = float(self.rect.y)

        """перемещение пули вверх"""
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
        """рисую пулю на экране"""
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)