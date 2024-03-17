"""
Created by Marcos Romo Poveda in mar 2024
"""
import unittest

from UC3MTravel.HotelManager import HotelManager
from UC3MTravel.HotelManager import HotelManagementException
import os
import json
from pathlib import Path
from freezegun import freeze_time

class TestRoomReservation(unittest.TestCase):

    def setUp(self):
        """Creamos las variables de entrada, se ejecutará por cada prueba"""
        self.my_reservation = HotelManager()

    @freeze_time("2024-06-14")

    def test_room_reservation_valid1(self):
        """Todos los valores introducidos son válidos"""
        JSON_FILES_PATH = str(Path.home()) + "Pycharmproyects/G81.2024.T98.EG2" \
                                             "/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        localizer_obj = HotelManager()
        localizer = localizer_obj.room_reservation(
            creditCard="5105105105105100", name_surname="Jose López",
            id_card="12448346X", phone=911234567, room_type="single",
            date_arrival="14/06/2024", days=2)

        value = self.my_reservation.room_reservation(
            creditCard="5105105105105100", name_surname="Jose López",
            id_card="12448346X", phone=911234567, room_type="single",
            date_arrival="14/06/2024", days=2)
        self.assertEqual(value, localizer)
