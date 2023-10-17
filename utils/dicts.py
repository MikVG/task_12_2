# файл dicts.py
def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует. В ином случае возвращается значение
    default
    :param collection: исходный словарь
    :param key: передаваемый ключ
    :param default: значение default
    :return: возвращаемое значение словаря по ключу или значение default
    """

    for k in collection:
        if k == key:
            return collection[key]

    return default

