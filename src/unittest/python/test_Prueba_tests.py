
"""UNITTEST"""
from unittest import TestCase
from UC3MTravel import HotelManager
from UC3MTravel import HotelManagementException
class TestHotelManager(TestCase):
    """Comentario"""
    def setUp(self):
        pass

    def test_valid_credit_card1(self):
        # Una tarjeta válida
        valid_card1 = "5555555555554444"
        self.assertIsNone(HotelManager.validateCreditCard(self, valid_card1))
        print("Test 1 OK")

    def test_valid_credit_card2(self):
        # Una tarjeta válida
        valid_card2 = "4008641178791526"
        self.assertIsNone(HotelManager.validateCreditCard(self, valid_card2))
        print("Test 2 OK")

    def test_valid_credit_card3(self):
        # Una tarjeta no válida
        valid_card3 = "4003209683263426"
        self.assertIsNone(HotelManager.validateCreditCard(self, valid_card3))
        print("Test 3 OK")


    def test_valid_credit_card4(self):
        # Una tarjeta no válida
        valid_card4 = "400320968326342A"
        with self.assertRaises(HotelManagementException) as error:
            HotelManager.validateCreditCard(self, valid_card4)

        self.assertEqual(error.exception.message, "El número de tarjeta recibido no es válido o no tiene"
                                                  " un formato válido.")
        print("Test 4 OK")

    def test_valid_credit_card5(self):
        # Una tarjeta no válida
        valid_card5 = "AAAAAAAAAAAAAAAA"
        with self.assertRaises(HotelManagementException) as error:
            HotelManager.validateCreditCard(self, valid_card5)

        self.assertEqual(error.exception.message, "El número de tarjeta recibido no es válido o no tiene"
                                                  " un formato válido.")
        print("Test 5 OK")


    def test_valid_credit_card6(self):
        # Una tarjeta no válida
        valid_card6 = "4916333877943663"
        with self.assertRaises(HotelManagementException) as error:
            HotelManager.validateCreditCard(self, valid_card6)

        self.assertEqual(error.exception.message, "El número de tarjeta recibido no es válido o no tiene"
                                                  " un formato válido.")
        print("Test 6 OK")

