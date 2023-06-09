from session import session
from models import Author


def main():
    number = 182
    user = session.query(Author).get(number)
    if user is None:
        print("User not found")
        return

    session.delete(user)
    session.commit()


    user = session.query(Author).get(number)
    if user is None:
        print(f"user with id {number} deleted")
    else:
        print(f"user with id {user.id} not deleted")


if __name__ == "__main__":
    main()
