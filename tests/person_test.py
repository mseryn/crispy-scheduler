from context import schedule


# Testing name manipulation

def test_default_name():
    test_person = schedule.resource.person()
    assert_true((test_person.get_name() == "default person name"), \
        "default person name not correctly set")

def test_initialized_name():
    test_person = schedule.resource.person(name = "Initialized Name")
    assert_true((test_person.get_name() == "Initialized Name"), \
        "initialized person name not correctly set")

def test_set_name():
    test_person = schedule.resource.person()
    test_person.set_name = "Set Name"
    assert_true((test_person.get_name() == "Set Name"), \
        "set person name not correctly set")


# Testing task manipulation (using task.meeting)

def test_default_task():
    test_person = schedule.resource.person()
    assert_true((test_person.get_tasks() == Null), \
        "default person tasks not correctly set")

def test_single_initialized_task():
    test_meeting = schedule.task.meeting()
    test_person = schedule.resource.person(task = [test_meeting])
    assert_true((test_person.get_name() == [test_meeting]), \
        "single initialized task in person not correctly set")

def test_multiple_initialized_task():
    test_meeting1 = schedule.task.meeting()
    test_meeting2 = schedule.task.meeting()
    test_person = schedule.resource.person(task = [test_meeting1, test_meeting2])
    assert_true((test_person.get_name() == [test_meeting1, test_meeting2]), \
        "single initialized resource in person not correctly set")

def test_overwrite_task():
    test_meeting = schedule.task.meeting()
    test_person = schedule.resource.person()
    test_person.overwrite_tasks([test_meeting])
    assert_true((test_person.get_name() == [test_meeting]), \
        "overwrite task in person not correctly set")

def test_add_task():
    test_meeting1 = schedule.task.meeting()
    test_meeting2 = schedule.task.meeting()
    test_person = schedule.resource.person(test_meeting1)
    test_person.add_task(test_meeting2)
    assert_true((test_person.get_name() == [test_meeting1, test_meeting2]), \
        "add task in person not correctly set")

