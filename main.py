import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")
FPS = 60

def tileBackground(screen: pygame.display, image: pygame.Surface) -> None:
    screenWidth, screenHeight = screen.get_size()
    imageWidth, imageHeight = image.get_size()
    
    # Calculate how many tiles we need to draw in x axis and y axis
    tilesX = math.ceil(screenWidth / imageWidth)
    tilesY = math.ceil(screenHeight / imageHeight)
    
    # Loop over both and blit accordingly
    for x in range(tilesX):
        for y in range(tilesY):
            screen.blit(image, (x * imageWidth, y * imageHeight))

def main():
    clock = pygame.time.Clock()
    run = True
    
    bg = pygame.image.load('backg.png')
    bg = pygame.transform.scale(bg, (400, 300))
    car_left = pygame.image.load('Player_left.png')
    car_left = pygame.transform.scale(car_left, (100, 100))
    car_right = pygame.image.load('Player_Right.png')
    car_right = pygame.transform.scale(car_right, (100, 100))
    while run:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        if len(keys) > 0:
            print(keys)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        tileBackground(win, bg)
        win.blit(car_left, (220, 500))
        win.blit(car_right, (620, 500))
        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
    
# 70, 220 and 470, 620