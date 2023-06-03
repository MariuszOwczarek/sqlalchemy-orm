from session import session, commit_on_success
from models import Article, Author

@commit_on_success
def main():
    answer = input(f' Do you want to add article? [Y/N]: ')

    if answer.lower() == 'y':
        run = True
    else:
        run = False

    while run:
        login = input('Provide author login: ')
        author = session.query(Author).filter_by(login=login).first()
        if author is None:
            print("Author not found")
            continue

        title = input('Provide article title: ')
        content = input('Provide article content: ')

        article = Article(title=title, content=content)
        author.articles.append(article)

        print(f'Article {title} added')

        answer = f' Do you want to add article? [Y/N]: '

        if answer.lower() != 'y':
            run = False

if __name__ == "__main__":
    main()
