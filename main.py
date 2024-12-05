from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# Timer settings
timeout = 5  # seconds before text disappears
last_written_time = time.time()

@app.route('/')
def index():
    return render_template('index.html', timeout=timeout)

@app.route('/get_timer')
def get_timer():
    global last_written_time
    elapsed_time = time.time() - last_written_time
    remaining_time = timeout - int(elapsed_time)

    if remaining_time <= 0:
        remaining_time = 0

    return jsonify({'remaining_time': remaining_time})

@app.route('/reset_timer')
def reset_timer():
    global last_written_time
    last_written_time = time.time()
    return jsonify({'status': 'timer reset'})

if __name__ == '__main__':
    app.run(debug=True)
