from flask import Flask, render_template, request, redirect, url_for, abort, session, jsonify, send_from_directory
from models import ShortURL, db
from utils import get_page_title, generate_random_string
import settings

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'this_should_have_been_random'
app.config.from_object(settings)
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/static/css/<path:path>')
#def send_css(path):
#    return send_from_directory('css', path)

@app.route('/create-short-url', methods=('POST', ))
def create_short_url():
    url = request.form.get('url')
    custom_url = request.form.get('custom_url')
    print url, custom_url
    # Fetch the page title of the url
    # This function call can be made asynchronous to improve response time
    #page_title = get_page_title(url)
    page_title = ""
    short_url = custom_url if custom_url!="" else generate_random_string()
    # Create the short url instance
    shorturl = ShortURL(url=url, short_url=short_url, url_title=page_title)
    db.session.add(shorturl)
    db.session.commit()

    return jsonify({
        'url': url_for('short_url', shorturl=shorturl.short_url, _external=True)
    })

@app.route('/s/<shorturl>')
def short_url(shorturl):
    short_url_ = ShortURL.query.filter_by(short_url=shorturl).first()

    if not short_url_:
        return abort(404)

    return render_template('short_url.html', short_url=short_url_)

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True)
