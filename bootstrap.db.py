from sqlalchemy.exc import IntegrityError

from models import Base, User
from session import session
from faker import Faker


def create_users(count=100):
    fake = Faker()
    return [
        User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            user_name=fake.user_name(),
            salary=fake.pyfloat(
                min_value=4000,
                max_value=10_000
            ),
            email=fake.email(),
        )
        for _ in range(count)
    ]


def main():
    # create all tables
    Base.metadata.create_all()

    # zapis danych poprzez sesje
    users = create_users(500)
    for user in users:
        try:
            session.add(user)
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f'Users: {user.user_name} already exists')


if __name__ == "__main__":
    main()
