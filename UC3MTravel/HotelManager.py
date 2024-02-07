import json
from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation

class HotelManager:
    def __init__(self):
        pass

    def validatecreditcard( self, x:str ):
        aux = 0
        for i in range(len(x) - 1):
            k = int(x[i])
            if i % 2 == 0:
                k = k*2
                if k >= 10:
                    k = str(k)
                    j = k[0]
                    k = k[1]
                    j = int(j)
                    k = int(k)
                    k += j
            aux += k
        if (aux * 9) % 10 == int(x[15]):
            return True
        else:
            return False

    def ReaddatafromJSOn( self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z",creditcardNumb=c,nAMeAndSURNAME="John Doe",phonenumber=p,room_type="single",numdays=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req