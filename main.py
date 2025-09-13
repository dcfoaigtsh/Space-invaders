import pygame, sys, random  # 匯入Pygame、sys和random模組
from game import Game  # 從game模組匯入Game類別

pygame.init()  # 初始化Pygame

# 設定螢幕寬度和高度以及偏移量
SCREEN_WIDTH = 750  # 螢幕寬度設為750像素
SCREEN_HEIGHT = 700  # 螢幕高度設為700像素
OFFSET = 50  # 偏移量設為50像素

# 定義顏色
GREY = (29, 29, 27)  # 定義灰色的RGB值
BLUE = (0, 255, 255)  # 定義藍色的RGB值

# 載入字體並渲染文字
font = pygame.font.Font("Font/monogram.ttf", 40)  # 使用指定字體和大小
large_font = pygame.font.Font("Font/monogram.ttf", 80)  # 使用指定字體和大小
large_font2 = pygame.font.Font("Font/monogram.ttf", 100)  # 使用指定字體和大小
level_surface = font.render("LEVEL 01", False, BLUE)  # 渲染"LEVEL 01"文字
game_over_surface = font.render("GAME OVER", False, BLUE)  # 渲染"GAME OVER"文字
score_text_surface = font.render("SCORE", False, BLUE)  # 渲染"SCORE"文字
highscore_text_surface = font.render("HIGH-SCORE", False, BLUE)  # 渲染"HIGH-SCORE"文字
pause_surface = large_font2.render("PAUSE", False, BLUE) # 渲染"PAUSE"文字

# 設定螢幕顯示模式
screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))  # 設定螢幕大小並創建螢幕物件
pygame.display.set_caption("Python Space Invaders")  # 設定螢幕標題

clock = pygame.time.Clock()  # 初始化時鐘物件

# 創建遊戲物件
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)  # 創建Game類別的實例

# 自定義事件
SHOOT_LASER = pygame.USEREVENT  # 定義射擊激光事件
pygame.time.set_timer(SHOOT_LASER, 300)  # 每300毫秒觸發一次射擊事件

MYSTERYSHIP = pygame.USEREVENT + 1  # 定義神秘飛船事件
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 6000))  # 隨機時間觸發神秘飛船事件

pausebutton = pygame.image.load("Graphics/pause.png") # 載入暫停圖片
pausebutton = pygame.transform.scale(pausebutton, (40, 40))  # 調整暫停圖片大小
pausebutton_rect = pausebutton.get_rect() # 獲取暫停圖片矩形
pausebutton_rect.center = (400, SCREEN_HEIGHT + OFFSET + 10) # 調整按鈕位置
playbutton = pygame.image.load("Graphics/play.png") # 載入播放圖片
playbutton = pygame.transform.scale(playbutton, (40, 40)) # 調整播放圖片大小
playbutton_rect = playbutton.get_rect() # 獲取播放圖片矩形
playbutton_rect.center = (350, SCREEN_HEIGHT + OFFSET + 10 )  # 調整按鈕位置

pause = False # 設定遊戲暫停狀態
left_mouse_down = False # 設定滑鼠左鍵按下狀態
p_pressing = False  # 設定P鍵按下狀態
   
def draw_text(text, font, text_col, x, y): # 繪製文字函數
    img = font.render(text, True, text_col) # 渲染文字
    screen.blit(img, (x, y))  # 繪製文字

bgm1 = pygame.mixer.Sound("Sounds/music.ogg")
bgm2 = pygame.mixer.Sound("Sounds/music.wav")

def play_bgm(bgm):
    pygame.mixer.stop()
    pygame.mixer.music.set_volume(0.3)
    bgm.play(loops=-1) 

