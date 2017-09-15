#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

# 获取 collection
def getColl():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.popular
    trending = db.trending
    return trending


class Trending(object):

    def __init__(self, author, title, description, language, star, network, todayStar):
        self.author = author
        self.title = title
        self.description = description
        self.language = language
        self.star = star
        self.network =network
        self.todayStar =todayStar

    def save(self):
        trending = {"author": self.author, "title": self.title, "description": self.description, "language": self.language, "star": self.star, "network": self.network, "todayStar": self.todayStar}
        coll = getColl()
        id = coll.insert(trending)
        print (id)

    @staticmethod
    def query():
        trendings = getColl().find()
        return trendings
