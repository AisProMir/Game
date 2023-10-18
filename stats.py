"""отслеживание статистики"""
class Stats():

    """инициализирует статистику"""
    def __init__(self):
     self.reset_stats()

     """статистика изменяющаяся во время игры"""
    def reset_stats(self):
        self.guns_left = 3
