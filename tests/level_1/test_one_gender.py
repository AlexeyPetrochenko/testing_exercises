import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize('verb_male, verb_female, gender',
                  [
                      ('сделал', 'сделала', 'male'),
                      ('купил', 'купила', 'male'),
                      ('стоял', 'стояла', 'male'),
                      (1, 0, 'male'),
                  ])
def test_return_verb_male(verb_male, verb_female, gender):
    assert genderalize(verb_male, verb_female, gender) == verb_male


@pytest.mark.parametrize('verb_male, verb_female, gender',
                  [
                      ('сделал', 'сделала', 'female'),
                      ('купил', 'купила', 'женщина'),
                      ('стоял', 'стояла', 'мужчина'),
                      ('стоял', 'стояла', ''),
                      ('стоял', 'стояла', '1234'),
                  ])
def test_return_verb_female_for_type_str(verb_male, verb_female, gender):
    assert (genderalize(verb_male, verb_female, gender)) == verb_female


@pytest.mark.parametrize('verb_male, verb_female, gender',
                  [
                      ('сделал', 'сделала', 123),
                      ('купил', 'купила', 4.123),
                      ('стоял', 'стояла', float('inf')),
                      ('стоял', 'стояла', float('-inf')),
                      ('стоял', 'стояла', ['male']),
                      ('стоял', 'стояла', set()),
                      ('стоял', 'стояла', ('male', 1, 3)),
                      ('стоял', 'стояла', None),

                  ])
def test_different_types_returning_correct_result(verb_male, verb_female, gender):
    assert genderalize(verb_male, verb_female, gender) == verb_female

