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
    for item in _list:
        result = item.split()

        if len(result) in dict_:
            dict_[len(result)] += 1
        
        else:
            dict_.update({len(result):1})
    
    for key, value in dict_.items():
        percentage = round((value / len(queries)) * 100, 2)
        return f'Поисковых запросов из {key} слова: {percentage}% ({value} запр.)'

res = requests_distributed(queries)
print(res)
