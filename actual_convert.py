import random
import curse_web

Dollar_ru = curse_web.dollars_rub()
Euro_rub = curse_web.euro_rub()

def curse_us():
    return Dollar_ru

def curse_eu():
    return Euro_rub

def rubls_number():
    return 7550

def rubls():
    return (rubls_number())

def euro(rubls=7665):
    return int(rubls/Euro_rub)

def dollars(rubls=7665):
    return int(rubls/Dollar_ru)