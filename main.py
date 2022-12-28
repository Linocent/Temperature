from device import TriggerThermometer


def main():
    compt = 1
    while compt == 1:
        trigger = input("voulez vous connaitre la température? Y/N\n")
        if trigger == "Y":
            TriggerThermometer().trigger()
        if trigger == "N":
            exit()
        else:
            print("Entrée non comprise")


if __name__ == "__main__":
    main()
