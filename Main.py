import random
from Robot import Robot
from Reward import Reward

def check_reward(robot, rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print('The robot found the reward: %s' % reward.name)
            ok = True
    return ok

r1 = Reward(random.randint(1, 10), random.randint(1, 10), 'Coin')
r2 = Reward(random.randint(1, 10), random.randint(1, 10), 'Gas')
r3 = Reward(random.randint(1, 10), random.randint(1, 10), 'Gun')
r4 = Reward(random.randint(1, 10), random.randint(1, 10), 'Coin')
r5 = Reward(random.randint(1, 10), random.randint(1, 10), 'Gas')
r6 = Reward(random.randint(1, 10), random.randint(1, 10), 'Gun')
r7 = Reward(random.randint(1, 10), random.randint(1, 10), 'Coin')
r8 = Reward(random.randint(1, 10), random.randint(1, 10), 'Gas')
r9 = Reward(random.randint(1, 10), random.randint(1, 10), 'Gun')
rewards = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
robot = Robot(random.randint(0, 10), random.randint(0, 10))
print(robot)
for i in range(10):
    moviment = input('Type [up, down, left or right] to move: ')
    if moviment == 'up':
        robot.move_up()
    elif moviment == 'down':
        robot.move_down()
    elif moviment == 'left':
        robot.move_left()
    elif moviment == 'right':
        robot.move_right()
    else:
        print('Invalid moviment')
        continue
    print(robot)
    check_reward(robot, rewards)
print('The rewards were in positions %s' % rewards)

