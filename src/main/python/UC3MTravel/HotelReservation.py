"""Created by Luca, Marcos and Alicia in mar 2024
"""
import hashlib
from datetime import datetime

#je
class HotelReservation():
    """Clase Hotel Reservation"""
    def __init__(self, idcard, creditcard, date_arrival, name_and_surname, phonenumber, room_type, numdays):
        self.__idcard = idcard
        self.__creditcard = creditcard
        Justnow = datetime.utcnow()
        self.__arrival = date_arrival
        self.__name_surname = name_and_surname
        self.__phonenumber = phonenumber
        self.__reservation_date = datetime.timestamp(Justnow)
        self.__roomtype = room_type
        self.__num_days = numdays
        self.__localizer = hashlib.md5(self.__str__().encode()).hexdigest()

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        JsonInfo = {"id_card": self.__idcard,
                     "credit_card": self.__creditcard,
                     "arrival_date": self.__arrival,
                     "name_surname": self.__name_surname,
                     "phone_number:": self.__phonenumber,
                     "reservation_date": self.__reservation_date,
                     "room_type": self.__roomtype,
                     "num_days": self.__num_days,
                     }
        return "HotelReservation:" + JsonInfo.__str__()

    @property
    def creditcard(self):
        return self.__creditcardnumber
    @creditcard.setter
    def creditcard(self, value):
        self.__creditcardnumber = value

    @property
    def idcard(self):
        return self.__idcard
    @idcard.setter
    def idcard(self, value):
        self.__idcard = value


    @property
    def localizer( self ):
        """Returns the md5 signature"""
        return self.__localizer
