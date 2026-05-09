while True:

    print("Pandas piemeri:")
    print("1 - pandas.melt")
    print("2 - pandas.pivot")
    print("3 - pandas.qcut")
    print("4 - pandas.merge")
    print("5 - pandas.merge_ordered")
    print("6 - pandas.merge_asof")
    print("7 - pandas.concat")
    print("8 - pandas.get_dummies")
    print("9 - pandas.factorize")
    print("10 - pandas.to_numeric")
    print("11 - pandas.col")
    print("12 - pandas.eval")
    print("13 - pandas.lreshape")
    print("14 - guess_datetime_format")
    print("15 - pandas.util.hash_array")
    print("0 - Exit")

    choice = input("Izvēlies funkciju: ")

    if choice == "1":
        import Funkcijas.Funkcijas1

    elif choice == "2":
        import Funkcijas.Funkcijas2

    elif choice == "3":
        import Funkcijas.Funkcijas3

    elif choice == "4":
        import Funkcijas.Funkcijas4

    elif choice == "5":
        import Funkcijas.Funkcijas5

    elif choice == "6":
        import Funkcijas.Funkcijas6

    elif choice == "7":
        import Funkcijas.Funkcijas7

    elif choice == "8":
        import Funkcijas.Funkcijas8

    elif choice == "9":
        import Funkcijas.Funkcijas9

    elif choice == "10":
        import Funkcijas.Funkcijas10

    elif choice == "11":
        import Funkcijas.Funkcijas11

    elif choice == "12":
        import Funkcijas.Funkcijas12

    elif choice == "13":
        import Funkcijas.Funkcijas13

    elif choice == "14":
        import Funkcijas.Funkcijas14

    elif choice == "15":
        import Funkcijas.Funkcijas15

    elif choice == "0":
        print("Programma aizvērta")
        break

    else:
        print("Nepareiza izvēle")
