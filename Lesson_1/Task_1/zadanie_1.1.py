import logic

while True:
    distance = int(input("Podaj dystans"))
    speed = int(input("Podaj predkosc"))
    printuj = logic.avg_speed(distance, speed)
    print(printuj)

