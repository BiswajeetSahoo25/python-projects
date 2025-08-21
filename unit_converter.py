#  **UNIT CONVERTER**

def convert_km(km):
    km_to_m = km * 1000
    print(f"{km}km to m is: {km_to_m}m")
    km_to_cm = km * 100000
    print(f"{km}km to cm is: {km_to_cm}cm")
    km_to_mile = km * 0.621371
    print(f"{km}km to mile is: {km_to_mile}mile")


def main():
    # ask what to convert(distance,mass,volume)
    while True:
        print('what do you want to measaure(distance,mass,volume)')
        print('*' * 40)
    
        try:
            to_convert = int(
                input('Pess: 1 for distance, 2 for mass, 3 for volume, 4 for exit:'))
        except:
            print("invalid input")
            return

        match to_convert:
            case 1:
                print("input in (km, m, cm, mile)")
                distance_input = input().strip()
                if distance_input == "km":
                    km = float(input("km = "))
                    convert_km(km)
                    print('*' * 40)
                    main()
                elif distance_input == "m":
                    pass
                elif distance_input == "cm":
                    pass
                elif distance_input == "mile":
                    pass
                else:
                    print("invalid input")

            # case 2:
            #     print("input in (kg, g, pound, tonne)")
            #     mass_input = input().strip()
            #     if mass_input == "kg":
            #         pass
            #     elif mass_input == "g":
            #         pass
            #     elif mass_input == "pound":
            #         pass
            #     elif mass_input == "tonne":
            #         pass
            #     else:
            #         print("invalid input")

            # case 3:
            #     print("input in (l, ml)")
            #     volume_input = input().strip()
            #     if volume_input == "l":
            #         pass
            #     if volume_input == "ml":
            #         pass

            case 4:
                print("thank you")
                return

            case _:
                print("invalid input")
                return


main()
