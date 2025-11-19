from flask import Flask, render_template, request, jsonify
import redis
import random

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

# Sample activities
ACTIVITIES = [
    {"name": "Read Docker Docs", "category": "Learning"},
    {"name": "Practice Terminal Commands", "category": "Learning"},
    {"name": "Build a Side Project", "category": "Coding"},
    {"name": "Take a 10-min Walk", "category": "Health"},
    {"name": "Listen to a Podcast", "category": "Relaxation"},
    {"name": "Review Code", "category": "Coding"},
    {"name": "Learn a New Language Feature", "category": "Learning"},
    {"name": "Refactor Old Code", "category": "Coding"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest', methods=['GET'])
def suggest():
    activity = random.choice(ACTIVITIES)
    # Increment suggestion counter in Redis
    redis_client.incr('total_suggestions')
    redis_client.incr(f'activity:{activity["name"]}')
    return jsonify(activity)

@app.route('/complete', methods=['POST'])
def complete():
    activity_name = request.json.get('name')
    redis_client.incr('total_completed')
    redis_client.incr(f'completed:{activity_name}')
    return jsonify({'status': 'success'})

@app.route('/stats', methods=['GET'])
def stats():
    total_suggestions = redis_client.get('total_suggestions') or 0
    total_completed = redis_client.get('total_completed') or 0
    
    activity_stats = []
    for activity in ACTIVITIES:
        suggested = redis_client.get(f'activity:{activity["name"]}') or 0
        completed = redis_client.get(f'completed:{activity["name"]}') or 0
        activity_stats.append({
            'name': activity['name'],
            'suggested': int(suggested),
            'completed': int(completed)
        })
    
    return jsonify({
        'total_suggestions': int(total_suggestions),
        'total_completed': int(total_completed),
        'activities': activity_stats
    })

@app.route('/reset', methods=['POST'])
def reset():
    # Clear all Redis keys
    redis_client.flushdb()
    return jsonify({'status': 'success', 'message': 'All stats reset!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
