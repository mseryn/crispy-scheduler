import datetime


def meeting():
    def __init__(self, name = "default meeting name", time = Null, room = Null, participants = []):
        _name = name
        _time = time
        _room = room
        _participants = participants

    def get_time(self):
        return _time

    def get_name(self):
        return _name

    def get_room(self):
        return _room

    def get_participants(self):
        return _participants

    def set_time(name):
        self._name = name

    def set_time(time):
        if time is instanceof(datetime.datetime):
            self._time = time
        else:
            print("time must be a datetime.datetime object")

    def set_room(room):
        self._room = room

    def overwrite_participants(participants):
        self._participants = participants

    def clear_participants():
        self._participants = []

    def add_participants(participants):
        for participant in participants:
            self._participants.append(participant)
