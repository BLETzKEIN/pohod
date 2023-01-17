import random

import wrap
kroski_sipetsa=[]
wrap.add_sprite_dir("spritew")
wrap.world.create_world(1400, 700)
grinula=None
qwer=0
fall=4
slychainaia_kroshka=None
fishes=[]
skin_fish=["fish blue1","fish colored1","fish colored2","fish colored3","fish pink1","fish purple1"]


ryka = "pystota"
water = wrap.sprite.add("aqua", 700, 400, "water")
wrap.sprite.set_size(water, 1400, 500)
wrap.sprite.move_bottom_to(water, 700)
fish = wrap.sprite.add("fish", 100, 350, "fish blue1")
wrap.sprite.set_size_percent(fish, 50, 50)
food = wrap.sprite.add("aqua", 1200, 100, "fishfood")


def randomniy_skin_fish ():
    w=len(skin_fish)
    randomi=random.randint(0,w-1)
    return skin_fish[randomi]

for e in range(50):
    slychainiy_skin=randomniy_skin_fish()
    e = wrap.sprite.add("fish", random.randint(50,1350), random.randint(250,650), slychainiy_skin)
    wrap.sprite.set_size_percent(e, 50, 50)
    fishes.append(e)


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
    #randomi=random.randint(0,w-1)
    slychainaia_kroshka=kroski_sipetsa[w-1]


def proverka_fish(fish):
    if 700 <= wrap.sprite.get_bottom(fish):
        if 90 < wrap.sprite.get_angle(fish) < 180:
            angle = random.randint(20, 80)
        else:
            angle = random.randint(280, 350)
        wrap.sprite.set_angle(fish, angle)

    if 200 >= wrap.sprite.get_top(fish):
        if wrap.sprite.get_reverse_x(fish):
            angle = random.randint(190, 260)

        else:
            angle = random.randint(100, 180)
        wrap.sprite.set_angle(fish, angle)
        wrap.sprite.move_top_to(fish, 210)

    if 1400 <= wrap.sprite.get_right(fish):
        wrap.sprite.set_reverse_x(fish, True)
        angle = random.randint(210, 330)
        wrap.sprite.set_angle(fish, angle)

    if 0 >= wrap.sprite.get_left(fish):
        angle = random.randint(30, 150)
        wrap.sprite.set_reverse_x(fish, False)
        wrap.sprite.set_angle(fish, angle)

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


def move_fish_to_kroshka (fish) :
    x = wrap.sprite.get_x(slychainaia_kroshka)
    y = wrap.sprite.get_y(slychainaia_kroshka)
    wrap.sprite.set_angle_to_point(fish, x, y)
    wrap.sprite.move_at_angle_point(fish, x, y, 5)

def move_fishess_to_kroshka(fish):
    global slychainaia_kroshka
    if len(kroski_sipetsa)==0:
        wrap.sprite.move_at_angle(fish, wrap.sprite.get_angle(fish), 5)
        proverka_fish(fish)
        return

    if slychainaia_kroshka==None:
        randomnaia_kroska()

    else:
        move_fish_to_kroshka(fish)
        proverka_fish(fish)

    if wrap.sprite.get_y(slychainaia_kroshka) >=697:
        slychainaia_kroshka = None
        return
    if wrap.sprite.is_collide_sprite(fish,slychainaia_kroshka):
        kroski_sipetsa.remove(slychainaia_kroshka)
        wrap.sprite.remove(slychainaia_kroshka)
        slychainaia_kroshka=None



@wrap.always(20)
def move():
    #global angle,slychainaia_kroshka
    for p in fishes:
        move_fishess_to_kroshka(p)
    move_fishess_to_kroshka(fish)


    # if len(kroski_sipetsa)==0:
    #     move_fish(fish)
    #     return
    #
    # if slychainaia_kroshka==None:
    #     randomnaia_kroska()
    #
    # else:
    #     move_fish_to_kroshka()
    #
    # if wrap.sprite.get_y(slychainaia_kroshka) >=697:
    #     slychainaia_kroshka = None
    #     return
    # if wrap.sprite.is_collide_sprite(fish,slychainaia_kroshka):
    #     kroski_sipetsa.remove(slychainaia_kroshka)
    #     wrap.sprite.remove(slychainaia_kroshka)
    #     slychainaia_kroshka=None



import wrap_py
wrap_py.app.start()