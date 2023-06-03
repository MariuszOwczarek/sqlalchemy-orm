from sqlalchemy.orm import relationship

from session import session
from models import Article, Author

def main():
    login = input(f'Provide author login: ')
    author = session.query(Author).filter(Author.login == login).first()
    if author is None:
        print(f'Author {login} not found')
        return


    print(f'The list of articles of ID#: {author.id}, {author}:')
    for article in author.articles:
        print(f'- {article}')

if __name__ == "__main__":
    main()