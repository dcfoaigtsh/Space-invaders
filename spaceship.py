import pygame  # 匯入Pygame模組
from laser import Laser  # 從laser模組匯入Laser類

class Spaceship(pygame.sprite.Sprite):  # 定義Spaceship類，繼承自pygame.sprite.Sprite
    def __init__(self, screen_width, screen_height, offset):  # 初始化Spaceship物件
        super().__init__()  # 呼叫父類的初始化方法
        self.offset = offset  # 設定偏移量
        self.screen_width = screen_width  # 設定螢幕寬度
        self.screen_height = screen_height  # 設定螢幕高度
        self.image = pygame.image.load("Graphics/spaceship.png")  # 加載飛船圖片
        self.rect = self.image.get_rect(midbottom=((self.screen_width + self.offset) / 2, self.screen_height))  # 設定飛船初始位置
        self.speed = 6  # 設定飛船移動速度
        self.lasers_group = pygame.sprite.Group()  # 創建激光群組
        self.laser_ready = True  # 設定激光是否可以發射
        self.laser_time = 0  # 設定激光發射時間
        self.laser_delay = 200  # 設定激光發射間隔時間（毫秒）
        self.laser_sound = pygame.mixer.Sound("Sounds/laser.wav")  # 加載激光聲音

    def get_user_input(self):  # 處理使用者輸入
        keys = pygame.key.get_pressed()  # 獲取鍵盤按鍵狀態

        if keys[pygame.K_RIGHT]:  # 如果按下右方向鍵
            self.rect.x += self.speed  # 向右移動飛船

        if keys[pygame.K_LEFT]:  # 如果按下左方向鍵
            self.rect.x -= self.speed  # 向左移動飛船

        if keys[pygame.K_SPACE] and self.laser_ready:  # 如果按下空格鍵並且激光可以發射
            self.laser_ready = False  # 設定激光不可發射
            laser = Laser(self.rect.center, 5, self.screen_height)  # 創建激光物件
            self.lasers_group.add(laser)  # 將激光加入群組
            self.laser_time = pygame.time.get_ticks()  # 記錄發射激光的時間
            self.laser_sound.play()  # 播放激光聲音

    def update(self):  # 更新飛船狀態
        self.get_user_input()  # 獲取使用者輸入
        self.constrain_movement()  # 限制飛船移動範圍
        self.lasers_group.update()  # 更新激光群組
        self.recharge_laser()  # 重新充能激光

    def constrain_movement(self):  # 限制飛船移動範圍
        if self.rect.right > self.screen_width:  # 如果飛船超出右邊界
            self.rect.right = self.screen_width  # 設定飛船在右邊界
        if self.rect.left < self.offset:  # 如果飛船超出左邊界
            self.rect.left = self.offset  # 設定飛船在左邊界

    def recharge_laser(self):  # 重新充能激光
        if not self.laser_ready:  # 如果激光不可發射
            current_time = pygame.time.get_ticks()  # 獲取當前時間
            if current_time - self.laser_time >= self.laser_delay:  # 如果超過發射間隔時間
                self.laser_ready = True  # 設定激光可以發射

    def reset(self):  # 重置飛船狀態
        self.rect = self.image.get_rect(midbottom=((self.screen_width + self.offset) / 2, self.screen_height))  # 重置飛船位置
        self.lasers_group.empty()  # 清空激光群組
