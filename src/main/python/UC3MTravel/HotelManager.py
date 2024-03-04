"""Comentario"""

import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation

class HotelManager:
    """Comentario"""
    def __init__(self):
        pass

    def validateCreditCard( self, x ):
        """Comentario"""
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

    def readDataFromJSOn( self, fi):
        """Comentario"""
        try:
            with open(fi) as af:
                DATA = json.load(af)
        except FileNotFoundError as ae:
            raise HotelManagementException("Wrong file or file path") from ae
        except json.JSONDecodeError as ae:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ae


        try:
            ac = DATA["CreditCard"]
            ap = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z",creditcardNumb=ac,nAMeAndSURNAME="John Doe",
                                   phonenumber=ap,room_type="single",numdays=3)
        except KeyError as ae:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from ae
        if not self.validateCreditCard(ac):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req
