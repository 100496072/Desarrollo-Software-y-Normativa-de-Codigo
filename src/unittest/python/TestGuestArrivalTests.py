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
    """Tests del método guest_arrival"""
    @freeze_time("01/07/2024")
    def testGuestArrivalValido(self):
        """Caso válido"""
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
    def testGuestArrivalDup1(self):
        """Se duplica el nodo 1"""
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
            for _ in range(2):
                json.dump(data, archivo, indent=4)
                archivo.write("\n")

        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    def testGuestArrivalDel1(self):
        """Eliminamos el nodo 1"""
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
    def testGuestArrivalDup2(self):
        """Duplicamos el nodo 2"""
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
    def testGuestArrivalDel2(self):
        """Eliminamos el nodo 2"""
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
    def testGuestArrivalDup3(self):
        """Duplicamos el nodo 3"""
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
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write("")
        data = {"Localizer": "d49c3ef42abd0183038e1f4ec296ed04", "IdCard": "02564364W"}
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            json.dump(data, archivo, indent=4)
        with open(file_store, "r", encoding="utf-8", newline="") as archivo:
            datos = archivo.read()
        caracter_buscado = '{'
        pos = 0
        for _ in range(1):
            pos = datos.find(caracter_buscado, pos)
        long = len(caracter_buscado)
        relleno = '"Localizer": "d49c3ef42abd0183038e1f4ec296ed04","IdCard": "02564364W"'
        datos_finales = datos[:pos] + relleno + relleno + datos[pos + 2*long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)
        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel3(self):
        """Eliminamos el nodo 3"""
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
    def testGuestArrivalDup4(self):
        """Duplicamos el nodo 4"""
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
    def testGuestArrivalDel4(self):
        """Eliminamos el nodo 4"""
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
    def testGuestArrivalMod5(self):
        """Modificamos el nodo 5"""
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
        datos_finales = datos[:pos] + '\n"Localizer": "d49c3ef42abd0183038e1f4ec296ed04"' + datos[pos + 1:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_6(self):
        """Eliminamos el nodo 6"""
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
        data = {"IdCard": "02564364W"}
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            json.dump(data, archivo, indent=4)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_7(self):
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
        pos = datos.find(",")
        datos_finales = datos[:pos] + ",," + datos[pos + 1:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_7(self):
        """Eliminamos el nodo 7"""
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
        data = { "IdCard": "02564364W"}
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            json.dump(data, archivo, indent=4)
        with open(file_store, "r", encoding="utf-8", newline="") as archivo:
            datos = archivo.read()
        pos = datos.find("{")
        datos_finales = datos[:pos] + "{\n ," + datos[pos + 1:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)
        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_8(self):
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
        pos = datos.find(",")
        datos_finales = datos[:pos] + ',\n"IdCard": "02564364W"' + datos[pos + 1:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_8(self):
        """Eliminamos el nodo 8"""
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
        data = {"Localizer": "d49c3ef42abd0183038e1f4ec296ed04"}
        with open(file_store, "a", encoding="utf-8", newline="") as archivo:
            json.dump(data, archivo, indent=4)
        with open(file_store, "r", encoding="utf-8", newline="") as archivo:
            datos = archivo.read()
        pos = datos.find("}")
        datos_finales = datos[:pos] + ',\n}' + datos[pos + 1:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_9(self):
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
        datos_finales = datos[:pos] + "¡" + datos[pos + 1:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_10(self):
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
        pos = datos.find('"Localizer"') -1
        datos_finales = datos[:pos] + '"Localizer"' + datos[pos + 1:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_10(self):
        """Eliminamos el nodo 10"""
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
        caracter_buscado = '"Localizer"'
        pos = datos.find(caracter_buscado)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_11(self):
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
        pos = datos.find(':')
        long = len(':')
        datos_finales = datos[:pos] + "::" + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")
    @freeze_time("01/07/2024")
    def test_guest_arrival_del_11(self):
        """Eliminamos el nodo 11"""
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
        caracter_buscado = ','
        pos = datos.find(caracter_buscado)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")
    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_12(self):
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
        caracter_buscado = '"d49c3ef42abd0183038e1f4ec296ed04"'
        pos = datos.find(caracter_buscado)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")
    @freeze_time("01/07/2024")
    def test_guest_arrival_del_12(self):
        """Eliminamos el nodo 12"""
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
        caracter_buscado = '"d49c3ef42abd0183038e1f4ec296ed04"'
        pos = datos.find(caracter_buscado)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")
    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_13(self):
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
        caracter_buscado = ','
        pos = datos.find(caracter_buscado)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + '.' + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")
    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_14(self):
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
        caracter_buscado = '"IdCard"'
        pos = datos.find(caracter_buscado)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")
    @freeze_time("01/07/2024")
    def test_guest_arrival_del_14(self):
        """Eliminamos el nodo 14"""
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
        caracter_buscado = '"IdCard"'
        pos = datos.find(caracter_buscado)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_15(self):
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
        caracter_buscado = ':'
        pos = datos.find(caracter_buscado)
        for i in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_15(self):
        """Eliminamos el nodo 15"""
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
        caracter_buscado = ':'
        pos = datos.find(caracter_buscado)
        for i in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")
    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_16(self):
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
        caracter_buscado = '"02564364W"'
        pos = datos.find(caracter_buscado)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_16(self):
        """Eliminamos el nodo 16"""
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
        caracter_buscado = '"02564364W"'
        pos = datos.find(caracter_buscado)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_17(self):
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
        caracter_buscado = '"'
        pos = 0
        for i in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] +caracter_buscado+caracter_buscado+ datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_17(self):
        """Eliminamos el nodo 17"""
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
        caracter_buscado = '"'
        pos = 0
        for i in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_18(self):
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
        caracter_buscado = 'Localizer'
        pos = 0
        for i in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_18(self):
        """Eliminamos el nodo 18"""
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
        caracter_buscado = 'Localizer'
        pos = 0
        for _ in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_19(self):
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
        caracter_buscado = '"'
        pos = 0
        for i in range(2):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_19(self):
        """Eliminamos el nodo 19"""
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
        caracter_buscado = '"'
        pos = 0
        for i in range(2):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_20(self):
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
        caracter_buscado = ':'
        pos = 0
        for _ in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = ';'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_21(self):
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
        caracter_buscado = '"'
        pos = 0
        for i in range(3):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_21(self):
        """Eliminamos el nodo 21"""
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
        caracter_buscado = '"'
        pos = 0
        for i in range(3):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_22(self):
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
        caracter_buscado = 'd49c3ef42abd0183038e1f4ec296ed04'
        pos = 0
        for i in range(3):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_22(self):
        """Eliminamos el nodo 22"""
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
        caracter_buscado = 'd49c3ef42abd0183038e1f4ec296ed04'
        pos = 0
        for i in range(3):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_23(self):
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
        caracter_buscado = '"'
        pos = 0
        for i in range(4):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_23(self):
        """Eliminamos el nodo 23"""
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
        caracter_buscado = '"'
        pos = 0
        for i in range(4):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_24(self):
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
        caracter_buscado = '"'
        pos = 0
        for i in range(5):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_24(self):
        """Eliminamos el nodo 24"""
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
        caracter_buscado = '"'
        pos = 0
        for i in range(5):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_25(self):
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
        caracter_buscado = 'IdCard'
        pos = 0
        for i in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_25(self):
        """Eliminamos el nodo 25"""
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
        caracter_buscado = 'IdCard'
        pos = 0
        for i in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_26(self):
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
        caracter_buscado = '"'
        pos = 0
        for i in range(6):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_26(self):
        """Eliminamos el nodo 26"""
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
        caracter_buscado = '"'
        pos = 0
        for i in range(6):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_27(self):
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
        caracter_buscado = ':'
        pos = 0
        for i in range(2):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = ';'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_28(self):
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
        caracter_buscado = '"'
        pos = 0
        for i in range(7):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_28(self):
        """Eliminamos el nodo 28"""
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
        caracter_buscado = '"'
        pos = 0
        for i in range(7):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_29(self):
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
        caracter_buscado = '02564364W'
        pos = 0
        for i in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_29(self):
        """Eliminamos el nodo 29"""
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
        caracter_buscado = '02564364W'
        pos = 0
        for i in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_dup_30(self):
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
        caracter_buscado = '"'
        pos = 0
        for _ in range(8):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_del_30(self):
        """Eliminamos el nodo 30"""
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
        caracter_buscado = '"'
        pos = 0
        for _ in range(8):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_31(self):
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
        caracter_buscado = '"'
        pos = 0
        for _ in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = '_'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_32(self):
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
        caracter_buscado = 'Localizer'
        pos = 0
        for _ in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = 'LLasid'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_33(self):
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
        caracter_buscado = '"'
        pos = 0
        for _ in range(2):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = '¨'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_34(self):
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
        caracter_buscado = '"'
        pos = 0
        for i in range(3):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = '¿'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_35(self):
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
        caracter_buscado = 'd49c3ef42abd0183038e1f4ec296ed04'
        pos = 0
        for _ in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = '33mollso¡'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_36(self):
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
        caracter_buscado = '"'
        pos = 0
        for _ in range(4):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = '-'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_37(self):
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
        caracter_buscado = '"'
        pos = 0
        for _ in range(5):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = '*'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_38(self):
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
        caracter_buscado = 'IdCard'
        pos = 0
        for _ in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = 'DNI98'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_39(self):
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
        caracter_buscado = '"'
        pos = 0
        for i in range(6):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = '^'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_40(self):
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
        caracter_buscado = '"'
        pos = 0
        for i in range(7):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = '='
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_41(self):
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
        caracter_buscado = '02564364W'
        pos = 0
        for i in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = '0256dda+'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def test_guest_arrival_mod_42(self):
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
        caracter_buscado = '"'
        pos = 0
        for i in range(8):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        caracter_modificado = '>'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")
