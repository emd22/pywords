from pymongo import *

client = MongoClient()
db = client.word_database

words = db.words

filename = input("filename: ")
file = open(filename)
filelines = file.readlines();

for line in filelines:
    for word in line.split():
        for document in db.words.find({ 'word': word }):
            print(document)