'''
Jessica Davis
Lab3.py
Solving the average of cars traveled per road
This is my work and my work only. - Jessica Davis
'''


def traffic():
    road_count = int(input('how many roads were surveyed?:' ))
    total_cars = 0
    for i in range(road_count):
        car_input = 0
        print('how many days was road',i + 1,'surveyed?:')
        days_surveyed = eval(input(''))
        for j in range(days_surveyed):
            print('\thow many cars traveled on day',j + 1,'?:')
            cars_traveled = eval(input(''))
            car_input = car_input + cars_traveled
        road_average = car_input / days_surveyed
        print('road',i + 1,' average vehicles per day: ', road_average)
        total_cars = car_input + total_cars
    print('total numer of vehicles traveled on all roads:', total_cars)
    print('average number of vehicles per road: ', total_cars / road_count)














