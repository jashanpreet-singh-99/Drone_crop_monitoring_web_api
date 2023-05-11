from flask import Flask, jsonify, request
import logging
import json
import os
import base64
import pyodbc
import config as c
import csv_from_data as gd

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

def connection():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+c.SERVER+';DATABASE='+c.DB+';UId=' + c.USER + ';PWD=' + c.PASSWORD)
    return cnxn

@app.route("/")
def hello():
    return c.WELCOME_MSG

@app.route('/delete_farm', methods=['POST'])
def delete_farm():
    try:
        content = request.json
        count = 0
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(c.query_d_farm(content[c.KEY_FARM_ID]))
        conn.commit()
        return jsonify({c.KEY_VALID: 1})
    except Exception as e:
        return jsonify({c.KEY_VALID: str(e)}), 422

@app.route('/rename_farm', methods=['POST'])
def rename_farm():
    try:
        content = request.json
        count = 0
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(c.query_d_farm(content[c.KEY_FARM_ID]))
        conn.commit()
        return jsonify({c.KEY_VALID: 1})
    except Exception as e:
        return jsonify({c.KEY_VALID: str(e)}), 422

@app.route('/add_farm', methods=['POST'])
def add_farm():
    try:
        content = request.json
        count = 0
        conn = connection()
        if (c.KEY_FARM_NAME in content.keys()):
            cursor = conn.cursor()
            markers = json.loads(content[c.KEY_MARKERS])
            cursor.execute(c.query_i_farm(content[c.KEY_FARM_NAME], len(markers),content[c.KEY_MARKERS]))
            cursor.execute(c.query_find_farmid(content[c.KEY_FARM_NAME]))
            res = cursor.fetchall()
            id = res[-1][0]
            gd.create_csv_from_data(id, content[c.KEY_MARKERS])
            app.logger.info('BULK -', c.bulk_insert(id))
            cursor.execute(c.bulk_insert(id))
            conn.commit()
            for v in markers:
                tmp = v.split(',')
                app.logger.info('Markers - Lat :' + tmp[0] + ' , Lng :' + tmp[1])
                count += 1
            app.logger.info('Markers Total : ' + content[c.KEY_MARKERS])
        return jsonify({c.KEY_VALID: id})
    except Exception as e:
        return jsonify({c.KEY_VALID: str(e)}), 422

@app.route('/show_farms', methods=['GET'])
def show_farms():
    try:
        cursor = connection().cursor()
        cursor.execute(c.QUERY_FARMS)
        query_result = [ dict(line) for line in [zip([ column[0] for column in cursor.description], row) for row in cursor.fetchall()] ]
        return jsonify({c.KEY_VALID: query_result})
    except Exception as e:
        return jsonify({c.KEY_VALID: str(e)}), 422

@app.route('/get_grid_farms', methods=['POST'])
def get_grid_farms():
    try:
        content = request.json
        cursor = connection().cursor()
        if (c.KEY_FARM_ID not in content.keys()) :
            return jsonify({c.KEY_VALID: 'Error no farm_id passed'})
        cursor.execute(c.query_g_grid(content[c.KEY_FARM_ID]))
        query_result = [ dict(line) for line in [zip([ column[0] for column in cursor.description], row) for row in cursor.fetchall()] ]
        return jsonify({c.KEY_GRID: query_result})
    except Exception as e:
        return jsonify({c.KEY_VALID: str(e) }), 422

@app.route('/drone_info', methods=['POST'])
def drone_info():
    try:
        content = request.json
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(c.query_i_drone(content[c.KEY_G_ID], content[c.KEY_RPM], content[c.KEY_ALTI]))
        cursor.execute(c.set_grid_pred(content[c.KEY_G_ID], content[c.KEY_STATE]))
        conn.commit()
        return jsonify({c.KEY_VALID: 1})
    except Exception as e:
        return jsonify({c.KEY_VALID: str(e) }), 422

@app.route('/get_drone_info', methods=['GET'])
def get_drone_info():
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(c.QUERY_DRONE)
        res = cursor.fetchall()
        cursor.execute(c.get_grid_pred(res[-1][1]))
        res_2 = cursor.fetchall()
        conn.commit()
        return jsonify({c.KEY_VALID:{'grid_id':res[-1][1], 'rpm':res[-1][2], 'altitude':res[-1][3], 'state':res[-1][4], 'pred':res_2[-1][0]}})
    except Exception as e:
        return jsonify({c.KEY_VALID: str(e) }), 422

@app.route('/set_drone_state', methods=['POST'])
def set_drone_state():
    try:
        content = request.json
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(c.query_state_drone(content[c.KEY_STATE]))
        conn.commit()
        return jsonify({c.KEY_VALID:str(1)})
    except Exception as e:
        return jsonify({c.KEY_VALID: str(e) }), 422

@app.route('/get_drone_state', methods=['GET'])
def get_drone_state():
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(c.QUERY_DRONE)
        res = cursor.fetchall()
        conn.commit()
        return jsonify({c.KEY_FARM_ID:res[-1][4]})
    except Exception as e:
        return jsonify({c.KEY_VALID: str(e) }), 422


@app.route('/reset', methods=['GET'])
def reset():
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute(c.QUERY_RESET)
        conn.commit()
        return jsonify({c.KEY_VALID:1})
    except Exception as e:
        return jsonify({c.KEY_VALID: str(e) }), 422

@app.route('/pred_grid', methods=['POST'])
def pred_grid():
    try:
        content = request.json
        photo = content[c.KEY_IMG]
        photo_data = base64.b64decode(photo)
        path = os.path.join(os.getcwd(), str(content[c.KEY_FARM_ID]))
        file_name = content[c.KEY_GRID] + '.png'
        if (not os.path.exists(path)):
            os.mkdir(path)
        with open(os.path.join(path, file_name), "wb") as file:
            file.write(photo_data)
        return jsonify({c.KEY_VALID: str(1)})
    except Exception as e:
        return jsonify({c.KEY_VALID: str(e)}), 422

if __name__ == "__main__":
    
    app.run(host='0.0.0.0', debug=True)