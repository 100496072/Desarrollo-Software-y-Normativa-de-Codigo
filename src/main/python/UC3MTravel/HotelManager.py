"""Comentario"""

import json
from pathlib import Path
from datetime import datetime
from UC3MTravel import HotelManagementException
from UC3MTravel import HotelReservation


class HotelManager:
    """Comentario"""
    def __init__(self):
        pass

    def validateCreditCard(self, x):
        """Comentario"""
        if type(x) is not str:
            raise HotelManagementException("El número de tarjeta recibido no es válido o no tiene un formato válido.")
        if len(x) == 16:
            Suma = 0
            for i in range(len(x) - 1):
                if not x[i].isdigit():
                    raise HotelManagementException(
                        "El número de tarjeta recibido no es válido o no tiene un formato válido.")
                if i % 2 == 0:
                    Resultado = int(x[i]) * 2
                    if Resultado >= 10:
                        Suma += 1 + (Resultado - 10)
                    else:
                        Suma += Resultado
                else:
                    Suma += int(x[i])
            if x[15].isdigit() and (Suma * 9) % 10 == int(x[15]):
                return None
            raise HotelManagementException(
                    "El número de tarjeta recibido no es válido o no tiene un formato válido.")
        raise HotelManagementException("El número de tarjeta recibido no es válido o no tiene un formato válido.")

    def validateIdcard(self, x):
        """Comentario"""

        if type(x) is not str:
            raise HotelManagementException("El DNI no es válido.")
        if len(x) == 9 and x[:-1].isdigit():

            letras = "TRWAGMYFPDXBNJZSQVHLCKE"
            numero = int(x[:-1])
            letra = x[-1].upper()
            letra_calculada = letras[numero % 23]

            if letra != letra_calculada:
                raise HotelManagementException("El DNI no es válido.")
        else:
            raise HotelManagementException("El DNI no es válido.")

    def validateNameSurname(self, x):
        """Comentario"""
        if type(x) is not str:
            raise HotelManagementException("La cadena del nombre y apellidos no es válida.")
        if len(x) >= 0 and len(x) <= 50:
            separacion = x.split()
            if len(separacion) < 2:
                raise HotelManagementException("La cadena del nombre y apellidos no es válida.")
        else:
            raise HotelManagementException("La cadena del nombre y apellidos no es válida.")

    def validatePhoneNumber(self, x):
        """Comentario"""
        if type(x) is not str:
            raise HotelManagementException("El número de teléfono no es válido.")
        if len(x) != 9:
            raise HotelManagementException("El número de teléfono no es válido.")

    def validateRoomType(self, x):
        """Comentario"""
        if x != "single" and "double" and "suite":
            raise HotelManagementException("El tipo de habitación no es válido.")

    def validateArrival(self, x):
        """Comentario"""
        if type(x) is not str:
            raise HotelManagementException("La fecha de entrada no es válida")
        try:
            datetime.strptime(x, "%d/%m/%Y")
        except ValueError as exc:
            raise HotelManagementException("La fecha de entrada no es válida") from exc

    def validateNumDays(self, x):
        """Comentario"""
        if type(x) is not str:
            raise HotelManagementException("El número de días no es válido.")
        if int(x) < 1 or int(x) > 10:
            raise HotelManagementException("El número de días no es válido.")


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

        try:
            self.validateCreditCard(creditcard)
            self.validateIdcard(idcard)
            self.validateArrival(date_arrival)
            self.validateNameSurname(name_and_surname)
            self.validatePhoneNumber(phonenumber)
            self.validateRoomType(room_type)
            self.validateNumDays(numdays)

        except ValueError as eA:
            print({eA})

        my_reservation = HotelReservation.HotelReservation(idcard=idcard, creditcard=creditcard,
                                                         date_arrival=date_arrival,
                                          name_and_surname=name_and_surname, phonenumber=phonenumber,
                                          room_type=room_type, numdays=numdays)

        #Llamo la ruta del fichero almacén, donde almacenaremos todas las reservas
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"

        # Comprobamos que dicho fichero existe
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            data_list = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        # Guardar los datos en un fichero almacen y comprobar que no están repetidos


        for item in data_list:
            if item["_HotelReservation__idcard"] == idcard:
                raise HotelManagementException("El cliente ya tenía una reserva.")
        data_list.append(my_reservation.__dict__)

        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise HotelManagementException("Wrong file or file path") from ex


        return my_reservation.localizer
