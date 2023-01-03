import re

import pandas as pd
import os
import re
import time
#
# class Population:
#     def __init__(self, **location):
#         self.location = location
#
#
#
#
#
#


def data_check(data, max_int):
    x = [i for i in range(1,max_int+1)]
    if data in x:
        return data
    else:
        input(f"You fucker...from 1 to {max_int}")

def get_data(location_name):
    location_data = pd.read_csv(f"./Population/{location_name}-2019.csv")
    return location_data

def get_location_aval(destination = './Population'):
    filenames = next(os.walk(destination), (None, None, []))[2]
    locations = []
    for name in filenames:
        loc = name.split('-')[0]
        locations.append(loc)
    return locations

def population_data():
    locations = get_location_aval()
    print("Hi! Choose the country you want to put first zombie in:")
    for i,name in enumerate(locations):
        print(f"For {name} press {i+1}")
    answ = data_check(int(input("So your choice:")),len(locations))
    ans = locations[answ-1]
    data = get_data(ans)
    # print(f"So data for {ans} is... \n {data}")
    return ans,data



#
# if __name__ == "__main__":
#     # destination = './Population'
#     # loc_available = get_location_aval()
#     ans = menu()
#     print(f"So data for {ans} is... \n ")
#     time.sleep(1)
#     print()




