"""
Created by Luca, Marcos and Alicia in mar 2024
"""
from unittest import TestCase
import os
import json
from pathlib import Path
from freezegun import freeze_time
from UC3MTravel import HotelManager
from UC3MTravel import HotelManagementException



class testRoomReservtionTests(TestCase):

    """def test1(self):
        "Camino a seguir considerando que no se encuentra el archivo de los check in"
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        reserva = HotelManager()
        reserva.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                phonenumber="912345678", room_type="SINGLE", numdays="1")
        file = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/store_arrival.json"
        key = reserva.guestArrival(file)"""

    """def test2(self):
        "Camino a seguir considerando que el formato del archivo de los check in no es válido"
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        reserva = HotelManager()
        reserva.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                phonenumber="912345678", room_type="SINGLE", numdays="1")
        file = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/store_arrival.json"
        key = reserva.guestArrival(file)"""

    def test3(self):
        "Camino a seguir considerando que no se encuentra el código de la habitación"
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        reserva = HotelManager()
        key = "2j93j3j9rjr904jr94j0rj9"
        with self.assertRaises(HotelManagementException) as error:
            reserva.guestCheckout(key)
        self.assertEqual(error.exception.message, "Código de habitación no registrado.")

    @freeze_time("14/6/2024")
    def test4(self):
        "Camino a seguir considerando que la fecha de salida no es válida"
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        reserva = HotelManager()
        reserva.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                phonenumber="912345678", room_type="SINGLE", numdays="1")
        file = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/store_arrival.json"
        key = reserva.guestArrival(file)
        with self.assertRaises(HotelManagementException) as error:
            reserva.guestCheckout(key)
        self.assertEqual(error.exception.message, "La fecha de salida no es válida")

    """def test5(self):
        "Camino a seguir considerando que no se encuentra el archivo para los check out"
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        reserva = HotelManager()
        reserva.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                phonenumber="912345678", room_type="SINGLE", numdays="1")
        file = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/store_arrival.json"
        key = reserva.guestArrival(file)"""

    """def test6(self):
        "Camino a seguir considerando que el formato del archivo para los check out no es valido"
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        reserva = HotelManager()
        reserva.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                phonenumber="912345678", room_type="SINGLE", numdays="1")
        file = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/store_arrival.json"
        key = reserva.guestArrival(file)"""

    """def test7(self):
        "Camino a seguir considerando que ha habido un error a la hora de abrir en modo"
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        "escritura el archivo de los check out"
        reserva = HotelManager()
        reserva.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                phonenumber="912345678", room_type="SINGLE", numdays="1")
        file = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/store_arrival.json"
        key = reserva.guestArrival(file)"""

    @freeze_time("15/6/2024")
    def test8(self):
        "Camino idóneo"
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        reserva = HotelManager()
        """reserva.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                phonenumber="912345678", room_type="SINGLE", numdays="1")
        file = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/store_arrival.json"
        key = reserva.guestArrival(file)
        result = reserva.guestCheckout(key)
        self.assertTrue(result)"""
        check_in_data = [{"_HotelStay__roomkey": "123", "_HotelStay__departure": self.fechaHoy()}]
        with open(self.temp_check_in_file, "w") as f:
            json.dump(check_in_data, f)

        result = reserva.guestCheckout("123")
        self.assertTrue(result)

