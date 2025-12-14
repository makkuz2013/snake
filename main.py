import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
running = True

def start():
    global snake_pos, snake_dir, tick, score, playing, snake
    snake = []
    snake_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    for i in range(5):
        snake.append(snake_pos.copy())
    snake_dir = pygame.Vector2(50,0)

    tick = 0

    score = 0

    playing = True

    spawn_apple()

font = pygame.font.Font(None, 48)

def spawn_apple():
    global apple_pos
    apple_pos = pygame.Vector2(random.randint(0,15) * 50, random.randint(0,11) * 50)

start()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('darkgreen')

    if playing:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            snake_dir.x = 0
            snake_dir.y = -50
        if keys[pygame.K_a]:
            snake_dir.x = -50
            snake_dir.y = 0
        if keys[pygame.K_s]:
            snake_dir.x = 0
            snake_dir.y = 50
        if keys[pygame.K_d]:
            snake_dir.x = 50
            snake_dir.y = 0

    for body in snake:
        rect = pygame.Rect(body.x,body.y,50,50)
        pygame.draw.rect(screen, 'green', rect)

    apple_rect = pygame.Rect(apple_pos.x,apple_pos.y,50,50)
    pygame.draw.rect(screen, 'red', apple_rect)

    text_surface = font.render(f'Score: {score}', False, 'white')
    text_rect = text_surface.get_rect()
    screen.blit(text_surface, text_rect)

    if tick % 20 == 0 and playing:
        snake_pos += snake_dir
        snake.append(snake_pos.copy())
        snake_rect = pygame.Rect(snake_pos.x,snake_pos.y,50,50)
        if snake_rect.colliderect(apple_rect):
            spawn_apple()
            score += 10
        else:
            snake.pop(0)

    if playing:
        if tick % 20 == 0:
            for body in snake[:-1]:
                body_rect = pygame.Rect(body.x,body.y,50,50)
                if snake_rect.colliderect(body_rect):
                    playing = False
            if not screen.get_rect().colliderect(snake_rect):
                playing = False
    else:
        text_surface = font.render('GAME OVER', False, 'red')
        text_rect = text_surface.get_rect()
        text_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
        screen.blit(text_surface, text_rect)
        button_rect = pygame.Rect(0,0,200,40)
        button_rect.center = text_rect.center
        button_rect.y += 40
        pygame.draw.rect(screen, 'blue', button_rect)
        text_surface = font.render('Restart', False, 'white')
        text_rect = text_surface.get_rect()
        text_rect.center = button_rect.center
        screen.blit(text_surface, text_rect)
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                start()

    pygame.display.flip()

    clock.tick(60)

    tick += 1

pygame.quit()