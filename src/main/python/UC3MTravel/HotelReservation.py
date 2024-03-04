"""Comentario"""
import hashlib
from datetime import datetime

#je
class HotelReservation:
    """Comentario"""
    def __init__(self, idcard, creditcardnumb, name_and_surname, phonenumber, room_type,numdays):
        self.__creditcardnumber = creditcardnumb
        self.__idcard = idcard
        justnow = datetime.utcnow()
        self.__arrival = datetime.timestamp(justnow)
        self.__name_surname = name_and_surname
        self.__phonenumber = phonenumber
        self.__roomtype = room_type
        self.__num_days = numdays

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        json_info = {"id_card": self.__idcard,
                     "name_surname": self.__name_surname,
                     "credit_card": self.__creditcardnumber,
                     "phone_number:": self.__phonenumber,
                     "arrival_date": self.__arrival,
                     "num_days": self.__num_days,
                     "room_type": self.__roomtype,
                     }
        return "HotelReservation:" + json_info.__str__()
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
        return hashlib.md5(self.__str__().encode()).hexdigest()
