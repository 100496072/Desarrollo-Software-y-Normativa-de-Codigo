import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation

class HotelManager:
    def __init__(self):

        pass

    def validatecreditcard( self, x ):
        Suma = 0
        contador = 0
        while contador != 15:
            if contador%2 == 0:
                Resultado = int(x[contador]) * 2
                if Resultado - 10 >= 0:
                    Suma += 1 + (Resultado - 10)
                else:
                    Suma += Resultado
            else:
                Suma += int(x[contador])
            contador += 1

        if int(str(Suma*9)[-1]) == int(x[15]):
            return True
        else:
            return False

    def ReaddatafromJSOn( self, fi):

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
        if not self.validatecreditcard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req