from flask import Flask, render_template, request, redirect, url_for, abort, session
from models import ShortURL, db
from utils import get_page_title

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_should_have_been_random';
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create-short-url', methods=('POST', ))
def create_short_url():
    url = request.form.get('url')
    # Fetch the page title of the url
    # This function call can be made asynchronous to improve response time
    page_title = get_page_title(url)
    # Create the short url instance
    short_url = ShortURL(url=url, url_title=page_title)
    db.session.add(short_url)
    db.session.commit()

    return jsonify({
        'url': url_for('short_url', slug=short_url.short_url, _external=True)
    })

