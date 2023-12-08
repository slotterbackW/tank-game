import pgzrun

WIDTH = 800
HEIGHT = 600

tank = Actor('tank_blue')
tank.y = 575
tank.x = 400
tank.angle = 90

tank2 = Actor('tank_red')
tank2.y = 30
tank2.x = 400
tank2.angle = 270

background = Actor('grass')

walls = []

for x in range(2, 15):
    wall = Actor('wall')
    wall.x = x * 50
    wall.y = 300
    walls.append(wall)

tank1_bullets = []
tank1_bullet_hold_off = 0
tank2_bullets = []
tank2_bullet_hold_off = 0

did_tank_1_win = False
did_tank_2_win = False


def update():
    global tank1_bullet_hold_off
    global tank2_bullet_hold_off
    global did_tank_1_win
    global did_tank_2_win

    if did_tank_1_win == False and did_tank_2_win == False:
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
                bullet = Actor('bulletblue2')
                bullet.angle = tank.angle
                bullet.x = tank.x
                bullet.y = tank.y
                tank1_bullets.append(bullet)
                tank1_bullet_hold_off = 75
        else:
            tank1_bullet_hold_off = tank1_bullet_hold_off - 1

        for bullet in tank1_bullets:
            if bullet.angle == 0:
                bullet.x = bullet.x + 5
            elif bullet.angle == 90:
                bullet.y = bullet.y - 5
            elif bullet.angle == 180:
                bullet.x = bullet.x - 5
            elif bullet.angle == 270:
                bullet.y = bullet.y + 5
            wall_index = bullet.collidelist(walls)
            if wall_index != -1:
                del walls[wall_index]
                tank1_bullets.remove(bullet)
            if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
                tank1_bullets.remove(bullet)

            hitTank2 = bullet.colliderect(tank2)
            if hitTank2 == True:
                did_tank_1_win = True

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
                bullet = Actor('bulletred2')
                bullet.angle = tank2.angle
                bullet.x = tank2.x
                bullet.y = tank2.y
                tank2_bullets.append(bullet)
                tank2_bullet_hold_off = 75
        else:
            tank2_bullet_hold_off = tank2_bullet_hold_off - 1

        for bullet in tank2_bullets:
            if bullet.angle == 0:
                bullet.x = bullet.x + 5
            elif bullet.angle == 90:
                bullet.y = bullet.y - 5
            elif bullet.angle == 180:
                bullet.x = bullet.x - 5
            elif bullet.angle == 270:
                bullet.y = bullet.y + 5
            wall_index = bullet.collidelist(walls)
            if wall_index != -1:
                del walls[wall_index]
                tank2_bullets.remove(bullet)
            if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
                tank2_bullets.remove(bullet)
            hitTank1 = bullet.colliderect(tank)
            if hitTank1 == True:
                did_tank_2_win = True

        if tank.collidelist(walls) != -1:
            tank.x = original_x
            tank.y = original_y

        if tank2.collidelist(walls) != -1:
            tank2.x = original2_x
            tank2.y = original2_y


def draw():
    if did_tank_1_win == True or did_tank_2_win == True:
        if did_tank_1_win == True:
            screen.fill((0, 0, 0))
            screen.draw.text('Tank 1 Wins!', (200, 250),
                             color=(255, 255, 255), fontsize=100)
        elif did_tank_2_win == True:
            screen.fill((0, 0, 0))
            screen.draw.text('Tank 2 Wins!', (200, 250),
                             color=(255, 255, 255), fontsize=100)
    else:
        background.draw()
        tank.draw()
        tank2.draw()
        for bullet in tank1_bullets:
            bullet.draw()
        for bullet in tank2_bullets:
            bullet.draw()
        for wall in walls:
            wall.draw()


pgzrun.go()  # Must be last line
