import pygame
from Colors import *


class Square:

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.value = 0
        self.new = False

    #отображаем квадрат определенного цвета
    def show(self, w, screen):

        x = self.i * w
        y = self.j * w
        rect = pygame.Rect(x, y, w, w)  #определение границ объекта
        pygame.draw.rect(screen, BG, rect) #заливаем объект
        if self.new:
            if self.value > 0:
                #заливаем облость ячейки если она новая и не пустая)
                #rect.inflate(10, 10)
                pygame.draw.rect(screen, SqrColors[self.value], rect)
            self.new = False
        else:
            if self.value > 0:
                pygame.draw.rect(screen, SqrColors[self.value], rect)
            pygame.draw.rect(screen, BORDER, rect, 10)

    #Вывести на экран значение ячейки
    def display_value(self, screen, font, w):
        #цвет текст
        if self.value > 0:
            textsurface = font.render(str(self.value), True, TEXT_COLOR1)
            if self.value > 4:
                textsurface = font.render(str(self.value), True, TEXT_COLOR2)
            #размещение текста внутри ячейки
            text_rect = textsurface.get_rect(center=(w * self.i + 1 // 2 + 50, w * self.j + 1 // 2 + 50))
            screen.blit(textsurface, text_rect)


    #Поиск индекса ячейки в векторе на основе заданных параметров
    def search_index(self, i, j, grid):

        for square in range(len(grid)):
            if grid[square].i == i and grid[square].j == j:
                return square
        return -1

    #Объединение ячеек
    def move(self, grid, move_dir):

        index = self.search_index(self.i + move_dir[0], self.j + move_dir[1], grid)
        if index >= 0:
            cell = grid[index] #крайняя
            # Проверка возможности объединения с крайней(если ячейки не новые и их значения равны)
            if self.value == cell.value and cell.value != 0 and not self.new:
                cell.value *= 2
                cell.new = True
                self.value = 0
                pygame.mixer.music.play()
                return True, cell.value
            # Перемещение ячейки
            elif cell.value == 0:
                cell.value = self.value
                self.value = 0
                if cell.value == 0:
                    return False, 0
                return True, 0
        return False, 0