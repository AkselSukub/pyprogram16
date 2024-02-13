#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# collection_converter.py

def collection_converter(type):
    def inner_func(string):
        numbers = map(int, string.split())
        if type == 'list':
            return list(numbers)
        else:
            return tuple(numbers)
    return inner_func

if __name__ == "__main__":
    # Пример использования
    convert_to_list = collection_converter('list')
    result_list = convert_to_list("1 2 3 4 5")

    convert_to_tuple = collection_converter('tuple')
    result_tuple = convert_to_tuple("1 2 3 4 5")

    print(result_list)
    print(result_tuple)
