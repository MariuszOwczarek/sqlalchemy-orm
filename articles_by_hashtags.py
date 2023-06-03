from session import session
from models import Hashtags
def main():
    hashtags = session.query(Hashtags).order_by(Hashtags.name)
    for hashtag in hashtags:
        print(f'{hashtag.name}: ')
        if len(hashtag.articles) == 0:
            print('No articles')

        for article in hashtag.articles:
            print(f'\t- {article.title}')


if __name__ == "__main__":
    main()