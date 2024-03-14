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
    def test_room_reservation_valido1(self):

        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        value = my_reservation.roomReservation(idcard="02564364W",creditcard="5105105105105100",
                                           date_arrival="21/03/2024", name_and_surname="jose Lopez",
                                           phonenumber="912345678", room_type="single",numdays="1")
        self.assertEqual(value, "dff22d19bfc3e273a34d6e8a81b3296e")

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_HotelReservation__idcard"] == "02564364W":
                found = True

        self.assertTrue(found)
        print("Test 1 OK")

    @freeze_time("01/07/2024")

    def test_room_reservation_valido2(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        value = my_reservation.roomReservation(idcard="02564364W",creditcard="5105105105105100",
                                           date_arrival="21/03/2025", name_and_surname="jose Lopez",
                                           phonenumber="912345678", room_type="single",numdays="1")
        self.assertEqual(value, "e53d07cf86601890e75618a2dea07f41")

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_HotelReservation__idcard"] == "02564364W":
                found = True

        self.assertTrue(found)
        print("Test 2 OK")

    def test_room_reservation_not_valido3(self):

        my_reservation = HotelManager()

        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="51051051051051",
                                                   date_arrival="21/03/2024", name_and_surname="jose Lopez",
                                                   phonenumber="912345678", room_type="single", numdays="1")

        self.assertEqual(error.exception.message, "El número de tarjeta recibido no es válido o no tiene"
                                                  " un formato válido.")

        print("Test 3 OK")

