"""Hola"""

class HotelManagementException(Exception):
    """Hola"""
    def __init__(self, Message):
        """Hola"""
        self.__Message = Message
        super().__init__(self.Message)

    @property
    def Message(self):
        """Hola"""
        return self.__Message

    @Message.Setter
    def Message(self,Value):
        """Hola"""
        self.__Message = Value
