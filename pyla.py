import pygame

class Pyla(pygame.sprite.Sprite):
    """создаю пули в текущей позиции пушки"""
    def __init__(self, screen, ginn):
        super(Pyla, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 139, 195, 74
        self.speed = 0.9
        self.rect.centerx = ginn.rect.centerx
        self.rect.top = ginn.rect.top
        self.y = float(self.rect.y)

        """перемещение пули вверх"""
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
        """рисую пулю на экране"""
    def draw_pyla(self):
        pygame.draw.rect(self.screen, self.color, self.rect)



