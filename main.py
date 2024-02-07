""""Parte 1 Ejercicio 2"""
from UC3MTravel import HotelManager


def main():
    """Funcion Principal"""
    mng = HotelManager()
    res = mng.ReaddatafromJSOn("test.json")
    strRes = res.__str__()
    print(strRes)
    print("CreditCard: " + res.CREDITCARD)
    print(res.LOCALIZER)

if __name__ == "__main__":
    main()
