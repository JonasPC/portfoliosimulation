import pytest
from simulator import Simulator
import random


def test_Simulator_callable():
    Simulator()

def test_random_draw():
    inst = Simulator()
    draw = inst.draw()
    assert draw < 2
    assert draw > -2

def test_acc_draws():
    inst = Simulator()
    draws = inst.multiple_draws()
    assert len(draws) == 10000

def test_aggregate_return():
    inst = Simulator()
    total_return = inst.aggregate_return()
    assert type(total_return) == float

def test_mc_draws():
    inst = Simulator()
    mc_return = inst.mc_sim(5000)
    assert len(mc_return) == 5000
    with pytest.raises(Exception) as e_info:
        inst.mc_sim(-2000)
