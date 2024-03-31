"""Comentario"""

import json
import re
from pathlib import Path
from datetime import datetime
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation
from .HotelStay import HotelStay

class HotelManager:
    """Comentario"""

    def __init__(self):
        pass

    def validateCreditCard(self, x):
        """Comentario"""
        if not isinstance(x, str):
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

        if not isinstance(x, str):
            raise HotelManagementException("El DNI no es válido.")
        if len(x) == 9 and x[:-1].isdigit():

            Letras = "TRWAGMYFPDXBNJZSQVHLCKE"
            Numero = int(x[:-1])
            Letra = x[-1].upper()
            LetraCalculada = Letras[Numero % 23]

            if Letra != LetraCalculada:
                raise HotelManagementException("El DNI no es válido.")
        else:
            raise HotelManagementException("El DNI no es válido.")

    def validateNameSurname(self, x):
        """Comentario"""
        if not isinstance(x, str):
            raise HotelManagementException("La cadena del nombre y apellidos no es válida.")
        if len(x) >= 0 and len(x) <= 50:
            Separacion = x.split()
            if len(Separacion) < 2:
                raise HotelManagementException("La cadena del nombre y apellidos no es válida.")
        else:
            raise HotelManagementException("La cadena del nombre y apellidos no es válida.")

    def validatePhoneNumber(self, x):
        """Comentario"""
        if not isinstance(x, str):
            raise HotelManagementException("El número de teléfono no es válido.")
        if len(x) != 9:
            raise HotelManagementException("El número de teléfono no es válido.")

    def validateRoomType(self, x):
        """Comentario"""
        if x.lower() not in ("single", "double", "suite"):
            raise HotelManagementException("El tipo de habitación no es válido.")

    def validateArrival(self, x):
        """Comentario"""
        if not isinstance(x, str):
            raise HotelManagementException("La fecha de entrada no es válida")
        try:
            datetime.strptime(x, "%d/%m/%Y")
        except ValueError as Exc:
            raise HotelManagementException("La fecha de entrada no es válida") from Exc

    def validateNumDays(self, x):
        """Comentario"""
        if not isinstance(x, str):
            raise HotelManagementException("El número de días no es válido.")
        if int(x) < 1 or int(x) > 10:
            raise HotelManagementException("El número de días no es válido.")

    def readDataFromJSOn(self, fi):
        """Comentario"""
        try:
            with open(fi, encoding='utf-8') as Af:
                DATA = json.load(Af)
        except FileNotFoundError as Ae:
            raise HotelManagementException("Wrong file or file path") from Ae
        except json.JSONDecodeError as Ae:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from Ae

        try:
            Ac = DATA["CreditCard"]
            Ap = DATA["phoneNumber"]
            Req = HotelReservation(idcard="12345678Z", creditcard=Ac, date_arrival="date_arrival",
                                   name_and_surname="John Doe", phonenumber=Ap, room_type="single", numdays=3)
        except KeyError as Ae:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from Ae
        if not self.validateCreditCard(Ac):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return Req

    def roomReservation(self, idcard: str, creditcard: str, date_arrival: str, name_and_surname: str,
                        phonenumber: str, room_type: str, numdays: str):
        """Comentario"""

        try:
            self.validateCreditCard(creditcard)
            self.validateIdcard(idcard)
            self.validateArrival(date_arrival)
            self.validateNameSurname(name_and_surname)
            self.validatePhoneNumber(phonenumber)
            self.validateRoomType(room_type)
            self.validateNumDays(numdays)

        except ValueError as Ea:
            print({Ea})

        MyReservation = HotelReservation(idcard=idcard, creditcard=creditcard, date_arrival=date_arrival,
                                          name_and_surname=name_and_surname, phonenumber=phonenumber,
                                          room_type=room_type, numdays=numdays)

        # Llamo la ruta del fichero almacén, donde almacenaremos todas las reservas
        JsonFilesPath = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        FileStore = JsonFilesPath + "store_reservation.json"

        # Comprobamos que dicho fichero existe
        try:
            with open(FileStore, "r", encoding="utf-8", newline="") as File:
                DataList = json.load(File)
        except FileNotFoundError:
            DataList = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        # Guardar los datos en un fichero almacen y comprobar que no están repetidos

        for Item in DataList:
            if Item["_HotelReservation__idcard"] == idcard:
                raise HotelManagementException("El cliente ya tenía una reserva.")
        DataList.append(MyReservation.__dict__)

        try:
            with open(FileStore, "w", encoding="utf-8", newline="") as File:
                json.dump(DataList, File, indent=2)
        except FileNotFoundError as ex:
            raise HotelManagementException("Wrong File or File path") from ex

        return MyReservation.localizer

    def guestArrival(self, input_file: json):
        "Comentario"
        try:
            with open(input_file, "r", encoding="utf-8", newline="") as File:
                InputData = json.load(File)
        except FileExistsError:
            InputData = {}
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        if len(InputData) != 2:
            raise HotelManagementException("El JSON no tiene la estructura esperada")
        for _ in InputData:
            Claves = iter(InputData.keys())
            PrimeraClave = next(Claves)
            if PrimeraClave != "Localizer":
                raise HotelManagementException("El JSON no tiene la estructura esperada")
            SegundaClave = next(Claves)
            if SegundaClave != "IdCard":
                raise HotelManagementException("El JSON no tiene la estructura esperada")
            RegexPattern = re.compile("[0-9, a-z]{32}")
            ValidRegexPatternLocalizer = RegexPattern.fullmatch(InputData[PrimeraClave])
            if ValidRegexPatternLocalizer is None:
                raise HotelManagementException("El JSON no tiene la estructura esperada")

            RegexPattern = re.compile("[0-9]{8}[A-Z]")
            ValidRegexPatternLocalizer = RegexPattern.fullmatch(InputData[SegundaClave])
            if ValidRegexPatternLocalizer is None:
                raise HotelManagementException("El JSON no tiene la estructura esperada")

        JsonFilesPath = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        FileStore = JsonFilesPath + "store_reservation.json"

        try:
            with open(FileStore, "r", encoding="utf-8", newline="") as File:
                InputList = json.load(File)
        except FileNotFoundError:
            InputList = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

        #Hay que poner esto como un while, pero aquí lo que hacemos es buscar en las reservas para comprobar que el
        # localizador está en nuestro almacén
        for Search in InputList:
            Found = False
            if InputData[PrimeraClave] == Search["_HotelReservation__localizer"]:
                Found = True
                Reservation = Search
        if not Found:
            raise HotelManagementException("El localizador no se corresponde con los datos almacenados")
        if Reservation["_HotelReservation__reservation_date"] != self.fechaHoy():
            raise HotelManagementException("La fecha de llegada no se corresponde con la fecha de reserva")
        MyRoom = HotelStay(Reservation["_HotelReservation__idcard"], Reservation["_HotelReservation__localizer"],
            Reservation["_HotelReservation__num_days"], Reservation["_HotelReservation__roomtype"])

        # Llamo la ruta del fichero almacén, donde almacenaremos todas los check_in
        JsonFilesPath = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        FileStore = JsonFilesPath + "check_in.json"

        # Comprobamos que dicho fichero existe
        try:
            with open(FileStore, "r", encoding="utf-8", newline="") as File:
                DataList = json.load(File)
        except FileNotFoundError:
            DataList = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        # Guardar los datos en un fichero almacen y comprobar que no están repetidos
        DataList.append(MyRoom.__dict__)
        try:
            with open(FileStore, "w", encoding="utf-8", newline="") as File:
                json.dump(DataList, File, indent=2)
        except FileNotFoundError as ex:
            raise HotelManagementException("Wrong File or File path") from ex
        return MyRoom.room_key

    def guestCheckout(self, room_key):
        """Método que comprueba la salida del cliente"""
        JsonFilesPath = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        FileStore = JsonFilesPath + "check_in.json"

        try:
            with open(FileStore, "r", encoding="utf-8", newline="") as File:
                InputList = json.load(File)
        except FileNotFoundError:
            InputList = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

        #Hay que poner esto como un while, buscamos si la roomkey está guardad en nuestro almacén de check in,
        # entonces hay una habitación
        for Search in InputList:
            Found = False
            if room_key == Search["_HotelStay__roomkey"]:
                Found = True
                Reservation = Search
            if not Found:
                raise HotelManagementException("El código de habitación no estaba registrado.")

        #Si no se cumple la comprobación, es que se está dejando la habitación en un día que no era el de finalización
        if Reservation["_HotelStay__departure"] != self.fechaHoy():
            raise HotelManagementException("La fecha de salida no es válida")

        return True

    def fechaHoy(self):
        """Calcula y devuelve la fecha de hoy"""
        JustNow = datetime.utcnow()
        Fecha = JustNow.timestamp()
        return Fecha
