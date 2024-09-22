import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize('verb_male, verb_female',
                         [
                                ('сделал', 'сделала'),
                                ('купил', 'купила'),
                                ('стоял', 'стояла'),
                            ])
def test__genderalize__return_verb_male(verb_male, verb_female):
    assert genderalize(verb_male, verb_female, 'male') == verb_male


@pytest.mark.parametrize('verb_male, verb_female, gender',
                         [
                                ('сделал', 'сделала', 'female'),
                                ('купил', 'купила', 'женщина'),
                                ('стоял', 'стояла', 'мужчина'),
                                ('стоял', 'стояла', 'it'),
                            ])
def test__genderalize__return_verb_female_for_other_gender_name(verb_male, verb_female, gender):
    assert (genderalize(verb_male, verb_female, gender)) == verb_female


@pytest.mark.parametrize('verb_male, verb_female, gender',
                         [
                             ('сделал', 'сделала', ''),
                             ('сделал', 'сделала', '1234'),
                             ('сделал', 'сделала', '    '),
                             ('сделал', 'сделала', '!@@#$%^')
                         ])
def test__genderalize__return_value_for_all_other_string(verb_male, verb_female, gender):
    assert genderalize(verb_male, verb_female, gender) == verb_female

