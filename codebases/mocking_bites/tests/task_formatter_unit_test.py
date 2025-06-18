import pytest
from unittest.mock import Mock
from lib.task_formatter import TaskFormatter

@pytest.fixture
def tf():
    task = Mock()
    task.title = 'walk the dog'
    task.complete = False
    tf = TaskFormatter(task)
    return tf

def test_initialisation(tf):
    assert isinstance(tf, TaskFormatter)

def test_tf_has_task(tf):
    assert tf.task.title == 'walk the dog'
    assert tf.task.complete == False

def test_format(tf):
    assert tf.format() == '[ ] walk the dog'
    tf.task.complete = True
    assert tf.format() == '[x] walk the dog'