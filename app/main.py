class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str
                 ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int
                 ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        result = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                result += self.calculate_washing_price(car)
                car.clean_mark = self.clean_power
        return result

    def calculate_washing_price(self, car: Car) -> float:
        cost = (car.comfort_class
                * (self.clean_power - car.clean_mark)
                * self.average_rating
                / self.distance_from_city_center)
        return round(cost, 1)

    def wash_single_car(self, car: Car) -> float:
        return self.calculate_washing_price(car)

    def rate_service(self, grade: float) -> None:
        up_count_of_ratings = self.count_of_ratings + 1
        self.average_rating = round(
            (self.average_rating * self.count_of_ratings + grade)
            / up_count_of_ratings)
        self.count_of_ratings = up_count_of_ratings


# # print("-"*30)
#
# bmw = Car(3, 3, 'BMW')
# audi = Car(4, 9, 'Audi')
# mercedes = Car(7, 1, 'Mercedes')
#
# ws = CarWashStation(6, 8, 3.9, 11)
#
# income = ws.serve_cars([
#     bmw,
#     audi,
#     mercedes
# ])
#
# # income == 41.7
# print(income)
#
# # bmw.clean_mark == 8
# # audi.clean_mark == 9
# # mercedes.clean_mark == 8
#
# print(bmw.clean_mark)
# print(audi.clean_mark)
# print(mercedes.clean_mark)
# # audi wasn't washed
# # all other cars are washed to '8'
#
# ford = Car(2, 1, 'Ford')
# wash_cost = ws.calculate_washing_price(ford)
# # only calculating cost, not washing
# # wash_cost == 9.1
# # ford.clean_mark == 1
#
# print(wash_cost)
# print(ford.clean_mark)
#
# print("-"*30)
#
# ws.rate_service(5)
#
# # ws.count_of_ratings == 12
# # ws.average_rating == 4.0
# print(ws.count_of_ratings)
# print(ws.average_rating)
