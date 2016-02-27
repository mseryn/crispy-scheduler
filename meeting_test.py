import schedule
import datetime


# Testing _name manipulation

def test_default_name():
    test_meeting = schedule.tasks.meeting()
    assert_true((test_meeting.get_name() == "default meeting name"), \
        "default name for meeting not correctly set")

def test_initialized_name():
    test_meeting = schedule.tasks.meeting(name = "Initialized With Name")
    assert_true((test_meeting.get_name() == "Initialized With Name"), \
        "initialized name for meeting not correctly set")

def test_set_name():
    test_meeting = schedule.tasks.meeting()
    test_meeting.set_name("Custom Meeting Name")
    assert_true((test_meeting.get_name() == "Custom Meeting Name"), \
        "custom name for meeting not correctly set")


# Testing _time manipulation:

def test_default_time():
    test_meeting = schedule.tasks.meeting()
    assert_true((test_meeting.get_time() == Null), \
        "default time for meeting not correctly set to Null")

def test_initialized_time():
    test_meeting = schedule.tasks.meeting(time = datetime.datetime.now())
    assert_true(test_meeting.get_time() == datetime.datetime.now()), \
        "initialized time for meeting not correctly set")

def test_set_time():
    test_meeting = schedule.tasks.meeting()
    test_meeting.set_time(datetime.datetime.now())
    assert_true(test_meeting.get_time() == datetime.datetime.now()), \
        "set time for meeting not correctly set")


# Testing _room manipulation:

def test_default_room():
    test_meeting = schedule.tasks.meeting()
    assert_true((test_meeting.get_room() == Null), \
        "default room for meeting not correctly set")

def test_initialized_room():
    test_room = schedule.resource.room()
    test_meeting = schedule.tasks.meeting(room = test_room)
    assert_true((test_meeting.get_room() == test_room), \
        "initialized room for meeting not correctly set")

def test_set_room():
    test_room = schedule.resource.room()
    test_meeting = schedule.tasks.meeting()
    test_meeting.set_room(test_room)
    assert_true((test_meeting.get_room() == test_room), \
        "set room for meeting not correctly set")


# Testing _participants manipulation:

def test_default_participants():
    test_meeting = schedule.tasks.meeting()
    assert_true((test_meeting.get_participants() == []), \
        "default participants for meeting not correctly set")

def test_single_initialized_participants():
    test_person = schedule.resource.person()
    test_meeting = schedule.tasks.meeting(participants = [test_person])
    assert_true((test_meeting.get_participants() == [test_person]), \
        "initialized single participant for meeting not correctly set")

def test_multiple_initialized_participants():
    test_person1 = schedule.resource.person()
    test_person2 = schedule.resource.person()
    test_meeting = schedule.tasks.meeting(participants = [test_person1, test_person2])
    assert_true((test_meeting.get_participants() == [test_person1, test_person2]), \
        "initialize multiple participants for meeting not correctly set")

def test_set_participants():
    test_person1 = schedule.resource.person()
    test_person2 = schedule.resource.person()
    test_meeting = schedule.tasks.meeting()
    test_meeting.set_participants([test_person1, test_person2])
    assert_true((test_meeting.get_participants() == [test_person1, test_person2]), \
        "set participants for meeting not correctly set")

