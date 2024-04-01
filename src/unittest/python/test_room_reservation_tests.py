"""
Created by Luca, Marcos and Alicia in mar 2024
"""
import os
import json
from unittest import TestCase
from freezegun import freeze_time
from pathlib import Path
from UC3MTravel import HotelManager
from UC3MTravel import HotelManagementException


class TestRoomReservtionTests(TestCase):
    @freeze_time("01/07/2024")
    def test_room_reservation_valido_01(self):
        """Caso válido"""
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        value = my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                               date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                               phonenumber="912345678", room_type="SINGLE", numdays="1")
        self.assertEqual(value, "d49c3ef42abd0183038e1f4ec296ed04")

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_HotelReservation__idcard"] == "02564364W":
                found = True

        self.assertTrue(found)
        print("Test Valido 1 OK")

    @freeze_time("01/07/2024")
    def test_room_reservation_valido_02(self):
        """Caso válido"""
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        value = my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                               date_arrival="19/6/2024",
                                               name_and_surname="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab aaaaaaaaaaaaaaa",
                                               phonenumber="912345678", room_type="DOUBLE", numdays="2")
        self.assertEqual(value, "07888add4cec2804f846afcd2a3b06b7")

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_HotelReservation__idcard"] == "02564364W":
                found = True

        self.assertTrue(found)
        print("Test Valido 2 OK")

    @freeze_time("01/07/2024")
    def test_room_reservation_valido_03(self):
        """Caso válido"""
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        value = my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                               date_arrival="20/6/2024", name_and_surname="Luisa Gómez",
                                               phonenumber="912345678", room_type="SUITE", numdays="9")
        self.assertEqual(value, "c6ef506e7f77dfc7221ca4be93ad6643")

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_HotelReservation__idcard"] == "02564364W":
                found = True

        self.assertTrue(found)
        print("Test Valido 3 OK")

    @freeze_time("01/07/2024")
    def test_room_reservation_valido_04(self):
        """Caso válido"""
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        value = my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                               date_arrival="14/6/2024",
                                               name_and_surname="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab aaaaaaaaaaaaaaa",
                                               phonenumber="912345678", room_type="SINGLE", numdays="1")
        self.assertEqual(value, "4561fabadaaab3e451ee48dc4d7b5f16")

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_HotelReservation__idcard"] == "02564364W":
                found = True

        self.assertTrue(found)
        print("Test Valido 4 OK")

    @freeze_time("01/07/2024")
    def test_room_reservation_valido_05(self):
        """Caso válido"""
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        value = my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                               date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ SANCHEZ",
                                               phonenumber="912345678", room_type="SINGLE", numdays="10")
        self.assertEqual(value, "4b1dd4791621c28e2fc8a9737184a65c")

        with open(file_store, "r", encoding="utf-8", newline="") as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_HotelReservation__idcard"] == "02564364W":
                found = True

        self.assertTrue(found)
        print("Test Valido 5 OK")

    @freeze_time("01/07/2024")
    def test_room_reservation_notvalido_01(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105101",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El número de tarjeta recibido no es válido o no tiene un formato "
                                                  "válido.")

        print("Test No Valido 1 OK")

    def test_room_reservation_notvalido_02(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard=5105105105105100,
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El número de tarjeta recibido no es válido o no tiene un formato "
                                                  "válido.")

        print("Test No Valido 2 OK")

    def test_room_reservation_notvalido_03(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="51051051051051000",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El número de tarjeta recibido no es válido o no tiene un formato "
                                                  "válido.")

        print("Test No Valido 3 OK")

    def test_room_reservation_notvalido_04(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="510510510510510",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El número de tarjeta recibido no es válido o no tiene un formato "
                                                  "válido.")

        print("Test No Valido 4 OK")

    def test_room_reservation_notvalido_05(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="06611518M", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El DNI no es válido.")

        print("Test No Valido 5 OK")

    def test_room_reservation_notvalido_06(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="0661151FM", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El DNI no es válido.")

        print("Test No Valido 6 OK")

    def test_room_reservation_notvalido_07(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="006611518?", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El DNI no es válido.")

        print("Test No Valido 7 OK")

    # Este test que consistiria en meter el idcard como formato int no se puede probar ya que python da un error
    """def test_room_reservation_notvalido_08(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard=int("02564364W"), creditcard="5105105105105100",
                                                   date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                                   phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El DNI no es válido.")

        print("Test No Valido 8 OK")"""

    def test_room_reservation_notvalido_09(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="006611518F", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El DNI no es válido.")

        print("Test No Valido 9 OK")

    def test_room_reservation_notvalido_10(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="06611518M", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El DNI no es válido.")

        print("Test No Valido 10 OK")

    def test_room_reservation_notvalido_11(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSELOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "La cadena del nombre y apellidos no es válida.")

        print("Test No Valido 11 OK")

    def test_room_reservation_notvalido_12(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOS1 LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "La cadena del nombre y apellidos no es válida.")

        print("Test No Valido 12 OK")

    def test_room_reservation_notvalido_13(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE  LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "La cadena del nombre y apellidos no es válida.")

        print("Test No Valido 13 OK")

    # Este test que consistiria en meter el name_and_surname como formato int no se puede probar ya que python da un
    # error
    """def test_room_reservation_notvalido_14(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                                   date_arrival="14/6/2024", name_and_surname=int("JOSE LOPEZ"),
                                                   phonenumber="912345678", room_type="SINGLE", numdays="1")


        self.assertEqual(error.exception.message, "La cadena del nombre y apellidos no es válida.")

        print("Test No Valido 14 OK")"""

    def test_room_reservation_notvalido_15(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024",
                                           name_and_surname="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab aaaaaaaaaaaaaaaaa",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "La cadena del nombre y apellidos no es válida.")

        print("Test No Valido 15 OK")

    def test_room_reservation_notvalido_16(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="Luis Val",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "La cadena del nombre y apellidos no es válida.")

        print("Test No Valido 16 OK")


    def test_room_reservation_notvalido_17(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="91234567A", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El número de teléfono no es válido.")

        print("Test No Valido 17 OK")

    def test_room_reservation_notvalido_18(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber=912345678, room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El número de teléfono no es válido.")

        print("Test No Valido 18 OK")
    def test_room_reservation_notvalido_19(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="91234567", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El número de teléfono no es válido.")

        print("Test No Valido 19 OK")
    def test_room_reservation_notvalido_20(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="9123456789", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "El número de teléfono no es válido.")

        print("Test No Valido 20 OK")


    def test_room_reservation_notvalido_21(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="TRIPLE", numdays="1")

        self.assertEqual(error.exception.message, "El tipo de habitación no es válido.")

        print("Test No Valido 21 OK")

    # Este test que consistiria en meter el room_type como formato int no se puede probar ya que python da un error
    """def test_room_reservation_notvalido_22(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type=int("SINGLE"), numdays="1")

        self.assertEqual(error.exception.message, "El tipo de habitación no es válido.")

        print("Test No Valido 22 OK")"""

    def test_room_reservation_notvalido_23(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="6a/227/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "La fecha de entrada no es válida.")

        print("Test No Valido 23 OK")

    def test_room_reservation_notvalido_24(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival=int(14/6/2024), name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="1")

        self.assertEqual(error.exception.message, "La fecha de entrada no es válida.")

        print("Test No Valido 24 OK")

    def test_room_reservation_notvalido_25(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="a")

        self.assertEqual(error.exception.message, "El número de días no es válido.")

        print("Test No Valido 25 OK")

    def test_room_reservation_notvalido_26(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays=1)

        self.assertEqual(error.exception.message, "El número de días no es válido.")

        print("Test No Valido 26 OK")

    def test_room_reservation_notvalido_27(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="0")

        self.assertEqual(error.exception.message, "El número de días no es válido.")

        print("Test No Valido 27 OK")

    def test_room_reservation_notvalido_28(self):
        JSON_FILES_PATH = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = JSON_FILES_PATH + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                           date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                           phonenumber="912345678", room_type="SINGLE", numdays="11")

        self.assertEqual(error.exception.message, "El número de días no es válido.")

        print("Test No Valido 28 OK")
