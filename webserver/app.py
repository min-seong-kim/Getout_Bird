import os
import re
from flask import Flask, send_from_directory, jsonify

# ——————————————————————
# 1) App setup
# ——————————————————————
app = Flask(
    __name__,
    static_folder='build',      # your React/Tailwind build output
    static_url_path=''          # serve build/* at /*
)

# Absolute paths to your resource folders
SAVE_FOLDER             = '/home/getout/workspace/watchbird/save'
SAVE_RESULT_FOLDER      = '/home/getout/workspace/watchbird/save_result'
SAVE_SOUNDS_FOLDER      = '/home/getout/workspace/watchbird/audio_socket/received_clips'
SAVE_BIRD_CLASS_FOLDER  = '/home/getout/workspace/watchbird/save_bird_class'

# ——————————————————————
# 2) Frontend routes
# ——————————————————————
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    full_path = os.path.join(app.static_folder, filename)
    if os.path.exists(full_path):
        return send_from_directory(app.static_folder, filename)
    return send_from_directory(app.static_folder, 'index.html')

# ——————————————————————
# 3) “save” image routes
# ——————————————————————
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(SAVE_FOLDER, filename)

# ——————————————————————
# 4) Image-list APIs for SAVE_FOLDER
# ——————————————————————
@app.route('/api/images')
def list_images():
    try:
        files = os.listdir(SAVE_FOLDER)
    except FileNotFoundError:
        return jsonify({'error': 'Save directory not found'}), 404

    images = sorted(f for f in files if f.startswith('frame_') and f.endswith('.jpg'))
    return jsonify(images)

@app.route('/api/latest-image')
def latest_image():
    try:
        files = [f for f in os.listdir(SAVE_FOLDER)
                 if f.startswith('frame_') and f.endswith('.jpg')]
    except FileNotFoundError:
        return jsonify({'error': 'Save directory not found'}), 404

    def idx(name):
        m = re.match(r'frame_(\d+)\.jpg', name)
        return int(m.group(1)) if m else -1

    files.sort(key=idx, reverse=True)
    if not files:
        return jsonify({'error': 'No image found'}), 404

    return jsonify({'imageUrl': f'/images/{files[0]}'} )

# ——————————————————————
# 5) Image-list API for SAVE_RESULT_FOLDER
# ——————————————————————
@app.route('/api/images_result')
def list_result_images():
    try:
        files = os.listdir(SAVE_RESULT_FOLDER)
    except FileNotFoundError:
        return jsonify({'error': 'save_result directory not found'}), 404

    result_images = sorted(
        f for f in files
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    )
    return jsonify(result_images)

# ——————————————————————
# 6) “save_result” image routes
# ——————————————————————
@app.route('/images_result/<path:filename>')
def serve_result_image(filename):
    return send_from_directory(SAVE_RESULT_FOLDER, filename)

# ——————————————————————
# 7) Sound-list API for SAVE_SOUNDS_FOLDER
# ——————————————————————
@app.route('/api/sounds')
def list_sounds():
    try:
        files = os.listdir(SAVE_SOUNDS_FOLDER)
    except FileNotFoundError:
        return jsonify({'error': 'received_clips directory not found'}), 404

    sounds = sorted(f for f in files if f.lower().endswith('.wav'))
    return jsonify(sounds)

# ——————————————————————
# 8) Serve sound files
# ——————————————————————
@app.route('/sounds/<path:filename>')
def serve_sound(filename):
    return send_from_directory(SAVE_SOUNDS_FOLDER, filename)

# ——————————————————————
# 9) Serve bird-class text files
# ——————————————————————
@app.route('/save_bird_class/<path:filename>')
def serve_bird_class(filename):
    return send_from_directory(SAVE_BIRD_CLASS_FOLDER, filename)

# ——————————————————————
# 10) Serve sound result JSON files
# ——————————————————————
@app.route('/sound_results/<path:filename>')
def serve_sound_results(filename):
    return send_from_directory(SAVE_SOUNDS_FOLDER, filename)

# ——————————————————————
# 11) Run
# ——————————————————————
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)

