from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Главная'
    img = '/static/images/baasploa.jpg'
    href = '/baasploa'
    model = 'Кроссовки BAASPLOA'
    return render_template("index.html", title = title, img = img, href = href, model = model)


@app.route('/jeans')
def jeans():
    jeans_list = [
        {'model': 'Джинсы PAGALEE DENIM', 'size':43, 'price':1500},
        {'model': 'Джинсы Brostem', 'size':42, 'price':1600},
        {'model': 'Джинсы Omaqlo', 'size':41, 'price':1700}
    ]
    return render_template("jeans.html", jeans_list = jeans_list, title = 'Джинсы')


@app.route('/shoes')
def shoes():
    shoes_list = [
        {'model': 'Кеды Bi Bari', 'size':43, 'price':1500},
        {'model': 'Туфли GUSTAS', 'size':42, 'price':1600},
        {'model': 'Туфли ZOLINBERG', 'size':41, 'price':1700}]
    return render_template("shoes.html", shoes_list = shoes_list, title = 'Обувь' )


@app.route('/jackets')
def jackets():
    jackets_list = [
        {'model': 'Куртка KITT LANGZHI', 'size':43, 'price':1500},
        {'model': 'Куртка джинсовая S-GEAR', 'size':42, 'price':1600},
        {'model': 'Куртка джинсовая iUkoworld', 'size':41, 'price':1700}]
    return render_template("jackets.html", jackets_list = jackets_list, title = 'Куртки')


@app.route('/baasploa')
def baasploa():
    title = 'Кроссовки BAASPLOA'
    product =  {'description': 'Легкие, удобные и яркие - эти женские спортивные \
    кроссовки BAASPLOA на шнуровке идеальны для весны, лета и демисезона. Они стали \
    незаменимыми сникерами для активного отдыха и тренировок.',
    'img': '/static/images/baasploa.jpg',
    'price': 700}
    return render_template("baasploa.html", title = title, product = product)


@app.errorhandler(404)
def page_not_found(e):
    title = 'Страница не найдена'
    text = 'Такой страницы не существует'
    return render_template('404.html', title = title, text = text), 404


if __name__ == '__main__':
    app.run(debug=True)
