import pytest
from ..def_1 import search

class TestClass:
    @pytest.mark.parametrize('geo_logs', 'expected', 
        ([
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}]),
    ([{'visit1': ['Москва', 'Россия']},
    {'visit3': ['Владимир', 'Россия']}, 
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
      {'visit10': ['Архангельск', 'Россия']}])
    )

    
    def test_one(self, geo_logs, expected):
        assert search(geo_logs) != expected



if __name__ == '__main__':
    TestClass()
