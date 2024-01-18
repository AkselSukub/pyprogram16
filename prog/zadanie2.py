#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# main.py

from flight_info import *

def main():
    flights = input_flight_info()
    destination = input("Введите пункт назначения, чтобы увидеть информацию о рейсах: ")
    print_flights_to_destination(flights, destination)

if __name__ == "__main__":
    main()
