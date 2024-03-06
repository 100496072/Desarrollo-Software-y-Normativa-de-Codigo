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

def testRoomReservtionTests(TestCase):
    @freeze_time("01/07/2024")

    def test_room_reservation_valido1(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/scr/JohnFiles"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_manager = HotelManager()
        value = my_manager.roomReservation(idcard="12345678Z",creditcard="5555555555555555",
                                           date_arrival="04/07/2024", name_and_surname="John Doe",phonenumber=ap,
                                           room_type="single",numdays="2")
        self.assertEqual(value, "1")

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_HotelReservation__idcard"] == "12345678":
                found = True
        self.assertTrue(found)