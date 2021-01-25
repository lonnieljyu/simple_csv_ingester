from flask import flash, render_template, request, redirect

from source import application

# debug
application.config['ENV'] = 'development'
application.config['DEBUG'] = True
application.config['TESTING'] = True


@application.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files or request.files['file'].filename == '':
            flash('Bad file')
            return redirect(request.url)

        file = request.files['file']
        if file:
            flash('Good file')
            return f'Ingested {file.filename}'
    return render_template('index.html')


if __name__ == '__main__':
    application.run()
