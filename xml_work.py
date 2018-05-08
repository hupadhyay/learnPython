import xml.dom.minidom
from xml.dom.minidom import parse

domTree = parse('simple/movie.xml');

colln = domTree.documentElement;

if colln.hasAttribute('shelf'):
    print(f'Root Element : {colln.getAttribute("shelf")}');
    
# Get All movies elements from collections.

movies = colln.getElementsByTagName('movie');

for movie in movies:
    if movie.hasAttribute('title'):
        print(f'Title : {movie.getAttribute("title")}')
        
    
    typeTag = movie.getElementsByTagName('type')[0]
    print(f'Type: {typeTag.childNodes[0].data}')
    
    formatTag = movie.getElementsByTagName('format')[0]
    print(f'Format: {formatTag.childNodes[0].data}')
    
    RatingTag = movie.getElementsByTagName('rating')[0]
    print(f'Rating: {RatingTag.childNodes[0].data}')
    
    StarsTag = movie.getElementsByTagName('stars')[0]
    print(f'Star: {StarsTag.childNodes[0].data}')
    
    DescTag = movie.getElementsByTagName('description')[0]
    print(f'Star: {DescTag.childNodes[0].data}')