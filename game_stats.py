class GameStats():
    """ Отслеживание статистики """

    def __init__(self, ai_game):
        """ Инициализирует статистику """
        self.settings = ai_game.settings
        self.reset_stats()

        # Активное состояние игры
        self.game_active = True
    
    def reset_stats(self):
        """ Инициализирует статистику, изменяющуюся в ходе игры """
        self.ship_left = self.settings.ship_limit