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