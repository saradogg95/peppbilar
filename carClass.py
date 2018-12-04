"""
id: int
type: string
category: string
manufacturer: string
registration_date: date
plate_number: string
mileage: int
is_available: bool
"""

class Car:
    def __init__(self, id=0, type="", category="", manufacturer="", registration_date="", plate_number="", mileage=0, is_available=True):
        