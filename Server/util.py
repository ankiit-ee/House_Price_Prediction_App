import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def estimate_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    tmp = np.zeros(len(__data_columns))
    tmp[0] = sqft
    tmp[1] = bath
    tmp[2] = bhk
    if loc_index >= 0:
        tmp[loc_index] = 1
    return round(__model.predict([tmp])[0], 2)


def get_location():
    return __locations


def load_saved_files():
    print("loading...")
    global __data_columns
    global __locations
    global __model

    with open("./imp_files/columns.json", 'r') as f:
        __data_columns = json.load(f)['data-columns']
        __locations = __data_columns[3:]

    with open("./imp_files/Bengaluru_House_Data.pickle", 'rb') as f:
        __model = pickle.load(f)

    print("loading files...over")


if __name__ == '__main__':
    load_saved_files()
    print(get_location())
    print(estimate_price('1st phase jp nagar', 1000, 3, 3))
    print(estimate_price('1st phase jp nagar', 1000, 2, 2))
    print(estimate_price('Mysore', 1000, 3, 3))
    print(estimate_price('Myse', 1000, 3, 3))
    print(estimate_price('Delhi', 1200, 2, 2))