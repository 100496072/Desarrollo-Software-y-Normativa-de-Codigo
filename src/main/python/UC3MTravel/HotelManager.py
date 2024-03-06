"""Comentario"""

import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation

class HotelManager:
    """Comentario"""
    def __init__(self):
        pass

    def validateCreditCard(self, x):
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

    """
    def validateCreditCard(self, x):
        Suma = 0
        for i in range(len(x)):
            digit = int(x[i])
            if i % 2 == 0:  # Dígitos en posiciones impares
                digit *= 2
                if digit >= 10:
                    digit = digit - 9  # Restar 9 si el resultado es mayor o igual a 10
            Suma += digit

        if Suma % 10 == 0:
            return True
        return False
    """

    def readDataFromJSOn(self, fi):
        """Comentario"""
        try:
            with open(fi, encoding='utf-8') as af:
                DATA = json.load(af)
        except FileNotFoundError as ae:
            raise HotelManagementException("Wrong file or file path") from ae
        except json.JSONDecodeError as ae:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ae


        try:
            ac = DATA["CreditCard"]
            ap = DATA["phoneNumber"]
            req = HotelReservation(idcard="12345678Z",creditcard=ac, name_and_surname="John Doe",phonenumber=ap,
                                   room_type="single",numdays=3)
        except KeyError as ae:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from ae
        if not self.validateCreditCard(ac):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req

    def roomReservation(self, idcard:str, creditcard:str,  date_arrival:str, name_and_surname:str,
                        phonenumber:str, room_type:str, numdays:str):

        #validar credit card
        self.validateCreditCard(creditcard)
        #validar idcard
        #validad cada uno de los argumentos

        my_reservation = HotelReservation(idcard=idcard, creditcard=creditcard, date_arrival=date_arrival,
                                          name_and_surname=name_and_surname, phonenumber=phonenumber,
                                          room_type=room_type, numdays=numdays)
        #Instanciar hotel reservation
        #llamo al metodo locaizer

        #guardar los datos en un fichero almacen y comprobar que no estan repetidos

        return my_reservation.localizer
