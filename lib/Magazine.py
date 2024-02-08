from .Article import Article
class Magazine:
    all_magazines = []
    def __init__(self, name, category) :
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)
        pass

    def __repr__(self) -> str:
        return (f"{self.name}" )
        pass

    def all(self):
        return Magazine.all_magazines
    
    def contributors(self):
        allArticles = Article.all_articles
        # get all articles for this magazine
        margArticles = [article for article in allArticles if article.magazine() == self]
        # find authors for these articles
        magAuthors = [article.author() for article in margArticles]
        return magAuthors

    pass