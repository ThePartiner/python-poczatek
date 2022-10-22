def calculate(**kwargs):
    for key, worth in kwargs.items():
        print(f"First_name: {key}, age: {worth}")

def run_example():
    dict = {
        "Mikolaj": 34,
        "Patryk": 25,
    }
    result = calculate(**dict)


if __name__ == '__main__':
    run_example()