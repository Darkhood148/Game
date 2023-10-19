import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")
FPS = 60
VEL = 10
obstacles = []

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
            
def render_obj(img, x, y):
    global win
    win.blit(img, (x,y))
    
def spawn_obstacle():
    im = pygame.image.load('Police.png')
    im = pygame.transform.scale(im, (100,100))
    pos = random.randint(0,3)
    xs = [70, 220, 470, 620]
    obstacles.append([im,xs[pos],0])

def main():
    clock = pygame.time.Clock()
    run = True
    
    bg = pygame.image.load('backg.png')
    bg = pygame.transform.scale(bg, (400, 300))
    car_left = pygame.image.load('Player_left.png')
    car_left = pygame.transform.scale(car_left, (100, 100))
    car_right = pygame.image.load('Player_Right.png')
    car_right = pygame.transform.scale(car_right, (100, 100))
    car_left_lane = False #False means left, True means right
    car_right_lane = False
    frames = 0
    
    while run:
        clock.tick(FPS)
        frames+=1
        
        if frames%60 == 0:
            spawn_obstacle()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    car_left_lane = not car_left_lane
                if event.key == pygame.K_RSHIFT:
                    car_right_lane=not car_right_lane
                    
        tileBackground(win, bg)
        
        if car_left_lane:
            x_left = 70
        else:
            x_left = 220

        if car_right_lane:
            x_right = 470
        else:
            x_right = 620
            
        render_obj(car_right, x_right,500)
        render_obj(car_left,x_left,500)
        
        for obstacle in obstacles:
            obstacle[2]+=VEL
            render_obj(obstacle[0], obstacle[1], obstacle[2])
        
        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
    
# 70, 220 and 470, 620