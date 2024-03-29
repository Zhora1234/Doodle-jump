import pygame
import os
import sys

base_path = getattr(sys,"_MEIPASS",os.path.abspath(os.path.dirname("main.py")))

def get_path(*paths):
    path = os.path.join(base_path,*paths)
    return path

def load_image(*paths):
    """Загружает картинку"""
    # Получаем полный путь к картинке
    path = get_path(*paths)

    # Загружаем картинку и конвертируем её
    image = pygame.image.load(path).convert()
    # Делаем чёрный цвет прозрачным
    image.set_colorkey((0, 0, 0))

    # Возвращаем картинку из функции
    return image
