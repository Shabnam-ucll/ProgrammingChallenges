
books = {
    "1984": ["George Orwell", "Fiction", 5],
    "Sapiens": ["Yuval Noah Harari", "Non-Fiction", 10],
    "To Kill a Mockingbird": ["Harper Lee", "Fiction", 8],
    "A Brief History of Time": ["Stephen Hawking", "Science", 7],
    "The Catcher in the Rye": ["J.D. Salinger", "Fiction", 6],
    "Becoming": ["Michelle Obama", "Biography", 12],
    "The Great Gatsby": ["F. Scott Fitzgerald", "Fiction", 4],
    "Homo Deus": ["Yuval Noah Harari", "Non-Fiction", 9],
    "The Subtle Art of Not Giving a F*ck": ["Mark Manson", "Self-Help", 15],
    "Educated": ["Tara Westover", "Biography", 10]
}

def add_book(books, title, author, genre, stock):
    if title not in books:
        books[title] = [author,genre,stock]
    else:
        books[title][2] += stock

def books_by_author(books, author):
    result = set()
    for title, details in books.items():
        if details[0] == author:
            result.add(title)
    return result

def check_availability(books, title):
    return title in books and books[title][2]>0


customers = {
    "Alice": {"Fiction", "Non-Fiction"},
    "Bob": {"Fiction", "Science"},
    "Charlie": {"Biography", "Non-Fiction"},
    "Diana": {"Self-Help", "Fiction"},
    "Eve": {"Non-Fiction", "Science", "Biography"},
    "Frank": {"Fiction", "Biography"},
    "Grace": {"Self-Help", "Non-Fiction"}
}

def add_genre(customers, name, genre):
    if name not in customers:
        customers[name] = set()
    customers[name].add(genre)

def all_genres(customers):
    result = set()
    for genres in customers.values():
        result.update(genres)
    return result

def recommend_books(books, customers, name):
    result = set()
    genres = customers[name]
    for title, details in books.items():
        if details[1] in genres:
            result.add(title)
    return result
