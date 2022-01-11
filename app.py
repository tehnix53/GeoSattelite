from flask import Flask, render_template, url_for
from database import df
from database2 import df as df2

app = Flask(__name__)
app.secret_key = "randomstring"


@app.route('/')
def drone_start():
    return render_template('index.html')


@app.route('/db')
def drone_table():
    sorted_file = df.sort_values(['name']).values
    return render_template('db.html', df=sorted_file)


@app.route('/map/<id>')
def drone_map(id):
    # category = df.loc[df.id == int(id)]['category'].values[0]
    # N = df.loc[df.id == int(id)]['N'].values[0]
    # E = df.loc[df.id == int(id)]['E'].values[0]
    value = df2.loc[df2.id == int(id)]['val'].values[0]

    return render_template('map.html', id=id, value=value)



@app.route('/about')
def drone_about():
    return render_template('about.html')

@app.route('/upload')
def drone_upload():
    return render_template('upload.html')


#app.run('127.0.0.1', 5000, debug=True)


if __name__ == '__main__':
    app.run()