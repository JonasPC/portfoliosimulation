import random
from functools import reduce

class Simulator():

    @staticmethod
    def draw():
        realisation = random.gauss(mu=0, sigma=1)
        return realisation

    @classmethod
    def multiple_draws(cls, simulations=10000):
        sim_list = [cls.draw() for i in range(simulations)]
        return sim_list

    @classmethod
    def aggregate_return(cls, simulations=10000):
        return_list = cls.multiple_draws(simulations=simulations)
        rel_returns = [1+return_list[i] for i in range(simulations)]
        return reduce(lambda x, y: x*y, rel_returns)

    @classmethod
    def mc_sim(cls, s):
        if s > 0:
            sim_list = [cls.aggregate_return for i in range(s)]
        else:
            raise Exception("s must be strictly positive")
        return sim_list
