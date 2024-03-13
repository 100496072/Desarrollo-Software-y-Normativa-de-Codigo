
"""UNITTEST"""
from unittest import TestCase
from UC3MTravel import HotelManager
class TestHotelManager(TestCase):
    """Comentario"""
    def setUp(self):
        pass

    def test_valid_credit_card1(self):
        # Una tarjeta válida
        valid_card1 = "5555555555554444"
        self.assertTrue(HotelManager.validateCreditCard(self, valid_card1))
        print("Test 1 OK")

    def test_valid_credit_card2(self):
        # Una tarjeta válida
        valid_card2 = "4008641178791526"
        self.assertTrue(HotelManager.validateCreditCard(self, valid_card2))
        print("Test 2 OK")

    def test_valid_credit_card3(self):
        # Una tarjeta no válida
        valid_card3 = "4003209683263426"
        self.assertTrue(HotelManager.validateCreditCard(self, valid_card3))
        print("Test 3 OK")


    def test_valid_credit_card4(self):
        # Una tarjeta no válida
        valid_card4 = "4916333877943683"
        self.assertFalse(HotelManager.validateCreditCard(self, valid_card4))
        print("Test 4 OK")

    def test_valid_credit_card5(self):
        # Una tarjeta no válida
        valid_card5 = "5555555555554443"
        self.assertFalse(HotelManager.validateCreditCard(self, valid_card5))
        print("Test 5 OK")


    def test_valid_credit_card6(self):
        # Una tarjeta no válida
        valid_card6 = "4916333877943663"
        self.assertFalse(HotelManager.validateCreditCard(self, valid_card6))
        print("Test 6 OK")

