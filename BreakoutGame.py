import pygame
import random

pygame.init()
size = (1920, 1080)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()
fps = 1000
pygame.display.set_caption("Breakout")
v = 4
green = pygame.Color('green')
grey = (128, 128, 128)
pygame.draw.rect(screen, grey, (860, 945, 200, 30))
dx = random.choice([1, -1])
dy = -1
score = 0
count = 0
lives = 3
lfrc = []
draw = 0
pygame.mouse.set_visible(False)
f = True
gamerunning = True


def plat(platx):
    pygame.draw.rect(screen, grey, (platx, 975, 200, 30))


def load_sprite(name):
    fullname = 'Sprites' + '/' + str(name)
    try:
        image = pygame.image.load(fullname).convert()
        return image
    except:
        print('Error', name)
        raise SystemExit()


stage = 1
ball_image = load_sprite('ss.png')
ballsprite = pygame.sprite.Group()
ball = pygame.sprite.Sprite()
ball.image = ball_image
ball.rect = ball.image.get_rect()
ballsprite.add(ball)
ball.rect.x = 0
ball.rect.y = 0
absprites = pygame.sprite.Group()
start = False
rb_image = load_sprite('redbrick.png')
yb_image = load_sprite('yellowbrick.png')
gb_image = load_sprite('greenbrick.png')
bb_image = load_sprite('bluebrick.png')
list_image = [rb_image, yb_image, gb_image, bb_image]
rb_list = []
yb_list = []
gb_list = []
bb_list = []


def GameOver():
    gameover_image = load_sprite('GameOver.png')
    fon = pygame.transform.scale(gameover_image, (1920, 1080))
    screen.blit(fon, (0, 0))
    global gamerunning
    while gamerunning:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamerunning = False
                    exit()
        pygame.display.flip()


def StartScreen():
    startscreen_image = load_sprite('StartScreen.png')
    fon = pygame.transform.scale(startscreen_image, (1920, 1080))
    screen.blit(fon, (0, 0))
    global f
    while f:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    f = False
        pygame.display.flip()


def start_block():
    for j in range(4):
        for i in range(8):
            brick = pygame.sprite.Sprite()
            brick.image = list_image[j]
            brick.rect = brick.image.get_rect()
            brick.rect.x = i * 240
            brick.rect.y = 42 + j * 70
            absprites.add(brick)
            if j == 0:
                rb_list.append(brick)
            if j == 1:
                yb_list.append(brick)
            if j == 2:
                gb_list.append(brick)
            if j == 3:
                bb_list.append(brick)


def pyramidka():
    for i in range(8):
        brick = pygame.sprite.Sprite()
        brick.image = bb_image
        brick.rect = brick.image.get_rect()
        brick.rect.x = i * 240
        brick.rect.y = 42
        absprites.add(brick)
        bb_list.append(brick)
    for i in range(6):
        brick = pygame.sprite.Sprite()
        brick.image = gb_image
        brick.rect = brick.image.get_rect()
        brick.rect.x = 240 + i * 240
        brick.rect.y = 112
        absprites.add(brick)
        bb_list.append(brick)
    for i in range(4):
        brick = pygame.sprite.Sprite()
        brick.image = yb_image
        brick.rect = brick.image.get_rect()
        brick.rect.x = 480 + i * 240
        brick.rect.y = 182
        absprites.add(brick)
        yb_list.append(brick)
    for i in range(2):
        brick = pygame.sprite.Sprite()
        brick.image = rb_image
        brick.rect = brick.image.get_rect()
        brick.rect.x = 720 + i * 240
        brick.rect.y = 252
        absprites.add(brick)
        rb_list.append(brick)


