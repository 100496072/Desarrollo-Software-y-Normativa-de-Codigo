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
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("")
        data = {"Localizer": "d49c3ef42abd0183038e1f4ec296ed04","IdCard": "02564364W"}
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            json.dump(data, archivo, indent=4)
        my_hotelroom = HotelManager()
        room_key = my_hotelroom.guestArrival(input_file= file_store)

        self.assertEqual("639493603b7794ae1d633bd1b592a45455d192987a7001d0670a237b5a5af97a", room_key)

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_1(self):
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
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("")
        data = {"Localizer": "d49c3ef42abd0183038e1f4ec296ed04", "IdCard": "02564364W"}
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            for i in range(2):
                json.dump(data, archivo, indent=4)
                archivo.write("\n")

        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_guest_arrival_del_1(self):
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
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("")
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_2(self):
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
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("{")
        data = {"Localizer": "d49c3ef42abd0183038e1f4ec296ed04", "IdCard": "02564364W"}
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            json.dump(data, archivo, indent=4)

        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_2(self):
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
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("")
        data = {"Localizer": "d49c3ef42abd0183038e1f4ec296ed04", "IdCard": "02564364W"}
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            json.dump(data, archivo, indent=4)
        with open(file_store, "r", encoding="utf-8", newline="") as archivo:
            datos = archivo.read()
        pos = datos.find("{")
        datos_finales = datos[:pos] + "" + datos[pos+1:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_3(self):
        json_files_path = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = json_files_path + "store_reservation.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_reservation = HotelManager()
        my_reservation.roomReservation(idcard="02564364W", creditcard="5105105105105100",
                                       date_arrival="14/6/2024", name_and_surname="JOSE LOPEZ",
                                       phonenumber="912345678", room_type="SINGLE", numdays="1")

        json_files_path = str(Path.home()) + "/PycharmProjects/G81.2024.T01.EG2/src/JsonFiles/"
        file_store = json_files_path + "store_arrival.json"
        my_hotelroom = HotelManager()
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)
        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_3(self):
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
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("{}")
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_4(self):
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
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("")
        data = {"Localizer": "d49c3ef42abd0183038e1f4ec296ed04", "IdCard": "02564364W"}
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            json.dump(data, archivo, indent=4)
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            archivo.write("}")
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_4(self):
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
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("")
        data = {"Localizer": "d49c3ef42abd0183038e1f4ec296ed04", "IdCard": "02564364W"}
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            json.dump(data, archivo, indent=4)
        with open(file_store, "r", encoding="utf-8", newline="") as archivo:
            datos = archivo.read()
        pos = datos.find("}")
        datos_finales = datos[:pos] + "" + datos[pos + 1:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_5(self):
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
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("")
        data = {"Localizer": "d49c3ef42abd0183038e1f4ec296ed04", "IdCard": "02564364W"}
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            json.dump(data, archivo, indent=4)
        with open(file_store, "r", encoding="utf-8", newline="") as archivo:
            datos = archivo.read()
        pos = datos.find("{")
        datos_finales = datos[:pos] + "¡" + datos[pos + 1:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_6(self):
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
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("")
        data = {"Localizer": "d49c3ef42abd0183038e1f4ec296ed04", "IdCard": "02564364W"}
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            json.dump(data, archivo, indent=4)
        with open(file_store, "r", encoding="utf-8", newline="") as archivo:
            datos = archivo.read()
        pos = datos.find("{") + 1
        datos_finales = datos[:pos] + '"Localizer": "d49c3ef42abd0183038e1f4ec296ed04"' + datos[pos + 1:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")
