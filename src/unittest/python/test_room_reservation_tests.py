"""
Created by Marcos Romo Poveda in mar 2024
"""
from unittest import TestCase
from freezegun import freeze_time
from pathlib import Path
import os
import json
from UC3MTravel import HotelManager
from UC3MTravel import HotelManagementException

class testRoomReservtionTests(TestCase):
    @freeze_time("01/07/2024")
    def test_room_reservation_valide_1(self):

        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        value = my_reservation.roomReservation(idcard="02564364W",creditcard="5105105105105100",
                                           date_arrival="20/6/2024", name_and_surname="Luisa Gómez",
                                           phonenumber="912345678", room_type="SUITE",numdays="9")
        self.assertEqual(value, "dff22d19bfc3e273a34d6e8a81b3296e")

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_HotelReservation__idcard"] == "02564364W":
                found = True

        self.assertTrue(found)
        print("Test Valido 1 OK")

    @freeze_time("01/07/2024")
    def test_room_reservation_valide_2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)


        my_reservation = HotelManager()
        value = my_reservation.roomReservation(idcard="31427936T",creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ SANCHEZ",
                                           phonenumber="912345678", room_type="SINGLE",numdays="10")
        self.assertEqual(value, "07d98b3b39afabde7157be6196d8e90c")

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_HotelReservation__idcard"] == "31427936T":
                found = True

        self.assertTrue(found)
        print("Test Valido 2 OK")


    @freeze_time("01/07/2024")
    def test_room_reservation_notvalide_1(self):


        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                               date_arrival="21/03/2024", name_and_surname="jose Lopez",
                                               phonenumber="912345678", room_type="single", numdays="1")

        my_reservation = HotelManager()

        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                                   date_arrival="21/03/2024", name_and_surname="jose Lopez",
                                                   phonenumber="912345678", room_type="single", numdays="1")

        self.assertEqual(error.exception.message, "El cliente ya tenía una reserva.")
        print("Test No Valido 1 OK")

    @freeze_time("01/07/2024")
    def test_room_reservation_notvalide_2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        my_reservation.roomReservation(idcard="31427936T", creditcard="5105105105105100",
                                               date_arrival="21/03/2025", name_and_surname="jose Lopez",
                                               phonenumber="912345678", room_type="single", numdays="1")

        my_reservation = HotelManager()

        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="31427936T", creditcard="5105105105105100",
                                                   date_arrival="21/03/2024", name_and_surname="jose Lopez",
                                                   phonenumber="912345678", room_type="single", numdays="1")

        self.assertEqual(error.exception.message, "El cliente ya tenía una reserva.")
        print("Test No Valido 2 OK")

    @freeze_time("01/07/2024")
    def test_room_reservation_notvalide_3(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()

        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="51051051051051",
                                           date_arrival="21/03/2024", name_and_surname="jose Lopez",
                                           phonenumber="912345678", room_type="single", numdays="1")

        self.assertEqual(error.exception.message, "El número de tarjeta recibido no es válido o no tiene"
                                                  " un formato válido.")

        print("Test No Valido 3 OK")
