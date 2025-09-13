import pygame  # 匯入Pygame模組

class Laser(pygame.sprite.Sprite):  # 定義Laser類，繼承自pygame.sprite.Sprite
    def __init__(self, position, speed, screen_height):  # 初始化Laser物件
        super().__init__()  # 呼叫父類的初始化方法
        self.image = pygame.Surface((4, 15))  # 創建激光的表面，大小為4x15
        self.image.fill((243, 216, 63))  # 填充激光的顏色為黃色
        self.rect = self.image.get_rect(center=position)  # 設定激光的位置
        self.speed = speed  # 設定激光的速度
        self.screen_height = screen_height  # 設定螢幕高度

    def update(self):  # 更新激光位置
        self.rect.y -= self.speed  # 根據速度更新激光的Y軸位置
        if self.rect.y > self.screen_height + 15 or self.rect.y < 0:  # 如果激光超出螢幕範圍
            self.kill()  # 刪除激光

