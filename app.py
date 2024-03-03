from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from gensim.summarization import summarize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_video():
    data = request.get_json()
    video_url = data['video_url']
    video_id = video_url.split('=')[-1]

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ' '.join([t['text'] for t in transcript])
        summary = summarize(text, ratio=0.2)
        return jsonify({'summary': summary})
    except:
        return jsonify({'error': 'Could not fetch transcript or summarize video.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
