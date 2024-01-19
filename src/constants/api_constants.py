# Add constants

#option 1
Base_URL = "https://restful-booker.herokuapp.com"
# option 2 with function
def base_url():
    return "https://restful-booker.herokuapp.com"

#option 3 in a class
class APIConstants(object):
    # object is always present even if you donot type

    @staticmethod
    def base_url(): # self is not required with static method
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"


    def url_patch_put_delete_booking(self,booking_id): # bookingID is string
        return "https://restful-booker.herokuapp.com/booking/" + str(self.booking_id)