from context import schedule


# Testing resource management

def test_default_resources():
    test_posting = schedule.posting()
    assert_true((test_posting.get_resources == []), \
        "default resources in posting not correct")

def test_initialized_resources():
    test_person = schedule.resource.person()
    test_posting = schedule.posting(resources = [test_person])
    assert_true((test_posting.get_resources = [test_person]), \
        "initialized resources in posting not correct")

def test_overwrite_resources():
    test_person = schedule.resource.person()
    test_posting = schedule.posting()
    test_posting.overwrite_resources([test_person])
    assert_true((test_posting.get_resources = [test_person]), \
        "overwrite resources in posting not correct")

def test_clear_resources():
    test_person = schedule.resource.person()
    test_posting = schedule.posting(resources = [test_person])
    test_posting.clear()
    assert_true((test_posting.get_resources = []), \
        "clear resources in posting not correct")

def test_add_resources():
    test_person = schedule.resource.person()
    test_posting = schedule.posting()
    test_posting.add_resources([test_person])
    assert_true((test_posting.get_resources = [test_person]), \
        "add resources in posting not correct")
    
# Testing task management

def test_default_tasks():
    test_posting = schedule.posting()
    assert_true((test_posting.get_tasks == []), \
        "default tasks in posting not correct")

def test_initialized_resources():
    test_meeting = schedule.task.meeting()
    test_posting = schedule.posting(tasks = [test_meeting])
    assert_true((test_posting.get_tasks() == [test_meeting]), \
        "initialized tasks in posting not correct")

def test_overwrite_tasks():
    test_meeting = schedule.task.meeting()
    test_posting = schedule.posting(tasks = [])
    test_posting.overwrite_tasks([test_meeting])
    assert_true((test_posting.get_tasks() == [test_meeting]), \
        "overwrite tasks in posting not correct")
    
def test_clear_tasks(): 
    test_meeting = schedule.task.meeting()
    test_posting = schedule.posting(tasks = [test_meeting])
    test_posting.clear_tasks()
    assert_true((test_posting.get_tasks() == []), \
        "clear tasks in posting not correct")

def test_add_tasks():
    test_meeting = schedule.task.meeting()
    test_posting = schedule.posting(tasks = [])
    test_posting.add_tasks([test_meeting])
    assert_true((test_posting.get_tasks() == [test_meeting]), \
        "add tasks in posting not correct")
