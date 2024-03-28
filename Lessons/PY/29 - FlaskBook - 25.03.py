# # -*- coding: utf-8 -*-
from flask import Flask, render_template
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine,
                        Integer, String, Column)
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql+psycopg2://postgres:12345@localhost/postgres')
session = Session(bind=engine)

Base = declarative_base()
class Book(Base):   #класс, который соответствует таблице
    __tablename__ = 'book'
    book_id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    author_id = Column(Integer(), nullable=False)
    price = Column(Integer(), nullable=False)
    amount = Column(Integer(), nullable=False)

class Author(Base):   #класс, который соответствует таблице
    __tablename__ = 'author'
    author_id = Column(Integer(), primary_key=True)
    author_name = Column(String(50), nullable=False)

menu = ['Первый', 'Второй', 'Третий', 'Четвертый']

# q = session.query(Book)
# print(q)

app = Flask(__name__)
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Про Flask', menu=menu)
@app.route('/about')
def about():
    return render_template('about.html', title='О сайте')
@app.route('/help')
def help():
    return render_template('help.html')
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')
@app.route('/book')
def book():
    q = session.query(Book)
    return render_template('book.html', title='Books', list=q)
@app.route('/book1')
def book1():
    q = session.query(Book, Author).join(Author, Book.author_id == Author.author_id).all()
    return render_template('book1.html', title='Book1', list=q)

if __name__ == "__main__":
    app.run(debug=True)
