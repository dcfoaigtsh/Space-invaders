import pygame, random  # 匯入Pygame和random模組
from spaceship import Spaceship  # 從spaceship模組匯入Spaceship類
from obstacle import Obstacle  # 從obstacle模組匯入Obstacle類
from obstacle import grid  # 從obstacle模組匯入grid
from alien import Alien  # 從alien模組匯入Alien類
from laser import Laser  # 從laser模組匯入Laser類
from alien import MysteryShip  # 從alien模組匯入MysteryShip類

class Game:
	def __init__(self, screen_width, screen_height, offset): # 初始化Game物件
		self.screen_width = screen_width # 設定螢幕寬度
		self.screen_height = screen_height # 設定螢幕高度
		self.offset = offset # 設定偏移量
		self.spaceship_group = pygame.sprite.GroupSingle() # 創建單個飛船群組
		self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height, self.offset)) # 增加Spaceship實例到群組
		self.obstacles = self.create_obstacles() # 創建障礙物
		self.aliens_group = pygame.sprite.Group() # 創建外星人群組
		self.create_aliens() # 創建外星人
		self.level = 1  # 初始關卡設置為1
		self.aliens_direction = 1 # 設定外星人移動方向
		self.alien_lasers_group = pygame.sprite.Group() # 創建外星人激光群組
		self.mystery_ship_group = pygame.sprite.GroupSingle() # 創建單個神秘飛船群組
		self.lives = 3 # 設定初始生命值
		self.run = True # 設定遊戲運行狀態
		self.score = 0 # 設定初始分數
		self.highscore = 0 # 設定初始最高分數
		self.explosion_sound = pygame.mixer.Sound("Sounds/explosion.ogg") # 載入爆炸音效
		self.load_highscore() # 載入最高分數
		
		
	def create_obstacles(self): # 創建障礙物
		obstacle_width = len(grid[0]) * 3 # 計算障礙物寬度
		gap = (self.screen_width + self.offset - (4 * obstacle_width))/5 # 計算障礙物之間的間距
		obstacles = [] # 初始化障礙物列表
		for i in range(4): # 創建4個障礙物
			offset_x = (i + 1) * gap + i * obstacle_width # 計算每個障礙物的X軸偏移量
			obstacle = Obstacle(offset_x, self.screen_height - 100) # 創建Obstacle實例
			obstacles.append(obstacle) # 將Obstacle實例加入列表
		return obstacles # 返回障礙物列表

	def create_aliens(self, level=1): # 創建外星人
		if level == 1:
			for row in range(5): # 創建5行外星人
				for column in range(11): # 每行創建11個外星人
					x = 75 + column * 55 # 計算每個外星人的X軸位置
					y = 110 + row * 55 # 計算每個外星人的Y軸位置

					if row == 0: # 第一行外星人類型為3
						alien_type = 6
					elif row in (1, 2): # 第二、三行外星人類型為2
						alien_type = 5
					else: # 第四、五行外星人類型為1
						alien_type = 4

					alien = Alien(alien_type, x + self.offset/2, y) # 創建Alien實例
					self.aliens_group.add(alien) # 將Alien實例加入群組
		elif level == 2:
			max_columns = 11  # 最大列數
			for row in range(6): # 創建5行外星人
				# 計算當前行的外星人數
				num_aliens_in_row = max_columns - row * 2
				start_x = 75 + row * 55  # 計算當前行的起始X軸位置
				for column in range(num_aliens_in_row):
					x = start_x + column * 55  # 計算每個外星人的X軸位置
					y = 110 + row * 55  # 計算每個外星人的Y軸位置

					if row == 0: # 第一行外星人類型為3
						alien_type = 7
					elif row == 1: # 第二行外星人類型為3
						alien_type = 8
					elif row == 2: # 第三行外星人類型為2
						alien_type = 9
					elif row == 3: # 第四行外星人類型為2
						alien_type = 10
					else: # 第五行外星人類型為1
						alien_type = 11

					alien = Alien(alien_type, x + self.offset/2, y) # 創建Alien實例
					self.aliens_group.add(alien) # 將Alien實例加入群組
		elif level == 3:
			rows = 3  # 行數
			columns = 11  # 每行外星人數量
			staggered_offset = 30  # 每行的交錯偏移量

			for row in range(rows): # 創建5行外星人
				for column in range(columns): # 每行創建11個外星人
					x = 75 + column * 55  # 計算每個外星人的X軸位置
					y = 110 + row * 55  # 計算每個外星人的Y軸位置

					# 每行外星人位置交錯
					if row % 2 == 0:
						x += staggered_offset

					if row == 0: # 第一行外星人類型為3
						alien_type = 2
					elif row == 1: # 第二行外星人類型為2
						alien_type = 1
					else: # 第三行外星人類型為1
						alien_type = 3

					alien = Alien(alien_type, x + self.offset/2, y) # 創建Alien實例
					self.aliens_group.add(alien) # 將Alien實例加入群組
	#第一關通關
	def level_1_completed(self): 
		self.create_aliens(2)
	
	#第二關通關
	def level_2_completed(self):
		self.create_aliens(3)
		
	# def level_3_completed(self):
	# 	self.create_aliens(4)

	def move_aliens(self): # 移動外星人
		self.aliens_group.update(self.aliens_direction) # 根據方向更新外星人位置

		alien_sprites = self.aliens_group.sprites() # 獲取所有外星人精靈
		for alien in alien_sprites: # 遍歷每個外星人
			if alien.rect.right >= self.screen_width + self.offset/2: # 如果外星人到達右邊界
				self.aliens_direction = -1 # 改變移動方向為左
				self.alien_move_down(4) # 外星人向下移動
			elif alien.rect.left <= self.offset/2: # 如果外星人到達左邊界
				self.aliens_direction = 1 # 改變移動方向為右
				self.alien_move_down(4) # 外星人向下移動

	def alien_move_down(self, distance):  # 外星人向下移動
		if self.aliens_group: # 如果外星人群組非空
			for alien in self.aliens_group.sprites(): # 遍歷每個外星人
				alien.rect.y += distance*2 # 向下移動指定距離

	def alien_shoot_laser(self): # 外星人射擊激光
		if self.aliens_group.sprites(): # 如果外星人群組非空
			random_alien = random.choice(self.aliens_group.sprites()) # 隨機選擇一個外星人
			laser_sprite = Laser(random_alien.rect.center, -6, self.screen_height)  # 創建Laser實例
			self.alien_lasers_group.add(laser_sprite) # 將Laser實例加入群組

	def create_mystery_ship(self):  # 創建神秘飛船
		self.mystery_ship_group.add(MysteryShip(self.screen_width, self.offset))    # 創建MysteryShip實例並加入群組
		
	def check_for_collisions(self): # 檢查碰撞
		victory = False
		#Spaceship
		if self.spaceship_group.sprite.lasers_group: # 如果飛船激光群組非空
			for laser_sprite in self.spaceship_group.sprite.lasers_group:   # 遍歷每個激光
				aliens_hit = pygame.sprite.spritecollide(laser_sprite, self.aliens_group, True) # 檢查激光是否擊中外星人
				if aliens_hit: # 如果有外星人被擊中
					self.explosion_sound.play() # 播放爆炸音效
					for alien in aliens_hit: # 遍歷每個被擊中的外星人
						self.score += alien.type * 100 # 根據外星人類型增加分數
						self.check_for_highscore()  # 檢查是否為最高分
						laser_sprite.kill() # 刪除擊中的激光

				if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True): # 檢查激光是否擊中神秘飛船
					self.score += 500 # 增加500分
					self.explosion_sound.play() # 播放爆炸音效
					self.check_for_highscore()  # 檢查是否為最高分
					laser_sprite.kill() # 刪除擊中的激光

				for obstacle in self.obstacles: # 遍歷所有障礙物
					if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):  # 檢查激光是否擊中障礙物
						laser_sprite.kill() # 刪除擊中的激光

		#Alien Lasers
		if self.alien_lasers_group: # 如果外星人激光群組非空
			for laser_sprite in self.alien_lasers_group:  # 遍歷每個外星人激光
				if pygame.sprite.spritecollide(laser_sprite, self.spaceship_group, False): # 檢查外星人激光是否擊中飛船
					laser_sprite.kill() # 刪除擊中的激光
					self.lives -= 1 # 減少生命值
					if self.lives == 0: # 如果生命值為0
						self.game_over() # 遊戲結束

				for obstacle in self.obstacles: # 遍歷所有障礙物
					if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True): # 檢查激光是否擊中障礙物
						laser_sprite.kill() # 刪除擊中的激光

		if self.aliens_group: # 如果外星人群組非空
			for alien in self.aliens_group: # 遍歷每個外星人
				for obstacle in self.obstacles: # 遍歷所有障礙物
					pygame.sprite.spritecollide(alien, obstacle.blocks_group, True) # 檢查外星人是否撞到障礙物
				if pygame.sprite.spritecollide(alien, self.spaceship_group, False):  #檢查外星人是否撞到飛船
					self.game_over() # 遊戲結束
		else:
			victory = True		
			return victory	

	def game_over(self): # 遊戲結束
		self.run = False # 設定遊戲運行狀態為False


	def reset(self): # 重置遊戲
		self.run = True # 設定遊戲運行狀拋為True
		self.victory = False
		self.lives = 3 # 重置生命值
		self.spaceship_group.sprite.reset() # 重置飛船位置
		self.aliens_group.empty() # 清空外星人群組
		self.alien_lasers_group.empty() # 清空外星人激光群組
		self.create_aliens() # 創建外星人
		self.mystery_ship_group.empty() # 清空神秘飛船群組
		self.obstacles = self.create_obstacles() # 重置障礙物
		self.score = 0 # 重置分數

	def check_for_highscore(self): # 檢查是否為最高分
		if self.score > self.highscore: # 如果分數大於最高分
			self.highscore = self.score # 更新最高分

			with open("highscore.txt", "w") as file: # 寫入最高分到文件
				file.write(str(self.highscore)) # 寫入最高分

	def load_highscore(self): # 載入最高分
		try: # 嘗試讀取最高分
			with open("highscore.txt", "r") as file: # 從文件讀取最高分
				self.highscore = int(file.read()) # 將讀取的最高分轉換為整數
		except FileNotFoundError: # 如果文件不存在
			self.highscore = 0 # 最高分為0
	
	def show_level_victory(self, message): # 顯示關卡勝利
		self.display_message(message) # 顯示消息
		pygame.time.wait(1500)  # 暫停1.5秒
	
	def display_message(self, message): # 顯示消息
		font = pygame.font.Font(None, 74) # 設置字體
		text = font.render(message, True, (255, 255, 255)) # 渲染消息
		text_rect = text.get_rect(center=(self.screen_width / 2, self.screen_height / 2)) # 設置消息位置
		screen = pygame.display.get_surface() # 獲取螢幕
		screen.blit(text, text_rect) # 顯示消息
		pygame.display.flip() # 更新螢幕

	