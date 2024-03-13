"""Comentario"""

import json
from pathlib import Path
from datetime import datetime
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation

class HotelManager:
    """Comentario"""
    def __init__(self):
        pass

    def validateCreditCard(self, x):
        """Comentario"""
        Suma = 0
        for i in range(len(x) - 1):
            if i % 2 == 0:
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

    def validateIdcard(self, x):
        """Comentario"""
        if 1 == 1:
            return True
        return False

    def validateNameSurname(self, x):
        """Comentario"""
        if len(x) >= 0 and len(x) <= 50:
            separacion = x.split()
            if len(separacion) >= 2:
                return True
        return False

    def validatePhoneNumber(self, x):
        """Comentario"""
        if len(x) == 9:
            return True
        return False

    def validateRoomType(self, x):
        """Comentario"""
        if x == "single" or "double" or "suite":
            return True
        return False

    def validateArrival(self, x):
        """Comentario"""
        try:
            datetime.strptime(x, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def validateNumDays(self, x):
        """Comentario"""
        if int(x) >= 1 and int(x) <= 10:
            return True
        return False

    def verificacion(self, creditcard, idcard, name_and_surname, phonenumber, room_type, date_arrival, numdays):
        if not creditcard:
            raise ValueError("El número de tarjeta recibido no es válido o no tiene un formato válido.")
        if not idcard:
            raise ValueError("El DNI no es válido.")
        if not name_and_surname:
            raise ValueError("La cadena del nombre y apellidos no es válida.")
        if not phonenumber:
            raise ValueError("El número de teléfono no es válido.")
        if not room_type:
            raise ValueError("El tipo de habitación no es válido.")
        if not date_arrival:
            raise ValueError("La fecha de entrada no es válida")
        if not numdays:
            raise ValueError("El número de días no es válido.")

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
            req = HotelReservation(idcard="12345678Z",creditcard=ac, date_arrival="date_arrival",
                                   name_and_surname="John Doe",phonenumber=ap, room_type="single",numdays=3)
        except KeyError as ae:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from ae
        if not self.validateCreditCard(ac):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req

    def roomReservation(self, idcard:str, creditcard:str,  date_arrival:str, name_and_surname:str,
                        phonenumber:str, room_type:str, numdays:str):
        """Comentario"""
        validecreditcard = self.validateCreditCard(creditcard)
        valideidtcard = self.validateIdcard(idcard)
        validenamesurname = self.validateNameSurname(name_and_surname)
        validephonenumber = self.validatePhoneNumber(phonenumber)
        valideroomtype = self.validateRoomType(room_type)
        validearrival = self.validateArrival(date_arrival)
        validenumdays = self.validateNumDays(numdays)

        try:
            self.verificacion(validecreditcard, valideidtcard, validenamesurname, validephonenumber, valideroomtype,
                              validearrival, validenumdays)
        except ValueError as e:
            print({e})



        my_reservation = HotelReservation(idcard=idcard, creditcard=creditcard, date_arrival=date_arrival,
                                          name_and_surname=name_and_surname, phonenumber=phonenumber,
                                          room_type=room_type, numdays=numdays)

        #Llamo la ruta del fichero almacén, donde almacenaremos todas las reservas
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"

        # Comprobamos que dicho fichero existe
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            data_list = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format")
        # Guardar los datos en un fichero almacen y comprobar que no están repetidos

        # Guardar la reserva en el fichero almacén
        # Devolver el localizador de la reserva
        return my_reservation.localizer
