import pytest
from lib.diary import Diary
from lib.secret_diary import SecretDiary

@pytest.fixture
def secret_diary():
    return SecretDiary(Diary('lorem ipsum'))

def test_instantiation(secret_diary):
    assert isinstance(secret_diary, SecretDiary)

def test_read_locked(secret_diary):
    with pytest.raises(Exception) as e:
        secret_diary.read()
    err_msg = str(e.value)
    assert err_msg == 'Go away!'

def test_read_locked(secret_diary):
    with pytest.raises(Exception, match='Go away!'):
        secret_diary.read()

def test_read_unlocked_then_relocked(secret_diary):
    secret_diary.unlock()
    assert secret_diary.read() == 'lorem ipsum'
    secret_diary.lock()
    with pytest.raises(Exception, match='Go away!'):
        secret_diary.read()
