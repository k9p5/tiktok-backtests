import math, decimal, enum
from datetime import datetime

dec = decimal.Decimal

class MoonPhases(enum.Enum):
    NEW_MOON = "New Moon"
    WAXING_CRESCENT = "Waxing Crescent"
    FIRST_QUARTER = "First Quarter"
    WAXING_GIBBOUS = "Waxing Gibbous"
    FULL_MOON = "Full Moon"
    WANING_GIBBOUS = "Waning Gibbous"
    LAST_QUARTER = "Last Quarter"
    WANING_CRESCENT = "Waning Crescent"



def get_moon_phase(date: datetime) -> MoonPhases:
    """
    moonphase.py - Calculate Lunar Phase
    Author: Sean B. Palmer, inamidst.com
    Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation
    """
    diff = date - datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))
    index = math.floor((lunations % dec(1) * dec(8)) + dec("0.5"))
    return [
        MoonPhases.NEW_MOON, 
        MoonPhases.WAXING_CRESCENT, 
        MoonPhases.FIRST_QUARTER, 
        MoonPhases.WANING_GIBBOUS, 
        MoonPhases.FULL_MOON, 
        MoonPhases.WANING_GIBBOUS, 
        MoonPhases.LAST_QUARTER, 
        MoonPhases.WANING_CRESCENT
    ][int(index) & 7]