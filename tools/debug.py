#!/usr/bin/env python3
import ipdb;
from lib.Author import Author
from lib.Magazine import Magazine
from lib.Article import Article


if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    testAuthor = Author("Author One")
    secondAuthor = Author("Author Two")
    print("Author's name", testAuthor.name())
    testMagazine = Magazine("Tutembee", "Travel")
    testMagazine2 = Magazine("Tupike", "Cooking")
    print("MAgazine Details", testMagazine.name, testMagazine.category)
    print("All magazines", testMagazine.all())
    testArticle = Article(testAuthor, testMagazine, "A Visit to Lamu")
    secondArticle = Article(testAuthor, testMagazine2, "Tupike Chakula Kitamu")
    thirdArticle = Article(testAuthor, testMagazine2, "Tupike Chakula Kibaya")
    print("Article Title", testArticle.title())
    print("All Articles", testArticle.all())
    print("Article Author", testArticle.author())
    print("Articles for our Author", testAuthor.articles())
    print("Magazines for our Author", testAuthor.magazines())
    print("All Authors in Our Magazine", testMagazine2.contributors())












# DO NOT REMOVE THIS
    # ipdb.set_trace()
