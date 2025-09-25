import pytest
from sqlalchemy import text


class TestUsersCRUD:
    def test_database_connection(self, db_session):
        result = db_session.execute(text("SELECT 1"))
        assert result.scalar() == 1

    def test_add_user(self, db_session, cleanup_test_data):
        test_user_id = 100000
        test_email = "test.user@example.com"
        test_subject_id = 1
        cleanup_test_data.append(test_user_id)
        insert_query = text(
            """
            INSERT INTO users (user_id, user_email, subject_id)
            VALUES (:user_id, :user_email, :subject_id)
        """
        )
        db_session.execute(
            insert_query,
            {
                "user_id": test_user_id,
                "user_email": test_email,
                "subject_id": test_subject_id,
            },
        )
        db_session.commit()
        result = db_session.execute(
            text("SELECT * FROM users WHERE user_id = :user_id"),
            {"user_id": test_user_id},
        )
        user = result.fetchone()

        assert user is not None
        assert user.user_id == test_user_id
        assert user.user_email == test_email
        assert user.subject_id == test_subject_id

    def test_update_user(self, db_session, cleanup_test_data):
        test_user_id = 100001
        original_email = "original@example.com"
        updated_email = "updated@example.com"
        test_subject_id = 2
        cleanup_test_data.append(test_user_id)
        db_session.execute(
            text(
                "INSERT INTO users (user_id, user_email, subject_id) "
                "VALUES (:id, :email, :subject)"
            ),
            {
                "id": test_user_id,
                "email": original_email,
                "subject": test_subject_id,
            },
        )
        db_session.commit()
        result_before = db_session.execute(
            text("SELECT user_email FROM users WHERE user_id = :id"),
            {"id": test_user_id},
        )
        assert result_before.scalar() == original_email
        db_session.execute(
            text("UPDATE users SET user_email = :new_email "
                 "WHERE user_id = :id"),
            {"id": test_user_id, "new_email": updated_email},
        )
        db_session.commit()
        result_after = db_session.execute(
            text("SELECT user_email FROM users WHERE user_id = :id"),
            {"id": test_user_id},
        )
        email = result_after.scalar()

        assert email == updated_email

    def test_delete_user(self, db_session):
        test_user_id = 100002
        test_email = "delete@example.com"
        test_subject_id = 3
        db_session.execute(
            text(
                "INSERT INTO users (user_id, user_email, subject_id) "
                "VALUES (:id, :email, :subject)"
            ),
            {
                "id": test_user_id,
                "email": test_email,
                "subject": test_subject_id,
            },
        )
        db_session.commit()
        result_before = db_session.execute(
            text("SELECT COUNT(*) FROM users WHERE user_id = :id"),
            {"id": test_user_id},
        )
        assert result_before.scalar() == 1
        db_session.execute(
            text("DELETE FROM users WHERE user_id = :id"),
            {"id": test_user_id},
        )
        db_session.commit()
        result_after = db_session.execute(
            text("SELECT COUNT(*) FROM users WHERE user_id = :id"),
            {"id": test_user_id},
        )
        assert result_after.scalar() == 0


def test_table_exists(db_session):
    try:
        result = db_session.execute(text("SELECT COUNT(*) FROM users"))
        count = result.scalar()
        assert count >= 0, "Таблица users не существует или недоступна"
        print(f"\n  ✅ Таблица users существует, записей: {count}")
    except Exception as e:
        pytest.fail(f"Таблица users недоступна: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
