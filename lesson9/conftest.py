import pytest
from sqlalchemy import text
from database import SessionLocal


@pytest.fixture
def db_session():
    session = SessionLocal()
    try:
        session.execute(text("SELECT 1"))
        yield session
    except Exception as e:
        pytest.skip(f"Нет подключения к базе данных: {e}")
    finally:
        session.close()


@pytest.fixture
def cleanup_test_data(db_session):
    test_user_ids = []
    yield test_user_ids
    if test_user_ids:
        try:
            for user_id in test_user_ids:
                db_session.execute(
                    text("DELETE FROM users WHERE user_id = :user_id"),
                    {"user_id": user_id}
                )
            db_session.commit()
        except Exception as e:
            print(f"Ошибка при очистке тестовых данных: {e}")
            db_session.rollback()
