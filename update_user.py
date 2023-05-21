from session import session
from models import User


def main():
    user = session.query(User).get(42)
    if user is None:
        print(f"User with id {user.id} not found")
        return

    print(f'Found {user.id}')
    print(f'Previous Salary: {user.salary}')

    user.salary *= 1.15

    session.add(user)
    session.commit()

    user = session.query(User).get(42)
    print(f'Current Salary: {user.salary}')

if __name__ == "__main__":
    main()
