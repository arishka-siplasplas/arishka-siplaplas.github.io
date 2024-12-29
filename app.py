from flask import Flask, render_template, session, request, url_for, redirect
import os

app = Flask(__name__)
app.secret_key = 'd36696003c071683d5905aef5efda202254cfa716e4c9241d13a33a345eb2f28'  

@app.route("/", methods=['GET', 'POST'])
def main():
    if 'theme' not in session:
        session['theme'] = 'dark-theme'  

    if request.method == 'POST':
        # Переключение темы
        if session['theme'] == 'dark-theme':
            session['theme'] = 'light-theme'
        else:
            session['theme'] = 'dark-theme'
        return redirect(url_for('main'))

    return render_template('index.html', theme=session['theme'])


@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим"



if __name__ == '__main__':
    app.run(port=5002, debug=True)

