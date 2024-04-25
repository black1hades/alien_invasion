class Settings:
    """存储游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船速度
        self.ship_speed = 0.5
        self.ship_limit = 2
        # 子弹设置
        self.bullet_speed = 0.8
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # 外星人设置
        self.alien_speed = 0.1
        self.fleet_drop_speed = 7
        # fleet_direction为1表示向右移, 为-1表示向左移
        self.fleet_direction = 1
        self.alien_rate = 1
        self.alien_rate_multi = 2

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 外星人分数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # self.ship_speed = 0.5
        self.bullet_speed = 0.8
        self.bullet_width = 8
        self.bullets_allowed = 3
        self.alien_speed = 0.1
        self.alien_rate = 1
        # fleet_direction为1表示向右移, 为-1表示向左移
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50

    def increase_speed(self):
        # self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        # self.bullet_width *= (self.speedup_scale * 1.5)
        self.bullets_allowed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        if self.alien_rate <= 7:
            self.alien_rate = int(self.alien_rate * 2)
        # print(self.alien_points)
