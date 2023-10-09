def rec_book(members,books):
  recommendation=[]
  genre_to_book = {}
  for book in books:
    genre = book['genre']
    if genre not in genre_to_book:
      genre_to_book[genre] = []
    genre_to_book[genre].append(book)

    for member in members:
      name = member['name']
      preferred_genre = member['genre']
      if preferred_genre in genre_to_book:
        for book in genre_to_book[preferred_genre]:
          if book['name'] not in recommendation:
            recomended_book = genre_to_book[0]['title']
        else:
          recomended_book = None
    
    recommendation = {'member': name,'book':recomended_book}
    recommendation.append(recomended_book)
    
    return recommendation