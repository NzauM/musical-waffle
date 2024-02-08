from .Article import Article
class Author:
    def __init__(self, name) :
        self._name = name
        
    def __repr__(self) -> str:
        return(f" {self._name}" )
        pass
    def name(self):
        return self._name
    
    def articles(self):
        # return a list of all articles, written by this author
        # get a list of all articles, and filter by author
        allArticles = Article.all_articles
        # authorArticles = []
        # for article in allArticles:
        #     if article.author() == self:
        #         authorArticles.append(article)
        # return authorArticles
        return [article for article in allArticles if article.author() == self]


    def magazines(self):
        # get a list of all magazines where the author has articles
        # access all articles by this author
        authorArticles = self.articles()
        # find out which magazines the articles belong to
        authorMagazines = []
        for article in authorArticles:
            authorMagazines.append(article.magazine()) if article.magazine() not in authorMagazines else ""
        return authorMagazines