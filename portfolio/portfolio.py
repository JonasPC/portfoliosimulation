import pandas as pd
import numpy as np


class Portfolio(object):

    def __init__(self, mu, std):
        self.mu = mu
        self.std = std

    def foo(self):
        return 'foo'

    def calc_annual_return(self):
        """calculates the annual return (plus 1)"""
        return 1 + np.random.normal(loc=self.mu, scale=self.std)

    def
