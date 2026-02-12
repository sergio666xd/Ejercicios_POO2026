class edades:
    @staticmethod
    def calc_edalberto(edad):
        return 2/3 * edad

    @staticmethod
    def calc_edana(edad):
        return 4/3 * edad

    @staticmethod
    def calc_edmama(edjuan,edalberto,edana):
        return edjuan + edalberto + edana

def main():
    edjuan = float(input("Ingrese la edad de Juan: "))
    edalberto = edades.calc_edalberto(edjuan)
    edana = edades.calc_edana(edjuan)
    edmama = edades.calc_edmama(edjuan,edalberto,edana)
    
    print(f"LAS EDADES SON: ALBERTO = {edalberto:.0f}, JUAN = {edjuan:.0f}, ANA = {edana:.0f}, MAMA = {edmama:.0f}")

if __name__ == "__main__":
    main()