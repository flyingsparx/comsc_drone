from flask import Flask, render_template, request, redirect, Response, url_for, session
import time, os, uuid, json, base64, hmac, urllib, random

app = Flask(__name__)
app.secret_key = os.environ.get('ROBOT_SALT')
app.secret_key = 'adfad'
app.maps = None 

def generate_session():
    return uuid.uuid4()

def validate_session():
    if session == None:
        session['user'] = generate_session()
        session['levels_complete'] = []
    if 'user' not in session:
        session['user'] = generate_session()
        session['levels_complete'] = []
    if session['user'] == None:
        session['user'] = generate_session()
        session['levels_complete'] = []

    global user
    global complete_levels
    user = str(session['user'])
    complete_levels = session['levels_complete']

def load_maps():
    f = open("maps.json", "r")
    text = f.read()
    maps = json.loads(text)
    for i,m in enumerate(maps):
        m['id'] = i+1
    return maps 

def get_map(map_number):
    return app.maps[int(map_number)-1]

def complete_level(map_number, map_name, code_lines):
    for c in session['levels_complete']:
        if c['map_id'] == map_number:
            session['levels_complete'].remove(c) 
    session['levels_complete'].append({'map_id':map_number,'map_name':map_name,'code_lines':code_lines})

@app.route('/')
def home():
    validate_session()
    levels = app.maps 
    print session['levels_complete']
    return render_template('dashboard.html', levels=levels, complete_levels=complete_levels, num_levels=len(levels), num_completed_levels=len(complete_levels))

@app.route('/level/<map_number>')
def level(map_number):
    validate_session()
    m = get_map(map_number)
    m['id'] = int(m['id'])
    return render_template('level.html', level=m, complete_levels=complete_levels)

@app.route('/level/<map_number>/json')
def level_json(map_number):
    m = get_map(map_number)
    return json.dumps(m)

@app.route('/run_drone/<map_number>', methods=['POST'])
def run_drone(map_number):
    validate_session()
    code = request.form['code']

    # count code lines:
    line_count = 0
    lines = code.split("\n")
    for line in lines:
        if line.strip() != "":
            line_count += 1

    return_obj = {}
    try:    
        # create and run drone code:
        drone = None
        maps = app.maps
        exec code

        moves = drone.get_stats()
        # if the drone finished the course, add this map to the session as a complete level:
        if moves[-1][4] == "Finished":
            complete_level(drone.map['id'], drone.map['name'], line_count)

        # Populate and return the move list:
        return_obj['result'] = moves
        return_obj['error'] = False
        return json.dumps(return_obj)
    except Exception as e:
        print e
        return_obj['error'] = True
        return json.dumps(return_obj)
    
# Main code
if __name__ == '__main__':
    app.debug = True
    app.maps = load_maps()
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
 
