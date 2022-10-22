def calculate(*args):
    r = ""
    pause = "-"
    for number in args:
        number1 = str(number)
        r += number1 + pause
    return r[:-1]

def run_example():
    numbers = [1,4,6,6,66, "Patryczek"]
    result = calculate(*numbers)
    print(result)

if __name__ == '__main__':
    run_example()