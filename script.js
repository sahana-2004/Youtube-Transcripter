function summarizeVideo() {
    var videoUrl = document.getElementById('videoUrl').value;

    fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ video_url: videoUrl })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('summary').innerHTML = '<h2>Summary</h2>' + data.summary;
    })
    .catch(error => console.error('Error:', error));
}
