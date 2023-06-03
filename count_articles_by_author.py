from sqlalchemy import func

from session import session
from models import Article

def main():
    result = session.query(Article.author_id, func.count()).group_by(Article.author_id)

    for author_id, total in result:
        print(f"Author ID: {author_id}, Total: {total}")

if __name__ == "__main__":
    main()
