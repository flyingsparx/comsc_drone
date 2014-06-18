from flask import Flask, render_template, request, redirect, Response, url_for, session
import time, os, uuid, json, base64, hmac, urllib, random

app = Flask(__name__)
app.secret_key = os.environ.get('ROBOT_SALT')
app.secret_key = 'adfad'

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

def get_maps():
    f = open("maps.json", "r")
    text = f.read()
    map_obj = json.loads(text)
    return map_obj['maps']

def get_map(map_id):
    maps = get_maps()
    m = None
    for map in maps:
        if map['id'] == map_id:   
            m = map
    return m

def complete_level(map_id, map_name, code_lines):
    session['levels_complete'].append({'map_id':map_id,'map_name':map_name,'code_lines':code_lines})
    print session['levels_complete']

@app.route('/')
def home():
    validate_session()
    levels = get_maps()
    print complete_levels
    return render_template('dashboard.html', levels=levels, complete_levels=complete_levels, num_levels=len(levels), num_completed_levels=len(complete_levels))

@app.route('/level/<map_id>')
def level(map_id):
    validate_session()
    m = get_map(map_id)
    return render_template('level.html', level=m, complete_levels=complete_levels)

@app.route('/level/<map_id>/json')
def level_json(map_id):
    m = get_map(map_id)
    return json.dumps(m)

@app.route('/run_drone/<map_id>', methods=['POST'])
def run_drone(map_id):
    validate_session()
    code = request.form['code']

    # count code lines
    line_count = 0
    lines = code.split("\n")
    for line in lines:
        if line.strip() != "\n":
            line_count += 1

    # create and run drone
    uniq = uuid.uuid4()
    drone = open(str(uniq)+".py", "w")
    drone.write(code)
    drone.close()          
    obj = {}
    try:    
        mod = None
        try:
            mod = __reload__(str(uniq))
        except:
            mod = __import__(str(uniq))
        stats = mod.drone.get_stats()
        positions = stats[0]
        finished = stats[1]
        crashed = stats[2]
        print stats
        if stats[-1][4] == "Finished":
            print "completing..."
            complete_level(mod.drone.map['id'], mod.drone.map['name'], line_count)
        obj['result'] = stats
        obj['error'] = False
        try:
            os.remove(str(uniq)+'.py')
            os.remove(str(uniq)+'.pyc')
        except:
            print "cant delete files"
        return json.dumps(obj)
    except:
        obj['error'] = True
        return json.dumps(obj)
    
# Main code
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
 
