from sqlalchemy import func

from session import session
from models import Author, Article


def main():
    query = session.query(
        Author.first_name.label("first_name"),
        Author.last_name.label("last_name"),
        func.count("*").label("total")
    ).join(
        Article
    ).group_by(
        Author.id
    )

    for record in query:
        print(
            record.first_name,
            record.last_name,
            record.total
        )


if __name__ == "__main__":
    main()
