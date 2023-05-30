import copy
import random

class Hat:

    def __init__(self, **balls):
        self.contents = []
        for color, value in balls.items():
            for _ in range(value):
                self.contents.append(color)


    def draw(self, draw_number):
        picked = []
        buffer_balls = copy.deepcopy(self.contents)

        if draw_number >= len(buffer_balls):
            return buffer_balls

        for _ in range(draw_number):
            pick = random.choice(buffer_balls)
            buffer_balls.remove(pick)
            picked.append(pick)

        return picked


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    N = num_experiments

    for _ in range(num_experiments):
        # make an object of drawn balls
        drawn_balls = {}
        buffer_balls = hat.draw(num_balls_drawn)

        for ball in buffer_balls:
            if ball in drawn_balls.keys():
                drawn_balls[ball] += 1
            else:
                drawn_balls[ball] = 1

        # check whether every element of expected_balls are in drawn_balls
        condition = True
        for item in expected_balls:
            try:
                if expected_balls[item] > drawn_balls[item]:
                    condition = False
                    break
            except KeyError:
                condition = False

        # if above condition meet, record it in M
        if condition:
            M += 1

    return M/N
