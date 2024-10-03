import pytest
from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.fixture()
def bad_words():
    bad_words = {"плохой", "грустно", "печально", "ужасно", "ненавижу"}
    return bad_words


@pytest.fixture()
def good_words():
    good_words = {"чудесный", "прекрасный", "солнце", "радость", "счастье"}
    return good_words


def test__check_tweet_sentiment__check_for_a_good_tweet(bad_words, good_words):
    text = "Сегодня чудесный день! Солнце светит, птицы поют. Все прекрасно Но мне грустно"
    
    result = check_tweet_sentiment(text, good_words, bad_words)
    
    assert result == 'GOOD'
   
    
def test__check_tweet_sentiment__check_for_a_bad_tweet(bad_words, good_words):
    text = "Все так плохо! Ничего не получается. Ненавижу этот мир!"
    
    result = check_tweet_sentiment(text, good_words, bad_words)
    
    assert result == 'BAD'
    
    
@pytest.mark.parametrize('text', 
                         [
                             '', 
                             'Я сегодня ходил в магазин. Купил продукты.', 
                             'Я сегодня ходил в прекрасный магазин, но ассортимент там плохой', 
                             
                         ])
def test__check_tweet_sentiment__neutral_result_check(text, bad_words, good_words):
    assert check_tweet_sentiment(text, good_words, bad_words) is None
