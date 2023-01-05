import random

import wrap
kroski_sipetsa=[]
wrap.add_sprite_dir("spritew")
wrap.world.create_world(1400, 700)
grinula=None
qwer=0
fall=4



ryka = "pystota"
water = wrap.sprite.add("aqua", 700, 400, "water")
wrap.sprite.set_size(water, 1400, 500)
wrap.sprite.move_bottom_to(water, 700)
fish = wrap.sprite.add("fish", 100, 350, "fish blue1")
wrap.sprite.set_size_percent(fish, 50, 50)
food = wrap.sprite.add("aqua", 1200, 100, "fishfood")
angle = random.randint(30, 150)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def foodd(pos_x, pos_y):
    global ryka,qwer
    if wrap.sprite.is_collide_point(food, pos_x, pos_y):
        ryka = "banka"
        qwer=1+qwer
    if ryka=="banka" and qwer>=2:
        wrap.sprite.set_angle(food, 260)
        rnge=random.randint(3,7)
        sozdaem_kroshki(rnge)

    # if wrap.sprite.is_collide_point(food, pos_x, pos_y) and ryka!="banka":
    #     ryka="banka"
    # elif ryka=="banka":
    #     wrap.sprite.set_angle(food, 260)
    #


def sozdaem_kroshki(renge):
    for r in range(renge):
        y_grin = random.randint(0, 10)
        x_grin = random.randint(0, 60)
        grinula = wrap.sprite.add("aqua", wrap.sprite.get_x(food) + x_grin, wrap.sprite.get_bottom(food) - y_grin,
                                  "fish food granula")
        wrap.sprite.set_size_percent(grinula, 20, 20)
        kroski_sipetsa.append(grinula)



@wrap.on_mouse_up(wrap.BUTTON_LEFT, wrap.BUTTON_MIDDLE)
def ne_sipetsa():
    wrap.sprite.set_angle(food, 90)



@wrap.on_mouse_down(wrap.BUTTON_MIDDLE)
def krosek100(pos_x, pos_y):
    global kroski_sipetsa,grinula
    if ryka == "banka":
        wrap.sprite.set_angle(food, 260)
        rahge=random.randint(100,120)
        sozdaem_kroshki(rahge)



@wrap.always(20)
def k_roski ():
    global grinula,fall
    for i in kroski_sipetsa:
        if wrap.sprite.is_collide_sprite(i, water):
            fall = random.randint(1,3)
            if wrap.sprite.get_y(i)>=697:
                kroski_sipetsa.remove(i)
        else:
            fall=5
        wrap.sprite.move(i,0,fall)

def randomnaia_kroska():
    global slychainaia_kroshka
    w=len(kroski_sipetsa)
    randomi=random.randint(0,w-1)
    slychainaia_kroshka=kroski_sipetsa[randomi]




@wrap.on_key_down(wrap.K_ESCAPE)
def yberi_ryka():
    global ryka,qwer
    ryka = "pystota"
    wrap.sprite.move_to(food, 1200, 100)
    qwer=0


@wrap.on_mouse_move()
def move_ryki(pos_x, pos_y):
    if ryka == "banka":
        wrap.sprite.move_to(food, pos_x, pos_y)
    if wrap.sprite.get_bottom(food) >= wrap.sprite.get_top(water):
        wrap.sprite.move_bottom_to(food, wrap.sprite.get_top(water))


@wrap.always(20)
def move():
    global angle
    if len(kroski_sipetsa)>=1:
        randomnaia_kroska()
        wrap.sprite.move_at_angle_point(fish,wrap.sprite.get_x(slychainaia_kroshka),wrap.sprite.get_y(slychainaia_kroshka),5)
    else:
        wrap.sprite.set_angle(fish, angle)
        wrap.sprite.move_at_angle(fish, angle, 5)
        if 700 <= wrap.sprite.get_bottom(fish):
            if 90 < wrap.sprite.get_angle(fish) < 180:
                angle = random.randint(20, 80)
            else:
                angle = random.randint(280, 350)

        if 200 >= wrap.sprite.get_top(fish):
            if wrap.sprite.get_reverse_x(fish):
                angle = random.randint(190, 260)
            else:
                angle = random.randint(100, 180)

        if 1400 <= wrap.sprite.get_right(fish):
            wrap.sprite.set_reverse_x(fish, True)
            angle = random.randint(210, 330)
        if 0 >= wrap.sprite.get_left(fish):
            angle = random.randint(30, 150)
            wrap.sprite.set_reverse_x(fish, False)

import wrap_py
wrap_py.app.start()