import os
from flask import Flask, render_template

# create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def index():
    return render_template('index.html')

# Safety & Support Pages
@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/community-guidelines')
def community_guidelines():
    return render_template('community-guidelines.html')

@app.route('/safety-center')
def safety_center():
    return render_template('safety-center.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms-of-service.html')

# Company Pages
@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Advertising Pages
@app.route('/advertising')
def advertising():
    return render_template('advertising.html')

@app.route('/buy-ads')
def buy_ads():
    return render_template('buy-ads.html')

@app.route('/advertising-policies')
def advertising_policies():
    return render_template('advertising-policies.html')

@app.route('/political-ads-library')
def political_ads_library():
    return render_template('political-ads-library.html')

@app.route('/brand-guidelines')
def brand_guidelines():
    return render_template('brand-guidelines.html')

@app.route('/promotions-rules')
def promotions_rules():
    return render_template('promotions-rules.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
