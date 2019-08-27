import deff

deff.zs()
deff.ausgabe()

while True:
    while deff.runde != 9:
        if deff.runde % 2 == 0:
            print("Spieler 1 wo soll dein X gesetzt werden? (1-9)")
            x = input("> ")
            if x == "q":
                break
            x = int(x)

            if x <= 3:
                if x == 1:
                    if deff.row1[0] == "   ":
                        deff.row1[0] = " X "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        continue
                if x == 2:
                    if deff.row1[2] == "   ":
                        deff.row1[2] = " X "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        continue
                if x == 3:
                    if deff.row1[4] == "   ":
                        deff.row1[4] = " X "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        continue
            if x <= 6:
                if x == 4:
                    if deff.row2[0] == "   ":
                        deff.row2[0] = " X "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        continue
                if x == 5:
                    if deff.row2[2] == "   ":
                        deff.row2[2] = " X "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        continue
                if x == 6:
                    if deff.row2[4] == "   ":
                        deff.row2[4] = " X "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        continue
            if x <= 9:
                if x == 7:
                    if deff.row3[0] == "   ":
                        deff.row3[0] = " X "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        continue
                if x == 8:
                    if deff.row3[2] == "   ":
                        deff.row3[2] = " X "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        continue
                if x == 9:
                    if deff.row3[4] == "   ":
                        deff.row3[4] = " X "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        continue
            deff.ausgabe()
            deff.runde = deff.runde + 1
            deff.pruf()
            continue

        else:
            print("Spieler 2 wo soll dein X gesetzt werden? (1-9)")
            x = input("> ")
            if x == "q":
                break
            x = int(x)

            if x <= 3:
                if x == 1:
                    if deff.row1[0] == "   ":
                        deff.row1[0] = " 0 "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        print("")
                        continue
                if x == 2:
                    if deff.row1[2] == "   ":
                        deff.row1[2] = " 0 "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        print("")
                        continue
                if x == 3:
                    if deff.row1[4] == "   ":
                        deff.row1[4] = " 0 "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        print("")
                        continue

            if x <= 6:
                if x == 4:
                    if deff.row2[0] == "   ":
                        deff.row2[0] = " 0 "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        print("")
                        continue
                if x == 5:
                    if deff.row2[2] == "   ":
                        deff.row2[2] = " 0 "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        print("")
                        continue
                if x == 6:
                    if deff.row2[4] == "   ":
                        deff.row2[4] = " 0 "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        print("")
                        continue

            if x <= 9:
                if x == 7:
                    if deff.row3[0] == "   ":
                        deff.row3[0] = " 0 "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        print("")
                        continue
                if x == 8:
                    if deff.row3[2] == "   ":
                        deff.row3[2] = " 0 "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        print("")
                        continue
                if x == 9:
                    if deff.row3[4] == "   ":
                        deff.row3[4] = " 0 "
                    else:
                        print("Das Feld ist bereits besetzt!")
                        print("")
                        continue
            deff.ausgabe()
            deff.runde = deff.runde + 1
            deff.pruf()
            continue

    if str(x) == "q":
        if deff.s1 > deff.s2:
            print("\nSpieler 2 ... du bist scheiße!")
        elif deff.s1 == deff.s2:
            print("\nGleichstand")
        else:
            print("\nSpieler 1 ... du bist scheiße!")

        break

    deff.zs()
    deff.ausgabe()
