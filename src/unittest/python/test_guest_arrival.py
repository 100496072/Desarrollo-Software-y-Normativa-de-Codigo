"""
Created by Luca, Marcos and Alicia in mar 2024
"""
from unittest import TestCase
from freezegun import freeze_time
from pathlib import Path
import os
import json
from UC3MTravel import HotelManager
from UC3MTravel import HotelManagementException
from unittest import TestCase


class TestGuestArrival(TestCase):
    @freeze_time("01/07/2024")
    def test_guest_arrival_valido(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                               date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                               phonenumber="912345678", room_type="SINGLE", numdays="1")

        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_arrival.json"

        my_hotelroom = HotelManager()
        room_key=my_hotelroom.guest_arrival(input_file= file_store)

        self.assertEqual("639493603b7794ae1d633bd1b592a45455d192987a7001d0670a237b5a5af97a", room_key)


