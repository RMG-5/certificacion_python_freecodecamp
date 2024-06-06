'''Calculadora de Probabilidades'''

import copy
import random


class Hat:
    '''Clase para crear sombreros con bolas de colores'''

    def __init__(self, **balls):
        self.contents = []
        for color, number in balls.items():
            self.contents.extend([color] * number)

    def __str__(self):
        return str(self.contents)

    def draw(self, number):
        '''Método para eliminar bolas de colores al azar'''
        balls_drawn = []
        if number >= len(self.contents):
            balls_drawn = self.contents.copy()
            self.contents.clear()
        else:
            x = 0
            while x < number:
                balls_drawn.append(self.contents.pop(
                    random.randrange(0, len(self.contents))))
                x += 1
        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''Función para calcular la probabilidad de obtener "n" numero de bolas de "x" color'''

    expected_balls_list = []
    for color, number in expected_balls.items():
        expected_balls_list.extend([color] * number)

    experiment_correct = 0
    x = 0
    while x < num_experiments:
        hat_copy = copy.deepcopy(hat)
        result_experiment = hat_copy.draw(num_balls_drawn)
        correct_output = len(result_experiment) - len(expected_balls_list)
        for ball in expected_balls_list:
            if ball in result_experiment:
                result_experiment.remove(ball)
        if len(result_experiment) == correct_output:
            experiment_correct += 1
        x += 1

    return experiment_correct / num_experiments


# ********** ********** ********** ********** ********** ********** ********** #
# Ejemplo de uso #

hat_1 = Hat(black=6, red=4, green=3)
EXPERIMENT_1 = experiment(hat=hat_1, expected_balls={
    "red": 2, "green": 1}, num_balls_drawn=5, num_experiments=2000)
print(EXPERIMENT_1)

hat_2 = Hat(white=20, blue=16, yellow=12, orange=8, pink=4)
EXPERIMENT_2 = experiment(hat=hat_2, expected_balls={
    "yellow": 2, "blue": 4, "pink": 1}, num_balls_drawn=10, num_experiments=2000)
print(EXPERIMENT_2)

# ********** ********** ********** ********** ********** ********** ********** #
