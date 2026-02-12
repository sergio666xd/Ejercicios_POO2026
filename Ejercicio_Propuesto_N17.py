import math

class area_longitud:
    @staticmethod
    def area(radio):
        return math.pi * radio * radio
    
    @staticmethod
    def longitud(radio):
        return 2 * math.pi * radio


def main():

    r = float(input("Ingrese el radio del círculo: "))

    area = area_longitud.area(r)
    longitud = area_longitud.longitud(r)
    print(f"Radio: {r}")
    print(f"Área: {area:.4f}")
    print(f"Longitud (circunferencia): {longitud:.4f}")


if __name__ == "__main__":
    main()
