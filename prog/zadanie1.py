#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# main.py

import collection_converter

type = input("Введите тип коллекции (list или tuple): ")
numbers_string = input("Введите список целых чисел, разделенных пробелами: ")

converter = collection_converter.collection_converter(type)
collection = converter(numbers_string)

print(collection)