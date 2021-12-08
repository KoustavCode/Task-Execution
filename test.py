import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from code import TaskExecution

ob = TaskExecution()


def test_numbers_1():
    assert (
        ob.first_execute(['CALL', 'U2', 'India', '13:00:00', '18:30:00', 0], '18:30:00')
        == 'True'
    )


def test_numbers_2():
    assert (
        ob.first_execute(['CALL', 'U2', 'India', '13:00:00', '18:30:00', 0], '19:30:00')
        == 'False'
    )


def test_numbers_3():
    assert (
        ob.second_execute(
            ['CALL', 'U2', 'India', '13:00:00', '18:30:00', 'Tuesday and Thursday'],
            'Friday 18:30:00',
        )
        == 'Tuesday 13:00:00'
    )
