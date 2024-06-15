# Day 6 - Functions
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# unknown functions were given by the site/challange


def face_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        face_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


# Hurdle 2
def jump():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

for i in range(0,6):
    jump()


# Hurdle 2
def jump():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()


while not at_goal():
    jump()

done()


# Hurdle 3
def jump():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()

done()


# Hurdle 4
def jump():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    if front_is_clear():
        move()
        while right_is_clear() == True:
            down()
    else:
        jump()    

def down():
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()    
    else:
        jump()


done()