#第一關通關轉場
def Level_1_clear():
    clear_surface = large_font.render("Level 1 Clear", False, BLUE)  # 渲染"Level 1 Clear"文字
    screen.fill(GREY) # 填充背景色為灰色
    screen.blit(clear_surface, (SCREEN_WIDTH // 2 - clear_surface.get_width() // 2, 
                                SCREEN_HEIGHT // 2)) # 繪製"Level 1 Clear"文字
    pygame.display.update() # 更新顯示內容

    pygame.time.wait(1000)  # 等待1秒

    level_2_surface = large_font.render("Level 2", False, BLUE)  # 渲染"Level 2"文字
    screen.fill(GREY) # 填充背景色為灰色
    screen.blit(level_2_surface, (SCREEN_WIDTH // 2 - level_2_surface.get_width() // 2, 
                                  SCREEN_HEIGHT // 2)) # 繪製"Level 2"文字
    
    pygame.time.wait(1000)  # 等待1秒

    countdown = 3 # 設定倒數計時為3
    last_count = pygame.time.get_ticks() # 獲取當前時間
    run_countdown = True # 設定倒數計時運行狀態為True

    while run_countdown:  # 當倒數計時運行狀態為True
        for event in pygame.event.get(): # 遍歷所有事件
            if event.type == pygame.QUIT: # 點擊關閉按鈕事件
                pygame.quit() # 退出Pygame
                sys.exit()  # 結束程式

        current_time = pygame.time.get_ticks() # 獲取當前時間

        if current_time - last_count >= 1000: # 若當前時間減去上次計時時間大於等於1秒
            countdown -= 1 # 倒數減1
            last_count = current_time # 更新上次計時時間

        if countdown > 0: # 若倒數計時大於0
            pygame.draw.rect(screen, GREY, (SCREEN_WIDTH // 2 - 10, SCREEN_HEIGHT // 2 + 200, 200, 50)) # 繪製灰色矩形
            draw_text('GET READY!', font, (255, 255, 255), int(SCREEN_WIDTH / 2 - 80), 
                      int(SCREEN_HEIGHT / 2 + 150)) # 繪製"GET READY!"文字
            draw_text(str(countdown), font, (255, 255, 255), int(SCREEN_WIDTH / 2 - 10), 
                      int(SCREEN_HEIGHT / 2 + 200)) # 繪製倒數計時文字
        else: 
            run_countdown = False # 倒數計時運行狀態設定為False
        pygame.display.update() # 更新顯示內容
        clock.tick(60) # 設定每秒幀數為60

#第二關通關轉場
def Level_2_clear():
    clear_surface = large_font.render("Level 2 Clear", False, BLUE)  # 渲染"Level 1 Clear"文字
    screen.fill(GREY) # 填充背景色為灰色
    screen.blit(clear_surface, (SCREEN_WIDTH // 2 - clear_surface.get_width() // 2, 
                                SCREEN_HEIGHT // 2)) # 繪製"Level 1 Clear"文字
    pygame.display.update() # 更新顯示內容

    pygame.time.wait(1000)  # 等待1秒

    level_2_surface = large_font.render("Level 3", False, BLUE)  # 渲染"Level 2"文字
    screen.fill(GREY) # 填充背景色為灰色
    screen.blit(level_2_surface, (SCREEN_WIDTH // 2 - level_2_surface.get_width() // 2, 
                                  SCREEN_HEIGHT // 2)) # 繪製"Level 2"文字
    
    pygame.time.wait(1000)  # 等待1秒
    countdown = 3 # 設定倒數計時為3
    last_count = pygame.time.get_ticks() # 獲取當前時間
    run_countdown = True # 設定倒數計時運行狀態為True 

    while run_countdown: # 當倒數計時運行狀態為True
        for event in pygame.event.get(): # 遍歷所有事件
            if event.type == pygame.QUIT: # 點擊關閉按鈕事件
                pygame.quit()   # 退出Pygame
                sys.exit() # 結束程式

        current_time = pygame.time.get_ticks() # 獲取當前時間

        if current_time - last_count >= 1000: # 若當前時間減去上次計時時間大於等於1秒
            countdown -= 1 # 倒數減1
            last_count = current_time # 更新上次計時時間

        if countdown > 0:
            pygame.draw.rect(screen, GREY, (SCREEN_WIDTH // 2 - 10, SCREEN_HEIGHT // 2 + 200, 200, 50))
            draw_text('GET READY!', font, (255, 255, 255), int(SCREEN_WIDTH / 2 - 80), 
                      int(SCREEN_HEIGHT / 2 + 150)) # 繪製"GET READY!"文字
            draw_text(str(countdown), font, (255, 255, 255), int(SCREEN_WIDTH / 2 - 10), 
                      int(SCREEN_HEIGHT / 2 + 200)) # 繪製倒數計時文字
        else:
            run_countdown = False # 倒數計時運行狀態設定為False
        pygame.display.update() # 更新顯示內容
        clock.tick(60)  # 設定每秒幀數為60             

#主遊戲迴圈
def main():
    game.victory = False # 設定勝利狀態為False
    global pause, left_mouse_down, p_pressing # 宣告全局變數
    level = 1  # 設定關卡為1
    level_surface = font.render(f"LEVEL {level}", False, BLUE) # 渲染關卡文字
    play_bgm(bgm2)
    pygame.mixer.music.set_volume(0.3)

    while True:
        current_time = pygame.time.get_ticks() # 獲取當前時間

        # 檢查事件
        for event in pygame.event.get():  # 遍歷所有事件
            if event.type == pygame.QUIT:  # 點擊關閉按鈕事件
                pygame.quit()  # 退出Pygame
                sys.exit()  # 結束程式
            if event.type == SHOOT_LASER and game.run and not pause:  # 外星人射擊激光事件且遊戲運行中
                game.alien_shoot_laser()  # 呼叫外星人射擊激光函數
            if event.type == MYSTERYSHIP and game.run and not pause:  # 創建神秘飛船事件且遊戲運行中
                game.create_mystery_ship()  # 呼叫創建神秘飛船函數
                pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 6000))  # 重設神秘飛船事件計時器
            if event.type == pygame.MOUSEBUTTONDOWN: # 滑鼠按下事件
                if pausebutton_rect.collidepoint(event.pos): # 檢查按下的是否是"pause"按鈕
                    pause = True # 設定暫停狀態為True
                elif playbutton_rect.collidepoint(event.pos): # 檢查按下的是否是"play"按鈕
                    pause = False # 設定暫停狀態為False
                if event.button == 1: # 檢查是否是滑鼠左鍵按下事件
                    left_mouse_down = True  # 設定滑鼠左鍵按下狀態為True
            elif event.type == pygame.MOUSEBUTTONUP: # 滑鼠放開事件
                if event.button == 1: # 檢查是否是滑鼠左鍵放開事件
                    left_mouse_down = False # 設定滑鼠左鍵按下狀態為False
            
            # 檢查鍵盤按鍵
            keys = pygame.key.get_pressed()  # 獲取所有按鍵的狀態
            if keys[pygame.K_r] and not game.run:  # 按下R鍵且遊戲未運行
                game.reset()  # 重置遊戲
                level = 1  # 重置關卡
                level_surface = font.render(f"LEVEL {level}", False, BLUE) # 重新渲染關卡文字
            elif event.type == pygame.KEYDOWN: # 按下鍵盤事件
                if event.key == pygame.K_p: # 按下P鍵
                    p_pressing = True   # 設定P鍵按下狀態為True
                    pause = not pause  # 切換暫停/播放狀態


        # 更新遊戲狀態
        if game.run and not pause:  # 若遊戲正在運行
            game.spaceship_group.update()  # 更新飛船群組
            game.move_aliens()  # 移動外星人
            game.alien_lasers_group.update()  # 更新外星人激光群組
            game.mystery_ship_group.update()  # 更新神秘飛船群組
            game.check_for_collisions()  # 檢查碰撞

            if not game.aliens_group: # 如果外星人群組為空
                game.run = False # 設定遊戲運行狀態為False
                game.alien_lasers_group.empty()
                game.mystery_ship_group.empty()
                if level == 1:  # 如果是第一關
                    Level_1_clear()  # 顯示"Clear"並等待3秒
                    level += 1  # 進入下一關
                    game.spaceship_group.update()  # 更新飛船群組
                    game.move_aliens()  # 移動外星人
                    game.alien_lasers_group.update()  # 更新外星人激光群組
                    game.mystery_ship_group.update()  # 更新神秘飛船群組
                    game.check_for_collisions()  # 檢查碰撞
                    level_surface = font.render(f"LEVEL {level}", False, BLUE) # 重新渲染關卡文字
                    game.run = True  # 重新開始遊戲
                    game.level_1_completed()
                elif level == 2:  # 如果是第一關
                    Level_2_clear()  # 顯示"Clear"並等待3秒
                    level += 1  # 進入下一關
                    game.spaceship_group.update()  # 更新飛船群組
                    game.move_aliens()  # 移動外星人
                    game.alien_lasers_group.update()  # 更新外星人激光群組
                    game.mystery_ship_group.update()  # 更新神秘飛船群組
                    game.check_for_collisions()  # 檢查碰撞
                    level_surface = font.render(f"LEVEL {level}", False, BLUE) # 重新渲染關卡文字
                    game.run = True  # 重新開始遊戲
                    game.level_2_completed() # 顯示"Clear"並等待3秒
                else:  # 如果是第三關
                    game.victory = True  # 設定勝利狀態為True
                    game.run = False # 設定遊戲運行狀態為False

        # 繪製螢幕內容
        screen.fill(GREY)  # 填充背景色為灰色

        # 繪製UI
        pygame.draw.rect(screen, BLUE, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)  # 繪製黃色矩形邊框
        pygame.draw.line(screen, BLUE, (25, 730), (775, 730), 3)  # 繪製黃色分隔線

        if game.run:  # 若遊戲正在運行
            screen.blit(level_surface, (570, 740, 50, 50))  # 繪製關卡文字

        if game.victory: # 若遊戲勝利
            if level == 1: # 若為第一關
                Level_1_clear() # 顯示"Clear"並等待3秒
                level += 1 # 進入下一關
                game.create_aliens(level) # 創建外星人
                game.run = True # 開始遊戲
                game.victory = False # 設定勝利狀態為False
            elif level == 2: # 若為第二關
                Level_2_clear() # 顯示"Clear"並等待3秒
                level += 1 # 進入下一關
                game.create_aliens(level) # 創建外星人
                game.run = True     # 開始遊戲
                game.victory = False # 設定勝利狀態為False
            else:
                victory_surface = large_font.render("YOU WIN!", False, BLUE)  # 渲染勝利文字
                screen.blit(victory_surface, (SCREEN_WIDTH // 2 - victory_surface.get_width() // 2, SCREEN_HEIGHT // 2))  # 繪製勝利文字
                if (current_time // 500) % 2 == 0:
                    Try_again_surface = font.render("Press R to try again", False, BLUE)
                    screen.blit(Try_again_surface, (SCREEN_WIDTH // 2 - Try_again_surface.get_width() // 2, SCREEN_HEIGHT // 2 + 70)) # 繪製再試一次文字  

        if not game.run and not game.victory:  # 若遊戲未運行
            screen.blit(game_over_surface, (570, 740, 50, 50))  # 繪製遊戲結束文字
            game.aliens_group.empty() # 清空外星人群組
            game.alien_lasers_group.empty()  # 清空外星人激光群組
            game.mystery_ship_group.empty() # 清空神秘飛船群組
            Lose_surface = large_font.render("You Lose...", False, BLUE)  # 渲染失敗文字
            screen.blit(Lose_surface, (SCREEN_WIDTH // 2 - Lose_surface.get_width() // 2 + 10, SCREEN_HEIGHT // 2 ))  # 繪製失敗文字
            if (current_time // 500) % 2 == 0:
                Try_again_surface = font.render("Press R to try again", False, BLUE)  # 渲染再試一次文字
                screen.blit(Try_again_surface, (SCREEN_WIDTH // 2 - Try_again_surface.get_width() // 2, SCREEN_HEIGHT // 2 + 70))  # 繪製再試一次文字

        # 繪製剩餘生命
        x = 50  # 初始化X軸位置
        for life in range(game.lives):  # 遍歷剩餘生命數量
            screen.blit(game.spaceship_group.sprite.image, (x, 745))  # 繪製飛船圖片
            x += 50  # 每次繪製後X軸位置右移50像素

        # 繪製分數和最高分
        screen.blit(score_text_surface, (50, 15, 50, 50))  # 繪製"Score"文字
        formatted_score = str(game.score).zfill(5)  # 將分數格式化為5位數字
        score_surface = font.render(formatted_score, False, BLUE)  # 渲染分數
        screen.blit(score_surface, (50, 40, 50, 50))  # 繪製分數
        screen.blit(highscore_text_surface, (550, 15, 50, 50))  # 繪製"High-Score"文字
        formatted_highscore = str(game.highscore).zfill(5)  # 將最高分數格式化為5位數字
        highscore_surface = font.render(formatted_highscore, False, BLUE)  # 渲染最高分數
        screen.blit(highscore_surface, (625, 40, 50, 50))  # 繪製最高分數

        # 繪製遊戲物件
        game.spaceship_group.draw(screen)  # 繪製飛船群組
        game.spaceship_group.sprite.lasers_group.draw(screen)  # 繪製飛船發射的激光
        for obstacle in game.obstacles:  # 遍歷所有障礙物
            obstacle.blocks_group.draw(screen)  # 繪製障礙物群組
        game.aliens_group.draw(screen)  # 繪製外星人群組
        game.alien_lasers_group.draw(screen)  # 繪製外星人激光群組
        game.mystery_ship_group.draw(screen)  # 繪製神秘飛船群組

        screen.blit(pausebutton, pausebutton_rect) # 繪製暫停按鈕
        screen.blit(playbutton, playbutton_rect) # 繪製播放按鈕

        if pause: # 若遊戲暫停
            if (current_time // 500) % 2 == 0: # 每500毫秒切換一次
                screen.blit(pause_surface, (SCREEN_WIDTH // 2 - pause_surface.get_width() // 2,  
                                        SCREEN_HEIGHT // 2 - pause_surface.get_height() // 2)) # 繪製"PAUSE"文字


        pygame.display.update()  # 更新顯示內容
        clock.tick(60)  # 設定每秒幀數為60

#倒數計時並開始遊戲
def countdown_and_start(): 
    countdown = 3 # 設定倒數計時為3
    last_count = pygame.time.get_ticks() # 獲取當前時間
    run_countdown = True # 設定倒數計時運行狀態為True

    while run_countdown: # 當倒數計時運行狀態為True
        for event in pygame.event.get(): # 遍歷所有事件
            if event.type == pygame.QUIT: # 點擊關閉按鈕事件
                pygame.quit() # 退出Pygame
                sys.exit() # 結束程式

        current_time = pygame.time.get_ticks()  # 獲取當前時間
        screen.fill((0, 0, 0))  # 填充背景色為黑色 

        if current_time - last_count >= 1000: # 若當前時間減去上次計時時間大於等於1秒
            countdown -= 1 # 倒數減1
            last_count = current_time # 更新上次計時時間

        if countdown > 0:
            draw_text('GET READY!', font, (255, 255, 255), int(SCREEN_WIDTH / 2 - 80), int(SCREEN_HEIGHT / 2 + 50)) # 繪製"GET READY!"文字
            draw_text(str(countdown), font, (255, 255, 255), int(SCREEN_WIDTH / 2 - 10), int(SCREEN_HEIGHT / 2 + 100)) # 繪製倒數計時文字
        else:
            run_countdown = False # 倒數計時運行狀態設定為False
            main() # 開始遊戲
        pygame.display.update() # 更新顯示內容
        clock.tick(60) # 設定每秒幀數為60

def control():
    arrow_img = pygame.image.load("Graphics/arrow2.png")  # 載入箭頭圖片
    space_img = pygame.image.load("Graphics/space2.png")  # 載入空白圖片
    play_img = pygame.image.load("Graphics/play2.png")  # 載入播放圖片

    arrow_img = pygame.transform.scale(arrow_img, (200, 100))  # 調整箭頭圖片大小
    space_img = pygame.transform.scale(space_img, (200, 75))  # 調整空白圖片大小
    play_img = pygame.transform.scale(play_img, (200, 100))  # 調整播放圖片大小

    arrow_rect = arrow_img.get_rect(center=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 200))  # 設定箭頭位置
    space_rect = space_img.get_rect(center=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 ))  # 設定空白圖片位置
    play_rect = play_img.get_rect(center=(SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2 + 200))  # 設定播放圖片位置

    run_control = True # 設定操作說明運行狀態為True

    # 操作說明迴圈
    while run_control:
        for event in pygame.event.get(): # 遍歷所有事件
            if event.type == pygame.QUIT: # 點擊關閉按鈕事件
                pygame.quit() # 退出Pygame
                sys.exit() # 結束程式
            elif event.type == pygame.MOUSEBUTTONDOWN: # 滑鼠按下事件
                if play_rect.collidepoint(event.pos):  # 檢查按下的是否是"play2"按鈕
                    run_control = False  # 退出操作說明循環
                    countdown_and_start() # 開始倒數計時並開始遊戲

        screen.fill((0, 0, 0))  # 填充背景色為黑色

        # 顯示遊戲說明圖片
        screen.blit(arrow_img, arrow_rect) # 繪製箭頭圖片
        screen.blit(space_img, space_rect) # 繪製空白圖片
        screen.blit(play_img, play_rect) # 繪製播放圖片

        font = pygame.font.Font(None, 36) # 使用默認字體和大小
        arrow_text = font.render(": Control Spaceship", True, (255, 255, 255)) # 渲染"Control Spaceship"文字
        space_text = font.render(": Shoot", True, (255, 255, 255)) # 渲染"Shoot"文字
        screen.blit(arrow_text, (arrow_rect.centerx - arrow_text.get_width() // 2 + 300, arrow_rect.bottom - 50)) # 繪製"Control Spaceship"文字
        screen.blit(space_text, (space_rect.centerx - space_text.get_width() // 2 + 225, space_rect.bottom - 50)) # 繪製"Shoot"文字

        pygame.display.update() # 更新顯示內容
        clock.tick(60)  # 設定每秒幀數為60

#主選單
def main_menu():
    title_font = pygame.font.Font("Font/monogram.ttf", 60) # 使用指定字體和大小
    cover = pygame.image.load("Graphics/cover.png")  # 載入封面圖片
    cover = pygame.transform.scale(cover, (SCREEN_WIDTH + 50 , SCREEN_HEIGHT + 85))  # 調整封面圖片大小
    start_button = pygame.image.load("Graphics/start2.png")  # 載入開始按鈕圖片
    start_button = pygame.transform.scale(start_button, (200, 100))  # 調整按鈕大小
    start_button_rect = start_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250))  # 設定按鈕位置
    run = True # 設定主選單運行狀態為True   
    play_bgm(bgm1) # 播放背景音樂

    while run:
        screen.fill((0, 0, 0))  # 使用黑色背景
        screen.blit(cover, (0, 0))  # 繪製封面圖片
        current_time = pygame.time.get_ticks() # 獲取當前時間
        if (current_time // 500) % 2 == 0: # 每500毫秒切換一次
            title_label = title_font.render("Press the start to begin...", 1, (243, 216, 63)) # 渲染"Press the start to begin..."文字
            screen.blit(title_label, (SCREEN_WIDTH/2 - title_label.get_width()/2 + 10, 675)) # 繪製"Press the start to begin..."文字
        screen.blit(start_button, start_button_rect) # 繪製開始按鈕
        pygame.display.update() # 更新顯示內容
        for event in pygame.event.get(): # 遍歷所有事件
            if event.type == pygame.QUIT: # 點擊關閉按鈕事件
                run = False # 退出主選單循環
            if event.type == pygame.MOUSEBUTTONDOWN: # 滑鼠按下事件
                if start_button_rect.collidepoint(event.pos):  # 檢查按鈕是否被按下
                    run = False  # 退出主選單循環，進入遊戲
                    control() # 進入操作說明
                 
    pygame.quit() # 退出Pygame
    sys.exit() # 結束程式

main_menu()     # 進入主選單