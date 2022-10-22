def calculate(*args):
    r = ""
    pause = "-"
    for number in args:
        number1 = str(number)
        r += number1 + pause
    return r

def run_example():
    numbers = [1,4,6,6,66,]

    dollar = [2,6,5,5,5,4,5]

    result = [*numbers, *dollar]
    print(result)

if __name__ == '__main__':
    run_example()