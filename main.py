import pgzrun

WIDTH = 800
HEIGHT = 600

tank = Actor('tank_blue')
tank2 = Actor('tank_red')
background = Actor('grass')

walls = []
tank1_bullets = []
tank1_bullet_hold_off = 0
tank2_bullets = []
tank2_bullet_hold_off = 0
did_tank_1_win = False
did_tank_2_win = False


def setup():
    global walls
    global tank1_bullets
    global tank2_bullets
    global tank1_bullet_hold_off
    global tank2_bullet_hold_off
    global did_tank_1_win
    global did_tank_2_win

    tank.y = 575
    tank.x = 400
    tank.angle = 90

    tank2.y = 30
    tank2.x = 400
    tank2.angle = 270

    tank1_bullets = []
    tank1_bullet_hold_off = 0
    tank2_bullets = []
    tank2_bullet_hold_off = 0

    walls = []

    for x in range(2, 15):
        wall = Actor('wall')
        wall.x = x * 50
        wall.y = 300
        walls.append(wall)

    did_tank_1_win = False
    did_tank_2_win = False


mode = 'START'  # START, GAME, END


def create_bullet(tank, bullet_img):
    bullet = Actor(bullet_img)
    bullet.angle = tank.angle
    bullet.x = tank.x
    bullet.y = tank.y
    return bullet


def animate_bullet(bullet):
    if bullet.angle == 0:
        bullet.x = bullet.x + 5
    elif bullet.angle == 90:
        bullet.y = bullet.y - 5
    elif bullet.angle == 180:
        bullet.x = bullet.x - 5
    elif bullet.angle == 270:
        bullet.y = bullet.y + 5


def update():
    global tank1_bullet_hold_off
    global tank2_bullet_hold_off
    global did_tank_1_win
    global did_tank_2_win
    global mode

    if mode == 'START':
        setup()
        if keyboard.g:
            mode = 'GAME'
    elif mode == 'GAME':
        original_x = tank.x
        original_y = tank.y
        original2_x = tank2.x
        original2_y = tank2.y

        if keyboard.left:
            tank.x = tank.x - 2
            tank.angle = 180
        elif keyboard.right:
            tank.x = tank.x + 2
            tank.angle = 0
        elif keyboard.up:
            tank.y = tank.y - 2
            tank.angle = 90
        elif keyboard.down:
            tank.y = tank.y + 2
            tank.angle = 270

        if tank1_bullet_hold_off == 0:
            if keyboard.space:
                bullet = create_bullet(tank, 'bulletblue2')
                tank1_bullets.append(bullet)
                tank1_bullet_hold_off = 75
        else:
            tank1_bullet_hold_off = tank1_bullet_hold_off - 1

        for bullet in tank1_bullets:
            animate_bullet(bullet)
            wall_index = bullet.collidelist(walls)
            if wall_index != -1:
                del walls[wall_index]
                tank1_bullets.remove(bullet)
            if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
                tank1_bullets.remove(bullet)

            hitTank2 = bullet.colliderect(tank2)
            if hitTank2 == True:
                did_tank_1_win = True
                mode = 'END'

        if keyboard.a:
            tank2.x = tank2.x - 2
            tank2.angle = 180
        elif keyboard.d:
            tank2.x = tank2.x + 2
            tank2.angle = 0
        elif keyboard.w:
            tank2.y = tank2.y - 2
            tank2.angle = 90
        elif keyboard.s:
            tank2.y = tank2.y + 2
            tank2.angle = 270

        if tank2_bullet_hold_off == 0:
            if keyboard.x:
                bullet = create_bullet(tank2, 'bulletred2')
                tank2_bullets.append(bullet)
                tank2_bullet_hold_off = 75
        else:
            tank2_bullet_hold_off = tank2_bullet_hold_off - 1

        for bullet in tank2_bullets:
            animate_bullet(bullet)
            wall_index = bullet.collidelist(walls)
            if wall_index != -1:
                del walls[wall_index]
                tank2_bullets.remove(bullet)
            if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
                tank2_bullets.remove(bullet)
            hitTank1 = bullet.colliderect(tank)
            if hitTank1 == True:
                did_tank_2_win = True
                mode = 'END'

        if tank.collidelist(walls) != -1:
            tank.x = original_x
            tank.y = original_y

        if tank2.collidelist(walls) != -1:
            tank2.x = original2_x
            tank2.y = original2_y
    elif mode == 'END':
        if keyboard.r:
            mode = 'START'


def draw():
    if mode == 'START':
        screen.fill((0, 0, 0))
        screen.draw.text('Tank Wars', (200, 250),
                         color=(255, 255, 255), fontsize=100)
        screen.draw.text('Press g to start', (300, 400),
                         color=(255, 255, 255), fontsize=32)
    elif mode == 'GAME':
        background.draw()
        tank.draw()
        tank2.draw()
        for bullet in tank1_bullets:
            bullet.draw()
        for bullet in tank2_bullets:
            bullet.draw()
        for wall in walls:
            wall.draw()
    elif mode == 'END':
        if did_tank_1_win == True:
            screen.fill((0, 0, 0))
            screen.draw.text('Tank 1 Wins!', (200, 250),
                             color=(255, 255, 255), fontsize=100)
        elif did_tank_2_win == True:
            screen.fill((0, 0, 0))
            screen.draw.text('Tank 2 Wins!', (200, 250),
                             color=(255, 255, 255), fontsize=100)
        screen.draw.text('Press r to restart', (300, 400),
                         color=(255, 255, 255), fontsize=32)


pgzrun.go()  # Must be last line
