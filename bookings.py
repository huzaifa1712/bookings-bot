import requests
from datetime import datetime

URL = 'http://localhost:3000/bookings/'

class Booking:
    # input: ISO datetime string from JSON 
    # output: human readable date string
    @staticmethod
    def isodate_to_str(isodate_str):
        # e.g Sat 12 Mar 2022 09:22PM
        return datetime.fromisoformat(isodate_str).strftime("%a %d %b %Y %I:%M%p")

    def __init__(self, booking_json):
        self.user_name = booking_json['user']['name']
        self.space_name = booking_json['space']['name']
        self.start_time = Booking.isodate_to_str(booking_json['start_time'])
        self.end_time = Booking.isodate_to_str(booking_json['end_time'])
    
    def __str__(self):
        return f'User: {self.user_name}, Place: {self.space_name}, Start: {self.start_time}, End: {self.end_time}'

def get_bookings():
    bookings = requests.get(URL).json()
    return list(map(lambda b: str(Booking(b)), bookings))
