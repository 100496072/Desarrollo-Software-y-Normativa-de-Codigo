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
    def testGuestArrivalDup6(self):
        """Duplicamos el nodo 6"""
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
    def testGuestArrivalDel6(self):
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
    def testGuestArrivalDup7(self):
        """Duplicamos el nodo 7"""
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
    def testGuestArrivalDel7(self):
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
    def testGuestArrivalDup8(self):
        """Duplicamos el nodo 8"""
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
    def testGuestArrivalDel8(self):
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
    def testGuestArrivalMod9(self):
        """Modificamos el nodo 9"""
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
    def testGuestArrivalDup10(self):
        """Duplicamos el nodo 10"""
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
    def testGuestArrivalDel10(self):
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
    def testGuestArrivalDup11(self):
        """Duplicamos el nodo 11"""
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
    def testGuestArrivalDel11(self):
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
    def testGuestArrivalDup12(self):
        """Duplicamos el nodo 12"""
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
    def testGuestArrivalDel12(self):
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
    def testGuestArrivalMod13(self):
        """Modificamos el nodo 13"""
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
    def testGuestArrivalDup14(self):
        """Duplicamos el nodo 14"""
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
    def testGuestArrivalDel14(self):
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
    def testGuestArrivalDup15(self):
        """Duplicamos el nodo 15"""
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
        for _ in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel15(self):
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
        for _ in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")
    @freeze_time("01/07/2024")
    def testGuestArrivalDup16(self):
        """Duplicamos el nodo 16"""
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
    def testGuestArrivalDel16(self):
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
    def testGuestArrivalDup17(self):
        """Duplicamos el nodo 17"""
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
        datos_finales = datos[:pos] +caracter_buscado+caracter_buscado+ datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel17(self):
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
        for _ in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDup18(self):
        """Duplicamos el nodo 18"""
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
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel18(self):
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
    def testGuestArrivalDup19(self):
        """Duplicamos el nodo 19"""
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
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel19(self):
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
        for _ in range(2):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalMod20(self):
        """Modificamos el nodo 20"""
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
    def testGuestArrivalDup21(self):
        """Duplicamos el nodo 21"""
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
        for _ in range(3):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel21(self):
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
        for _ in range(3):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDup22(self):
        """Duplicamos el nodo 22"""
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
        for _ in range(3):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel22(self):
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
        for _ in range(3):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def testGuestArrivalDup23(self):
        """Duplicamos el nodo 23"""
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
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel23(self):
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
        for _ in range(4):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDup24(self):
        """Duplicamos el nodo 24"""
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
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel24(self):
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
        for _ in range(5):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDup25(self):
        """Duplicamos el nodo 25"""
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
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel25(self):
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
    def testGuestArrivalDup26(self):
        """Duplicamos el nodo 26"""
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
        for _ in range(6):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel26(self):
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
        for _ in range(6):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalMod27(self):
        """Modificamos el nodo 27"""
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
        for _ in range(2):
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
    def testGuestArrivalDup28(self):
        """Duplicamos el nodo 28"""
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
        for _ in range(7):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel28(self):
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
        for _ in range(7):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")

    @freeze_time("01/07/2024")
    def testGuestArrivalDup29(self):
        """Duplicamos el nodo 29"""
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
        for _ in range(1):
            pos = datos.find(caracter_buscado, pos + 1)
        long = len(caracter_buscado)
        datos_finales = datos[:pos] + caracter_buscado + caracter_buscado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "El JSON no tiene la estructura esperada")

    @freeze_time("01/07/2024")
    def testGuestArrivalDel29(self):
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
    def testGuestArrivalDup30(self):
        """Duplicamos el nodo 30"""
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
    def testGuestArrivalDel30(self):
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
    def testGuestArrivalMod31(self):
        """Modificamos el nodo 31"""
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
    def testGuestArrivalMod32(self):
        """Modificamos el nodo 32"""
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
    def testGuestArrivalMod33(self):
        """Modificamos el nodo 33"""
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
    def testGuestArrivalMod34(self):
        """Modificamos el nodo 34"""
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
        for _ in range(3):
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
    def testGuestArrivalMod35(self):
        """Modificamos el nodo 35"""
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
    def testGuestArrivalMod36(self):
        """Modificamos el nodo 36"""
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
    def testGuestArrivalMod37(self):
        """Modificamos el nodo 37"""
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
    def testGuestArrivalMod38(self):
        """Modificamos el nodo 38"""
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
    def testGuestArrivalMod39(self):
        """Modificamos el nodo 39"""
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
        for _ in range(6):
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
    def testGuestArrivalMod40(self):
        """Modificamos el nodo 40"""
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
        for _ in range(7):
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
    def testGuestArrivalMod41(self):
        """Modificamos el nodo 41"""
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
        for _ in range(1):
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
    def testGuestArrivalMod42(self):
        """Modificamos el nodo 42"""
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
        caracter_modificado = '>'
        datos_finales = datos[:pos] + caracter_modificado + datos[pos + long:]
        with open(file_store, "w", encoding="utf-8", newline="") as archivo:
            archivo.write(datos_finales)
        with self.assertRaises(HotelManagementException) as error:
            my_hotelroom.guestArrival(input_file=file_store)

        self.assertEqual(error.exception.message, "JSON Decode Error - Wrong JSON Format")
