import pygame, random  # 匯入Pygame和random模組

class Alien(pygame.sprite.Sprite):  # 定義Alien類別，繼承自Pygame的Sprite類
    def __init__(self, type, x, y):  # 初始化Alien物件
        super().__init__()  # 呼叫父類別的初始化方法
        self.type = type  # 設定外星人類型
        path = f"Graphics/alien_{type}.png"  # 設定圖片路徑
        self.image = pygame.image.load(path)  # 載入圖片
        self.rect = self.image.get_rect(topleft=(x, y))  # 設定圖片的初始位置

    def update(self, direction):  # 更新外星人位置
        self.rect.x += direction  # 根據方向移動外星人


class MysteryShip(pygame.sprite.Sprite):  # 定義MysteryShip類別，繼承自Pygame的Sprite類
    def __init__(self, screen_width, offset):  # 初始化MysteryShip物件
        super().__init__()  # 呼叫父類別的初始化方法
        self.screen_width = screen_width  # 設定螢幕寬度
        self.offset = offset  # 設定偏移量
        self.image = pygame.image.load("Graphics/mystery.png")  # 載入神秘飛船圖像

        # 隨機選擇初始位置
        x = random.choice([self.offset/2, self.screen_width + self.offset - self.image.get_width()])
        
        # 根據初始位置確定速度
        if x == self.offset/2:
            self.speed = 3
        else:
            self.speed = -3

        self.rect = self.image.get_rect(topleft=(x, 90))  # 設定圖像的初始位置

    def update(self):  # 更新神秘飛船位置
        self.rect.x += self.speed  # 根據速度移動飛船

        # 如果飛船超出螢幕邊界，則移除飛船
        if self.rect.right > self.screen_width + self.offset/2:
            self.kill()
        elif self.rect.left < self.offset/2:
            self.kill()  # 移除飛船

