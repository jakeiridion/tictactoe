s1 = 0
s2 = 0


def zs():
    global runde
    global anfang
    global stop
    global row1
    global row2
    global row3
    runde = 0
    stop = 0
    row1 = ["   ", "|", "   ", "|", "   "]
    row2 = ["   ", "|", "   ", "|", "   "]
    row3 = ["   ", "|", "   ", "|", "   "]


def ausgabe():
    for i in range(5):
        print(row1[i], end="")
    print("")
    for i in range(5):
        print(row2[i], end="")
    print("")
    for i in range(5):
        print(row3[i], end="")
        if i == 4:
            print("")
    print("")


def pruf():
    # wagerecht
    global s1
    global s2

    if row1 == [" X ", "|", " X ", "|", " X "] \
            or row2 == [" X ", "|", " X ", "|", " X "] \
            or row3 == [" X ", "|", " X ", "|", " X "]:
        s1 = s1 + 1
        print("X gewinnt !")
        print("Spieler 1:", s1, "\nSpieler 2:", s2)
        print("")

        zs()
        ausgabe()

    if row1 == [" 0 ", "|", " 0 ", "|", " 0 "] \
            or row2 == [" 0 ", "|", " 0 ", "|", " 0 "] \
            or row3 == [" 0 ", "|", " 0 ", "|", " 0 "]:
        s2 = s2 + 1
        print("0 gewinnt !")
        print("Spieler 1:", s1, "\nSpieler 2:", s2)
        print("")

        zs()
        ausgabe()

    # diagonal:

    if row1[0] == row2[2] and row1[0] == row3[4] and row1[0] != "   " and row2[2] != "   " and row3[4] != "   ":
        if row1[0] == " X ":
            s1 = s1 + 1
            print("X gewinnt !")
            print("Spieler 1:", s1, "\nSpieler 2:", s2)
        else:
            s2 = s2 + 1
            print("0 gewinnt !")
            print("Spieler 1:", s1, "\nSpieler 2:", s2)
        print("")

        zs()
        ausgabe()

    if row1[4] == row2[2] and row1[4] == row3[0] and row1[4] != "   " and row2[2] != "   " and row3[0] != "   ":
        if row1[0] == " X ":
            s1 = s1 + 1
            print("X gewinnt !")
            print("Spieler 1:", s1, "\nSpieler 2:", s2)
        else:
            s2 = s2 + 1
            print("0 gewinnt !")
            print("Spieler 1:", s1, "\nSpieler 2:", s2)
        print("")
        zs()
        ausgabe()

    # senkrecht:

    if row1[0] == row2[0] and row1[0] == row3[0] and row1[0] != "   " and row2[0] != "   " and row3[0] != "   ":
        if row1[0] == " X ":
            s1 = s1 + 1
            print("X gewinnt !")
            print("Spieler 1:", s1, "\nSpieler 2:", s2)
        else:
            s2 = s2 + 1
            print("0 gewinnt !")
            print("Spieler 1:", s1, "\nSpieler 2:", s2)
        print("")
        zs()
        ausgabe()

    if row1[2] == row2[2] and row1[2] == row3[2] and row1[2] != "   " and row2[2] != "   " and row3[2] != "   ":
        if row1[2] == " X ":
            s1 = s1 + 1
            print("X gewinnt !")
            print("Spieler 1:", s1, "\nSpieler 2:", s2)
        else:
            s2 = s2 + 1
            print("0 gewinnt !")
            print("Spieler 1:", s1, "\nSpieler 2:", s2)
        print("")
        zs()
        ausgabe()

    if row1[4] == row2[4] and row1[4] == row3[4] and row1[4] != "   " and row2[4] != "   " and row3[4] != "   ":
        if row1[4] == " X ":
            s1 = s1 + 1
            print("X gewinnt !")
            print("Spieler 1:", s1, "\nSpieler 2:", s2)
        else:
            s2 = s2 + 1
            print("0 gewinnt !")
            print("Spieler 1:", s1, "\nSpieler 2:", s2)
        print("")
        zs()
        ausgabe()
