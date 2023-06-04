# Дан список поисковых запросов. Получить распределение количества слов в них. 
# Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]


def requests_distributed(_list):
    dict_ = {}
    list_ = []
    list_1 = []
    for item in _list:
        result = item.split()
        dict_.update({len(result):result})
        list_.append(dict_)
    for my_dict in list_:
        for key, value in my_dict.items():
            percentage = round((len(value) / len(queries)) * 100, 2)
            list_1.append(f'Поисковых запросов из {key} слов: {percentage}% ')
        return list_1


res = requests_distributed(queries)
print(res)
