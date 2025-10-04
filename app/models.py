
from datetime import datetime
from app import db

# Tabela łącząca wiele książek z wieloma autorami
book_authors = db.Table(
    'book_authors',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    books = db.relationship('Book', secondary=book_authors, back_populates='authors')

    def __repr__(self):
        return f"<Author {self.name}>"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer)
    genre = db.Column(db.String(100))
    pages = db.Column(db.Integer)
    description = db.Column(db.Text)
    is_available = db.Column(db.Boolean, default=True)

    authors = db.relationship('Author', secondary=book_authors, back_populates='books')
    loans = db.relationship('Loan', backref='book', lazy=True)

    def __repr__(self):
        return f"<Book {self.title}>"

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrower = db.Column(db.String(100), nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime, nullable=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __repr__(self):
        return f"<Loan {self.borrower} - {self.book.title}>"