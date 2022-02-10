import Math

def test_calc_addition():
    result = Math.calc_addition(4, 2)
    assert result == 6

def test_cal_multiply():
    result = Math.cal_multiply(2, 4)
    assert result == 8

def test_cal_division():
    result = Math.cal_division(4, 2)
    assert result == 2

def test_cal_substraction():
    result = Math.cal_substraction(4, 2)
    assert result == 2

def test_cal_power():
    result = Math.cal_power(2, 2)
    assert result == 4
