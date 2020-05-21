from flask import Flask
from flask import redirect
import random

app = Flask(__name__)

# Please pick [a-z] for the id.
# Pick a URL where you want the redirect to go.
sites = [
    {
        'id': 'smizell',
        'url': 'https://smizell.com'
    },
]

def next_site(site_id):
    for index, site in enumerate(sites):
        if site_id == site['id']:
            if index == (len(sites) - 1):
                return sites[0]
            return sites[index + 1]
    return random_site()

def previous_site(site_id):
    for index, site in enumerate(sites):
        if site_id == site['id']:
            if index == 0:
                return sites[len(sites) - 1]
            return sites[index - 1]
    return random_site()

def random_site():
    return random.choice(sites)

@app.route('/', methods=['GET'])
@app.route('/random', methods=['GET'])
def random_route():
    return redirect(random_site()['url'])

@app.route('/site/<string:site_id>/next', methods=['GET'])
def next_route(site_id):
    return redirect(next_site(site_id)['url'])

@app.route('/site/<string:site_id>/previous', methods=['GET'])
def previous_route(site_id):
    return redirect(previous_site(site_id)['url'])
