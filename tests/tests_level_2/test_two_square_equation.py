import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize('coefficients, answer', 
                         [
                             ((4.0, 2.0, -3.0), (-1.1513878188659974, 0.6513878188659973)),
                             ((-4.0, 21.0, 3.0), (5.389168048436998, -0.1391680484369977)),
                             ((-15.5, 22.34, 100.12), (3.362365109960286, -1.9210747873796405)),
                         ])
def test__solve_square_equation__with_two_roots(coefficients, answer):
    assert solve_square_equation(*coefficients) == answer


@pytest.mark.parametrize('coefficients',
                         [
                             (4.0, 2.0, 3.0),
                             (10.12, 2.11, 3.0)
                         ])
def test__solve_square_equation__no_roots_when_discriminant_less_than_zero(coefficients):
    assert solve_square_equation(*coefficients) == (None, None)


@pytest.mark.parametrize('coefficients, answer',
                         [
                             ((0.0, 14.0, 24.0), (-1.7142857142857142, None)),
                             ((0.0, 4.0, 1.0), (-0.25, None))
                         ])
def test__solve_square_equation__with_one_root_when_no_square_coefficient(coefficients, answer):
    assert solve_square_equation(*coefficients) == answer
    
    

@pytest.mark.parametrize('coefficients',
                         [
                             (0.0, 0.0, 3.0),
                             (0.0, 0.0, -3.0),
                         ])
def test__solve_square_equation__no_roots_when_no_square_and_linear_coefficients(coefficients):
    assert solve_square_equation(*coefficients) == (None, None)
    

@pytest.mark.parametrize('coefficients, answer',
                         [
                             ((0.0, 0.0, 0.0), (None, None)),
                             ((float('inf'), 4.0, 1.0), (None, None)),
                             ((11.1, 11.0, float('-inf')), (float('-inf'), float('inf')))
                         ])
def test__solve_square_equation__corner_cases(coefficients, answer):
    assert solve_square_equation(*coefficients) == answer
    