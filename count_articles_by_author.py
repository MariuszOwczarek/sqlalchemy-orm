from sqlalchemy import func
from models import Article, Author
from session import session


def main():
    authors_articles_subquery = session.query(
        Article.author_id.label("author_id"),
        func.count("*").label("total")
    ).group_by(
        Article.author_id
    ).subquery()

    result = session.query(
        Author.first_name,
        Author.last_name,
        authors_articles_subquery.c.total
    ).join(
        authors_articles_subquery
    )

    for record in result:
        print(
            record.first_name,
            record.last_name,
            record.total
        )


if __name__ == "__main__":
    main()
