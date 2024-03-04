""""Parte 1 Ejercicio 2"""
from UC3MTravel import HotelManager

def main():
    """Funcion Principal"""
    Mng = HotelManager.HotelManager()
    Res = Mng.readDataFromJSOn("test.json")
    StrRes = str(Res)
    print(StrRes)
    print("CreditCard: " + Res.idcard)
    print(Res.localizer)

if __name__ == "__main__":
    main()