def random_lvl():
    cx = 0
    ac = 0
    cy = 0
    for _ in range(32):
        a = random.choice([0, 1, 2, 3])
        lfrc.append(a)
    for i in lfrc:
        brick = pygame.sprite.Sprite()
        brick.image = list_image[i]
        brick.rect = brick.image.get_rect()
        brick.rect.x = cx * 240
        brick.rect.y = 42 + cy * 70
        if cx == 7:
            cx = 0
            cy += 1
            ac += 1
        else:
            cx += 1
            ac += 1
        absprites.add(brick)
        if i == 0:
            rb_list.append(brick)
        if i == 1:
            yb_list.append(brick)
        if i == 2:
            gb_list.append(brick)
        if i == 3:
            bb_list.append(brick)


running = True
start_block()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEMOTION:
            platx = pygame.mouse.get_pos()[0]
            if not start:
                ball.rect.x = platx + 85
                ball.rect.y = 945

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = True

    if f:
        StartScreen()
        screen.fill((0, 0, 0))
    screen.fill((0, 0, 0))
    f1 = pygame.font.SysFont('arial', 36)
    text1 = f1.render('Score ' + str(score), 1, green)
    text2 = f1.render('Lives ' + str(lives), 1, green)
    text3 = f1.render('Stage ' + str(stage), 1, green)
    screen.blit(text1, (0, 0))
    screen.blit(text2, (640, 0))
    screen.blit(text3, (1280, 0))
    pygame.draw.line(screen, green, [0, 40], [1920, 40], 2)
    new_dx = pygame.mouse.get_rel()[0]
    if start:
        ball.rect.x = ball.rect.x + dx * v
        blocks_hit_list = pygame.sprite.spritecollide(ball, absprites, True)
        if len(blocks_hit_list) > 0:
            for block in blocks_hit_list:
                if block in rb_list:
                    block.kill()
                    absprites.remove(block)
                    score += 40
                    rb_list.remove(block)
                if block in yb_list:
                    block.kill()
                    absprites.remove(block)
                    score += 30
                    yb_list.remove(block)
                if block in gb_list:
                    block.kill()
                    absprites.remove(block)
                    score += 20
                    gb_list.remove(block)
                if block in bb_list:
                    block.kill()
                    absprites.remove(block)
                    score += 10
                    bb_list.remove(block)
            dx *= -1
            ball.rect.x = ball.rect.x + dx * v
            ball.rect.y = ball.rect.y + dy * v
            if len(absprites) == 0:
                start = False
                stage += 1
                if stage == 2:
                    dy = -1
                    pyramidka()
                elif stage == 3:
                    dy = -1
                    random_lvl()
        else:
            ball.rect.y = ball.rect.y + dy * v
            blocks_hit_list = pygame.sprite.spritecollide(ball, absprites, True)
            if len(blocks_hit_list) > 0:
                for block in blocks_hit_list:
                    if block in rb_list:
                        block.kill()
                        absprites.remove(block)
                        score += 40
                        rb_list.remove(block)
                    if block in yb_list:
                        block.kill()
                        absprites.remove(block)
                        score += 30
                        yb_list.remove(block)
                    if block in gb_list:
                        block.kill()
                        absprites.remove(block)
                        score += 20
                        gb_list.remove(block)
                    if block in bb_list:
                        block.kill()
                        absprites.remove(block)
                        score += 10
                        bb_list.remove(block)
                dy *= -1
                ball.rect.y = ball.rect.y + dy * v
                if len(absprites) == 0:
                    start = False
                    stage += 1
                    if stage == 2:
                        dy = -1
                        pyramidka()
                    elif stage == 3:
                        dy = -1
                        random_lvl()

    y = ball.rect.y
    x = ball.rect.x
    if y <= 40:
        dy *= -1

    if ball.rect.y >= 945 and ball.rect.y <= 950 and start and x + 30 >= platx and x + 30 <= platx + 200:
        dy *= -1
        dx += new_dx / 50
    if x <= 0 or x >= 1900:
        dx *= -1
    if ball.rect.y >= 1080:
        start = False
        ball.rect.x = platx + 85
        ball.rect.y = 945
        dy = -1
        dx = random.choice([1, -1])
        count += 1
        lives -= 1
        if count == 4:
            GameOver()
    plat(platx)
    ballsprite.draw(screen)
    absprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
