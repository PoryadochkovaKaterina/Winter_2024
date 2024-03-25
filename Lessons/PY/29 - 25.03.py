from flask import Flask, render_template
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import (create_engine, MetaData, Table,
                        Integer, String, Column,
                        DateTime, ForeignKey, Numeric,
                        SmallInteger)
from sqlalchemy.orm import relationship, declarative_base

engine = create_engine('postgresql+psycopg2://postgres:*****@localhost/postgres')
session = Session(bind=engine)

Base = declarative_base()
class Book(Base):   #класс, который соответствует таблице
    __tablename__ = 'book'
    book_id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    author_id = Column(Integer(), nullable=False)
    price = Column(Integer(), nullable=False)
    amount = Column(Integer(), nullable=False)
menu = ['Первый', 'Второй', 'Третий', 'Четвертый']

q = session.query(Book)

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
    return render_template('book.html', title='Books', list=q)

if __name__ == "__main__":
    app.run(debug=True)
