def calculate(**kwargs):
    for key, worth in kwargs.items():
        print(f"First_name: {key}, age: {worth}")

def run_example():
    dict = {
        "Mikolaj": 34,
        "Patryk": 25,
    }

    dict2 = {
        "Mike": 50,
        "Pat": 75,
    }

    all_dict = {**dict, **dict2}

    result = calculate(**all_dict)


if __name__ == '__main__':
    run_example()