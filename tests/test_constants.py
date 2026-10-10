from numpy import sqrt
from leo_satcom.common import constants as const

def test_range_earth_radius():
    assert  6370000 < const.EARTH_RADIUS_M < 6500000

def test_range_gravity_parameter():    
    assert 3.9e14 < const.GRAVITY_PARAMETER_M3_S2 < 4.0e14

def test_range_speed_of_light():
    assert 2.9e8 < const.SPEED_OF_LIGHT_M_S < 3.1e8

def test_range_boltzmann_constant():
    assert 1.3e-23 < const.BOLTZMANN_CONSTANT_J_K < 1.4e-23

def test_range_gravity_acceleration():
    assert 9 < const.GRAVITY_PARAMETER_M3_S2 / (const.EARTH_RADIUS_M ** 2) < 10.0

def test_range_orbital_velocity():
    assert 7e3 < sqrt(const.GRAVITY_PARAMETER_M3_S2 / const.EARTH_RADIUS_M) < 9e3