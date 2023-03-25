import pygame  # 1. pygame 선언

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
size = [600, 600]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

block_position = [0, 0]  # (y,x)


def draw_block(screen, color, position):
    block = pygame.Rect((position[0] * 20, position[1] * 20),
                        (20, 20))
    pygame.draw.rect(screen, color, block)


# 4. pygame 무한루프
def runGame():
    global done

    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    block_position[1] -= 1  # 블록의 y 좌표를 1 뺀다
                elif event.key == pygame.K_DOWN:
                    block_position[1] += 1  # 블록의 y 좌표를 1 더한다
                elif event.key == pygame.K_LEFT:
                    block_position[0] -= 1  # 블록의 x 좌표를 1 뺀다
                elif event.key == pygame.K_RIGHT:
                    block_position[0] += 1  # 블록의 x 좌표를 1 더한다

        draw_block(screen, GREEN, block_position)
        pygame.display.update()


runGame()
pygame.quit()
