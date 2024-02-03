class Settings():
    """ Класс для хранения всех настроек игры """

    def __init__(self):
        """ Инициализация настроек игры """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Настройки снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 5
        self.fleet_drop_speed = 10
        
        # fleet_direction = 1 обозначает движение вправо, -1 - влево
        self.fleet_direction = 1