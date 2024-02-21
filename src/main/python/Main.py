""""Parte 1 Ejercicio 2"""
from UC3MTravel import HotelManager

def Main():
    """Funcion Principal"""
    Mng = HotelManager()
    Res = Mng.ReadDataFromJSOn("test.json")
    StrRes = str(Res)
    print(StrRes)
    print("CreditCard: " + Res.CREDITCARD)
    print(Res.LOCALIZER)

if __name__ == "__main__":
    Main()
