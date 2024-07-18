from flask import Flask, render_template, request,flash, redirect, url_for
from flask_mail import Mail, Message
import os
from downloader import fetch_video_links


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configuration de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_video', methods=['POST'])
def download_video():
    video_url = request.form['video_url']
    video_info = fetch_video_links(video_url)
    if video_info:
        return render_template('download_video.html', title=video_info['title'], 
                               thumbnail=video_info['thumbnail'], 
                               mp4=video_info['mp4'],
                               description=video_info['description'])
    else:
        return "Failed to fetch video information", 400

@app.route('/download_mp3', methods=['POST'])
def download_mp3():
    video_url = request.form['video_url']
    video_info = fetch_video_links(video_url)
    if video_info:
        return render_template('download_mp3.html', title=video_info['title'], 
                               thumbnail=video_info['thumbnail'],
                               audio_low_quality=video_info['audio_low_quality'],
                               audio_high_quality=video_info['audio_high_quality'],
                               description=video_info['description'])
    else:
        return "Failed to fetch video information", 400

@app.route('/download_mp4', methods=['POST'])
def download_mp4():
    video_url = request.form['video_url']
    video_info = fetch_video_links(video_url)
    if video_info:
        return render_template('download_mp4.html', title=video_info['title'], 
                               thumbnail=video_info['thumbnail'], 
                               video_mp4_low_quality=video_info['video_mp4_low_quality'],
                               video_mp4_high_quality=video_info['video_mp4_high_quality'],
                               description=video_info['description'])
    else:
        return "Failed to fetch video information", 400

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        video_link = request.form['video_link']
        message = request.form['message']

        msg = Message(subject=subject,
                      recipients=['contact@gamezonehub.fr'],
                      body=f"Name: {name}\nEmail: {email}\nVideo URL: {video_link}\n\nMessage:\n{message}")
        mail.send(msg)
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/youtube-to-mp3')
def youtube_to_mp3():
    return render_template('youtube-to-mp3.html')

@app.route('/youtube-to-mp4')
def youtube_to_mp4():
    return render_template('youtube-to-mp4.html')

@app.route('/private-downloader')
def private_downloader():
    return render_template('private-downloader.html')

@app.route('/copyright-information')
def copyright_information():
    return render_template('copyright-information.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/terms-of-use')
def terms_of_use():
    return render_template('terms-of-use.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

if __name__ == '__main__':
    app.run(debug=True)
