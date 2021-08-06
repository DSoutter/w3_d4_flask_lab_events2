from models.event import Event

event_1 = Event('2021-08-06', 'Fantastic Frolic Finds Focal Face', 5, 'udderbelly', 'alliterative fun with friends', False)
event_2 = Event('2021-08-07', 'Great Game Gets Goalies Grateful', 28, 'Tynecastle', 'bunch of grateful goalies, what could be finer', False)
event_3 = Event('2021-08-09', 'Heavy Hippopotamai Hold Harry Hostage', 14, 'Edinburgh Dungeon', 'poor harry has got himself in quite a pickle this time', True)

events = [event_1, event_2, event_3]

def add_new_event(event):
    events.append(event)