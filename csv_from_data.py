import pandas as pd

def is_point_in_polygon(x, y, polygon):
    n = len(polygon) // 2
    num_intersections = 0
    #print((polygon))
    for i in range(n):
        xi, yi = polygon[2*i], polygon[2*i+1]
        xj, yj = polygon[(2*i+2) % (2*n)], polygon[(2*i+3) % (2*n)]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            num_intersections += 1
    return num_intersections % 2 == 1

def create_csv_from_data(farmId,polygon):
    var = polygon.replace('\\', '')
    var = eval(var)
    t = []
    for i in var:
        print(i)
        tmp = i.split(',')
        t.append(float(tmp[0]))
        t.append(float(tmp[1]))
    polygon = t

    latitudes = polygon[0::2]
    longitudes = polygon[1::2]
    min_lat = min(latitudes)
    max_lat = max(latitudes)
    min_lon = min(longitudes)
    max_lon = max(longitudes)
    deltaLat = (max_lat - min_lat)/16
    deltaLon = (max_lon - min_lon)/16
    lstGridPoints = []
    countminlat = min_lat

    # create grid
    count = 0
    while countminlat < max_lat:  
        if(count % 2 == 1):
            countminlon = max_lon
            while countminlon > min_lon:
                lstGridPoints.append(countminlat);        
                lstGridPoints.append(countminlon);    
                countminlon-=deltaLon
        else:    
            countminlon = min_lon
            while countminlon < max_lon:
                lstGridPoints.append(countminlat);        
                lstGridPoints.append(countminlon);    
                countminlon+=deltaLon
        countminlat+=deltaLat
        count += 1
    #print(lstGridPoints)

    count = 0
    lstPolyGridPoints= []
    length = len(lstGridPoints)

    # check if grid point is in polygon
    while count < length:
        if(is_point_in_polygon(lstGridPoints[count], lstGridPoints[count + 1], polygon)):
            lstPolyGridPoints.append(lstGridPoints[count])
            lstPolyGridPoints.append(lstGridPoints[count + 1])
        count += 2

    # Example list of floats
    float_list = lstPolyGridPoints

    # Convert list of floats to list of tuples with consecutive values
    tuple_list = [(float_list[i], float_list[i+1]) for i in range(0, len(float_list)-1, 2)]
    previousX = tuple_list[0][0]
    countI = 0
    countJ = 0
    lstDictionary = []
    for point in tuple_list:
        data = {}
        if(previousX != point[0]):
            previousX = point[0]
            countJ += 1 
        data["farm_id"] = farmId
        data["grid_id"] = 'G_' + str(countI) + '_' + str(countJ)
        data["tp_l"] = (point[0] - deltaLat/2, point[1] + deltaLon/2)
        data["tp_r"] = (point[0] + deltaLat/2, point[1] + deltaLon/2)
        data["bt_r"] = (point[0] + deltaLat/2, point[1] - deltaLon/2)
        data["bt_l"] = (point[0] - deltaLat/2, point[1] - deltaLon/2)
        data["pred"] = -1
        countI += 1
        lstDictionary.append(data)
    
    df = pd.DataFrame(lstDictionary)
    df.head()
    df.to_csv(str(farmId) + '_grid.csv', index=False, sep=';',  header=False)