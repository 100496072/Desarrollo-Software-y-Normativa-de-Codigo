"""Created by Luca, Marcos and Alicia in mar 2024
"""

class HotelManagementException(Exception):
    """Clase HotelManagementException"""
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        return self.__message


    @message.setter
    def message(self,value):
        self.__message = value
