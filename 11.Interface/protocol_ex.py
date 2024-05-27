from typing import Protocol


class Drivable(Protocol):
    def drive(self, distance: float) -> None:
        ...


class Car:
    def drive(self, distance: float) -> None:
        print(f"Car is driving {distance} miles")


class Bike:
    def drive(self, distance: float) -> None:
        print(f"Bike is driving {distance} miles")


def start_trip(vehicle: Drivable, distance: float) -> None:
    vehicle.drive(distance)


car = Car()
bike = Bike()

start_trip(car, 10)  # 출력: Car is driving 10 miles
start_trip(bike, 5)  # 출력: Bike is driving 5 miles
