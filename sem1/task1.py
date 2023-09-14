from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Привет мир"


@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'


@app.route('/<int:num_1>/<int:num_2>')
def sum_nums(num_1: int, num_2: int) -> str:
    return str(num_1 + num_2)


@app.route('/string/<string:name>')
def len_word(name: str) -> str:
    return str(len(name))


@app.route('/world')
def world():
    return render_template('index.html')


@app.route('/students/')
def students():
    head = {'first_name': 'имя',
            'last_name': 'фамилия',
            'age': 'возраст',
            'rating': 'средний бал'}

    students_list = [{'first_name': 'иван',
                      'last_name': 'иванов',
                      'age': 18,
                      'rating': 5}, {'first_name': 'петр',
                                                 'last_name': 'петров',
                                                 'age': 22,
                                                 'rating': 8}, {'first_name': 'Кара',
                                                                            'last_name': 'Мара',
                                                                            'age': 19,
                                                                            'rating': 5}]
    return render_template('index.html', **head, students_list=students_list)


@app.route('/news/')
def news():
    news_block = [
        {'title': 'новость_1',
        'description': 'описание_1',
        'creating_at': datetime.now().strftime('%H:%M - %m.%d.%Y года')},
        {'title': 'новость_2',
         'description': 'описание_2',
         'creating_at': datetime.now().strftime('%H:%M - %m.%d.%Y года')},
        {'title': 'новость_3',
         'description': 'описание_3',
         'creating_at': datetime.now().strftime('%H:%M - %m.%d.%Y года')}]
    return render_template('news.html',news_block=news_block)

if __name__ == '__main__':
    app.run(debug=True)
