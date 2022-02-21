import csv

all_articles = []
liked_articles = [] 
not_liked_articles = []
did_not_read = []

with open("articles.csv","r",encoding="utf8") as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    all_movies = data[1:]
