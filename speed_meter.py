penalty = False
while penalty == False:
    max_velocity = 80
    velocity = int(input('What was the speed of the car? '))
    if velocity <= max_velocity:
        print('There was no fine.')
    elif velocity >= max_velocity and velocity <= max_velocity + 10:
        print('Light fine.')
    elif velocity >= max_velocity +11 and velocity <= max_velocity + 20:
        print('Serious fine.')
    elif velocity >= max_velocity + 20:
        print('Very serious fine.')
