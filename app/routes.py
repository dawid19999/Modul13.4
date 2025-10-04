
from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Book, Author, Loan
from app.forms import BookForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def index(book_id=None):
    books = Book.query.all()

    if book_id:
        book = Book.query.get_or_404(book_id)
        form = BookForm(
            title=book.title,
            authors=", ".join([a.name for a in book.authors]),
            year=book.year,
            genre=book.genre,
            pages=book.pages,
            description=book.description,
            is_available=book.is_available
        )
    else:
        form = BookForm()

    if form.validate_on_submit():
        author_names = [name.strip() for name in form.authors.data.split(",") if name.strip()]
        authors = []
        for name in author_names:
            author = Author.query.filter_by(name=name).first()
            if not author:
                author = Author(name=name)
                db.session.add(author)
            authors.append(author)

        if book_id:
            book.title = form.title.data
            book.year = form.year.data
            book.genre = form.genre.data
            book.pages = form.pages.data
            book.description = form.description.data
            book.is_available = form.is_available.data
            book.authors = authors
        else:
            new_book = Book(
                title=form.title.data,
                year=form.year.data,
                genre=form.genre.data,
                pages=form.pages.data,
                description=form.description.data,
                is_available=form.is_available.data,
                authors=authors
            )
            db.session.add(new_book)

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('index.html', form=form, books=books, editing_id=book_id)


@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))