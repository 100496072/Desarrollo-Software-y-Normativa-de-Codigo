import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation

class HotelManager:
    def __init__(self):
        pass

    def ValidateCreditCard( self, x ):

        Suma = 0
        Contador = 0
        for i in range(len(x) - 1):
            if Contador % 2 == 0:
                Resultado = int(x[i]) * 2
                if Resultado >= 10:
                    Suma += 1 + (Resultado - 10)
                else:
                    Suma += Resultado
            else:
                Suma += int(x[i])

        if (Suma * 9) % 10 == int(x[15]):
            return True
        return False

    def ReadDataFromJSOn( self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z",creditcardNumb=c,nAMeAndSURNAME="John Doe",phonenumber=p,room_type="single",numdays=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateCreditCard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req
