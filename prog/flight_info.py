#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# flight.py

def input_flight_info():
    flights = []
    while True:
        destination = input("Введите пункт назначения рейса (или 'q' для выхода): ")
        if destination.lower() == 'q':
            break
        flight_number = int(input("Введите номер рейса: "))
        aircraft_type = input("Введите тип самолета: ")
        flights.append({
            'destination': destination,
            'flight_number': flight_number,
            'aircraft_type': aircraft_type
        })
    flights.sort(key=lambda x: x['flight_number'])
    return flights

def print_flights_to_destination(flights, destination):
    matching_flights = [flight for flight in flights if flight['destination'] == destination]
    if not matching_flights:
        print(f"Нет рейсов в направлении {destination}.")
    else:
        for flight in matching_flights:
            print(f"Номер рейса: {flight['flight_number']}, тип самолета: {flight['aircraft_type']}")
