"""Hola"""

class HotelManagementException(Exception):
    """Hola"""
    def __init__(self, message):
        """Hola"""
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """Hola"""
        return self.__message

    @message.Setter
    def Message(self,value):
        """Hola"""
        self.__message = value
