content = []

with open('words.txt') as f:
    content = f.readlines()
    
content = [x.strip() for x in content]

db.words.insert_many([{
    '_id': i,
    'word': content[i]
} for i in range(0, len(content))]);