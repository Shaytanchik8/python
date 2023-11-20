import pygame

pygame.init()
pygame.mixer.init()
pygame.display.init()
pygame.font.init()

from Square import *
import random


class Game:
    def __init__(self):
        self.width = 400  #ширина
        self.height = 500  #высота
        self.w = 100
        self.fps = 15
        self.screen = pygame.display.set_mode((self.width, self.height)) #дисплей
        self.logo = pygame.image.load('assets/Logo.ico')  #лого
        self.font_38 = pygame.font.Font('assets/ClearSans.ttf', 38)   #шрифт SCOPE
        self.font_24 = pygame.font.Font('assets/ClearSans.ttf', 24) #шрифт квадратов
        self.clak = pygame.mixer.music.load('assets/clak.wav')  #звук на передвичжение
        self.grid = []  #матрица
        self.score = 0  #счёт
        self.highscore = 0
        self.lost = False

        pygame.display.set_caption('1024 in python')
        pygame.display.set_icon(self.logo)

    def run(self):
        self.create_grid()
        self.random2()
        self.random2()
        clock = pygame.time.Clock()
        run = True
        while run:
            moved_list = []  # Vector of booleans that
            clock.tick(self.fps)
            # TODO implement highscore
            score_text = self.font_38.render('Score:', True, TEXT_COLOR1)
            points_text = self.font_38.render(str(self.score), True, TEXT_COLOR1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if not self.lost:

                    # нажатие кнопки вниз и 4 варианта действия:
                    # 1. вверх
                    # 2. вправо
                    # 3. вниз
                    # 4. влево

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            for line in range(3):  # зацикливается 2 раза
                                for square in range(len(self.grid)):
                                    # Направление движения, move_dir[0] == col, move_dir[1] == row
                                    move_dir = (0, -1)

                                    # Если действительно ячейка переместилась, то в качестве возвращаемого значения получаем True
                                    moved, points = self.grid[square].move(self.grid, move_dir)
                                    moved_list.append(moved)

                                    # обновляем счет на ячейке
                                    self.score += points

                            # Только если переместили ячейки можно добавлять новый элемент 2
                            if True in moved_list:
                                self.random2()

                            # При каждом нажатии проверяем, не проиграли ли.
                            self.check_lost()

                        elif event.key == pygame.K_RIGHT:
                            for line in range(3):
                                for square in range(len(self.grid) - 1, -1, -1):
                                    move_dir = (1, 0)
                                    moved, points = self.grid[square].move(self.grid, move_dir)
                                    moved_list.append(moved)
                                    self.score += points

                            if True in moved_list:
                                self.random2()
                            self.check_lost()

                        elif event.key == pygame.K_DOWN:
                            for line in range(3):
                                for square in range(len(self.grid) - 1, -1, -1):
                                    move_dir = (0, 1)
                                    moved, points = self.grid[square].move(self.grid, move_dir)
                                    moved_list.append(moved)
                                    self.score += points

                            if True in moved_list:
                                self.random2()
                            self.check_lost()

                        elif event.key == pygame.K_LEFT:
                            for line in range(3):
                                for square in range(len(self.grid)):
                                    move_dir = (-1, 0)
                                    moved, points = self.grid[square].move(self.grid, move_dir)
                                    moved_list.append(moved)
                                    self.score += points

                            if True in moved_list:
                                self.random2()
                            self.check_lost()
                else:
                    # Если текущая игра проиграна, то появляется экран, на котором проверяется нажатие кнопки повтора.
                    mouse_pressed = pygame.mouse.get_pressed()
                    pos = pygame.mouse.get_pos()
                    left_click = mouse_pressed[0]

                    if left_click == 1:
                        if 142 < pos[0] < 262:
                            if 230 < pos[1] < 270:
                                self.restart()

            self.update(score_text, points_text)
        pygame.quit()

    #Обновляет игровую сетку
    def update(self, score_text, points_text):

        self.screen.fill((255, 255, 255))

        # Отображение всей сетки
        for i in range(len(self.grid)):
            self.grid[i].show(self.w, self.screen)
            self.grid[i].display_value(self.screen, self.font_38, self.w)

        if self.lost:
            # Создание проигрышного экрана
            transp_fg = pygame.Surface((400, 400))
            transp_fg.fill((240, 192, 0))
            transp_fg.set_alpha(128)

            # Проигрышный текст
            lost_text = self.font_38.render('You Lost', True, TEXT_COLOR2)
            lost_text_rect = lost_text.get_rect(center=(400 // 2, 400 // 2 - 30))

            # Повторная игра - значок
            retry_rect = pygame.Rect(400 // 2 - 57, 400 // 2 + 30, 120, 40)
            retry_text = self.font_24.render('Retry', True, TEXT_COLOR2)
            retry_text_rect = retry_text.get_rect(center=(400 // 2 + 4, 400 // 2 + 48))


            self.screen.blit(transp_fg, (0, 0))
            self.screen.blit(lost_text, lost_text_rect)
            pygame.draw.rect(self.screen, TEXT_COLOR1, retry_rect)
            self.screen.blit(retry_text, retry_text_rect)

        self.screen.blit(self.logo, (335, 435))
        self.screen.blit(score_text, (30, 425))
        self.screen.blit(points_text, (150, 425))

        pygame.display.flip()


 #Создаем игровое поле-сетку
    def create_grid(self):

        for i in range(4):
            for j in range(4):
                square = Square(i, j)  #рисуем квадраты
                self.grid.append(square)  #добавляем квадраты в поле-сетку

    #добавляем 2 в рандомную клетку
    def random2(self):

        tries = 0
        found = 0
        while found == 0 and tries < 1000:
            i = int(random.randrange(0, 4))
            j = int(random.randrange(0, 4))
            for cell in range(len(self.grid)):
                if self.grid[cell].i == i and self.grid[cell].j == j and self.grid[cell].value == 0:
                    found = 1
                    self.grid[cell].value = 2
                    self.grid[cell].new = True
                else:
                    tries += 1

    #Проверяет, не проиграл ли игрок
    def check_lost(self):
        filled_cells = 0
        for square in range(len(self.grid)):
            if self.grid[square].value > 0:
                filled_cells += 1
            if filled_cells == 16:
                self.lost = True

    #Новая игра
    def restart(self):
        self.grid = []
        self.lost = False
        self.score = 0
        self.create_grid()
        self.random2()
        self.random2()


game = Game()
game.run()