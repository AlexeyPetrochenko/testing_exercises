from functions.level_2.five_replace_word import replace_word


def test__replace_word__replacement_of_several_words():
    assert replace_word('Привет Мир Пока Мир', 'Мир', 'World') == 'Привет World Пока World'


def test__replace_word__replace_one_word():
    assert replace_word('Привет Мир', 'Мир', 'World') == 'Привет World'
    
    
def test__replace_word__replacing_words_in_different_registers():
    assert replace_word('Привет МИР', 'мир', 'World') == 'Привет World'
    

def test__replace_word__replacing_words_with_punctuation_marks():
    assert replace_word('Привет, Мир!', 'Мир', 'World') == 'Привет, Мир!'
    

def test__replace_word__replace_word_in_empty_text():
    assert replace_word('', 'Мир', 'World') == ''
    
    