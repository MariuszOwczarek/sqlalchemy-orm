from models import Author
from session import session


def main():

    # odczytywanie
    query = session.query(Author).all()
    for _ in query:
        print(f'{_.first_name}, {_.last_name}, {_.user_name}, {_.salary}, {_.email}')


if __name__ == "__main__":
    main()
