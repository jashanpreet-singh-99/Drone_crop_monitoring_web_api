WELCOME_MSG = 'Welcome to Farm Simulation, 2023 Demo Day.'

KEY_FARM_NAME = 'f_name'
KEY_FARM_ID = 'farm_id'

KEY_VALID = 'valid'
KEY_GRID = 'grid'

KEY_MARKERS = 'points'

KEY_IMG = 'img'

KEY_G_ID = 'grid_id'
KEY_RPM = 'rpm'
KEY_ALTI = 'altitude'
KEY_STATE = 'state'

## DATABASE
## CONFIG
SERVER = 'localhost'
DB = 'farm_1'
USER = 'sa'
PASSWORD = 'Admin@123'

## QUERY

QUERY_FARMS = 'SELECT * FROM farms'

QUERY_DRONE = 'SELECT * FROM drone WHERE drone_id=0'

QUERY_RESET = 'UPDATE grid SET pred=-1'

def query_i_farm(name, no_marker, markers):
    return "INSERT INTO farms VALUES('" + name + "', " + str(no_marker) + ", '" + markers+"')"

def query_i_drone(grid, rpm, alti):
    return "UPDATE drone SET grid_id='" + grid+ "', rpm=" + str(rpm) + ",altitude=" + str(alti) + "  WHERE drone_id=0"

def query_state_drone(state):
        return "UPDATE drone SET state=" + str(state) + " WHERE drone_id=0"

def query_find_farmid(name):
    return "SELECT farm_id FROM farms WHERE name='" + name + "'"

def query_d_farm(id):
    return "DELETE FROM farms WHERE farm_id=" + str(id)

def query_g_grid(id):
    return "SELECT * FROM grid WHERE farm_id=" + str(id)

def set_grid_pred(grid, pred):
     return "UPDATE grid SET pred=" + str(pred) + " WHERE grid_id='" + grid + "'"

def get_grid_pred(grid):
     return "SELECT pred FROM grid WHERE grid_id='" + grid + "'"

def bulk_insert(id) :
    return "BULK INSERT grid FROM '/home/azureuser/web/"+ str(id) + "_grid.csv' WITH (FIELDTERMINATOR=';')"