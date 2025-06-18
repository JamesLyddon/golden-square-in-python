import pytest
from unittest.mock import Mock
from lib.secret_diary import SecretDiary

@pytest.fixture
def secret_diary():
    diary = Mock()
    diary.contents = 'lorem ipsum'
    diary.read.return_value = 'lorem ipsum'
    return SecretDiary(diary)

def test_initialisation(secret_diary):
    assert isinstance(secret_diary, SecretDiary)

def test_read_locked_diary(secret_diary):
    with pytest.raises(Exception) as e:
        secret_diary.read() == 'Go away!'
    err_msg = str(e.value)
    assert err_msg == 'Go away!'

def test_read_unlocked_diary(secret_diary):
    secret_diary.unlock()
    assert secret_diary.read() == 'lorem ipsum'

def test_read_unlocked_then_relocked(secret_diary):
    secret_diary.unlock()
    assert secret_diary.read() == 'lorem ipsum'
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read() == 'Go away!'
    err_msg = str(e.value)
    assert err_msg == 'Go away!'