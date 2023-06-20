from unittest import TestCase, main
from ..def_1 import search, geo_logs
from parameterized import parameterized


class SearchTest(TestCase):

    def test_search(self):
        result = search(geo_logs)
        self.assertEqual(result,
                            [
                                {'visit1': ['Москва', 'Россия']},
                                {'visit3': ['Владимир', 'Россия']},
                                {'visit7': ['Тула', 'Россия']},
                                {'visit8': ['Тула', 'Россия']},
                                {'visit9': ['Курск', 'Россия']},
                                {'visit10': ['Архангельск', 'Россия']}
                            ]
                            )
    



if __name__ == '__main__':
    main()
    




