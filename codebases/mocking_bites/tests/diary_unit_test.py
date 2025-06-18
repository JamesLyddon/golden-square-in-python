import pytest
from lib.diary import Diary

@pytest.fixture
def diary():
    return Diary('lorem ipsum')

def test_initialisation(diary):
    assert isinstance(diary, Diary)

def test_read_contents(diary):
    assert diary.read() == 'lorem ipsum'