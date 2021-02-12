import pygame
import os
import sys
import requests



map_request = "https://static-maps.yandex.ru/1.x/?ll=132.704839,-25.479124&spn=25.457,20.9&l=sat"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)


pygame.init()

size = width, height = 600, 450

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Австралия")
screen.blit(pygame.image.load(map_file), (0, 0))

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
