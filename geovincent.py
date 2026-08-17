import math 

#https://en.wikipedia.org/wiki/Vincenty%27s_formulae

def GetSecondPoint(LatLonStr, LenStr, Azimuth, Rerevse, Magnetic):
    #R = float(6371000)  # 6,371km
    #R = float(6367449)  # 6,371km
    R = float(6378245)  # 6,371km

    wgs84_a = float(6378137.0)
    wgs84_b = float(6356752.314245)
    wgs84_f = (wgs84_a-wgs84_b)/wgs84_a
    
    len_f = float(LenStr)
    azim_f = float(Azimuth)
    mag_f = float(Magnetic)
    
    if float(mag_f) > 0:
        azim_f = azim_f + float(mag_f) 
        
    if Rerevse:
        azim_f = -1 * azim_f 
        
    latlon_split = LatLonStr.split(sep=' ')

    # Превращение координаты в число (градусы))
    def getGeo (geostr):
        #print (f"geostr: {geostr}")
    
        geostr = geostr.strip()
    
        geostr = geostr.replace('N', '')
        geostr = geostr.replace('E', '')
    
        g = geostr.find('°')
    
        if g == -1:
            return float(geostr)   
    
        m = geostr.find('\'')
        s = geostr.find('\"')
    
        #print(f"g {g} m {m} s {s}")
    
        geofloat = 0
    
        if s != -1:
            #print(geostr[m+1:s])
        
            geofloat = float(geostr[m+1:s])/60
            geofloat = round(geofloat, 8)  #6
        
        #print(f"geofloat1 {geofloat}")
        
        if m != -1:
            
            # print(geostr[g+1:m])
            geofloat = (geofloat + float(geostr[g+1:m]))/60
            geofloat = round(geofloat, 8)  # 8
        
            #print(f"geofloat2 {geofloat}")
        
        geofloat = float(geostr[0:g]) + geofloat
        
        return geofloat

    lat = getGeo(latlon_split[0])
    lon = getGeo(latlon_split[1])
    
    lat_rad = math.radians(lat)     # φ
    lon_rad = math.radians(lon)      # L
    ang_rad = math.radians(azim_f)
    
    U1 =  math.atan((1-wgs84_f) * math.tan(lat_rad))       
    tanU1 = math.tan(U1)
    cosU1 = math.cos(U1)
    sinU1 = math.sin(U1)

    sigma1 = math.atan2(tanU1, math.cos(ang_rad))
    sinAlfa = cosU1 * math.sin(ang_rad)
    uu = (1 - sinAlfa*sinAlfa) *((wgs84_a*wgs84_a)/(wgs84_b*wgs84_b) - 1)  
    
    k = math.sqrt(1+uu)
    k = (k-1)/(k+1)
    A = (1+0.25*k*k)/(1-k)
    B = k*(1-(3/8)*k*k)         
    
    def delta_sigma(sigma):
        cos2sigma = math.cos(2*sigma1+sigma)
        cos_sigma = math.cos(sigma)
        sin_sigma = math.sin(sigma)

        delta_s = B/6*cos2sigma*(-3+4*sin_sigma*sin_sigma)*(-3+4*cos2sigma*cos2sigma)
        delta_s = B*sin_sigma*(cos2sigma + B/4*(cos_sigma*(-1+2*cos2sigma*cos2sigma)-delta_s))

        #print (f"sigma: {sigma} delta_s {delta_s}") 
    
        sigma = sigma_0 + delta_s 
        
        #print (f"sigma: {sigma}")
    
        return sigma  
    
    sigma_0 = len_f/ (wgs84_b*A)

    sigma = sigma_0

    for i in range (1, 10):
        sigma_prev = sigma  
        sigma = delta_sigma(sigma)
    
        if sigma == sigma_prev:
            break 
        
    cos2sigma = math.cos(2*sigma1+sigma)
    cos_sigma = math.cos(sigma)
    sin_sigma = math.sin(sigma)

    sqrt1 = sinU1 * sin_sigma - cosU1*math.cos(sigma)*math.cos(ang_rad)
    lat2_rad = math.atan2(sinU1*math.cos(sigma) + cosU1*sin_sigma*math.cos(ang_rad), (1-wgs84_f)*math.sqrt(sinAlfa*sinAlfa + sqrt1*sqrt1))

    lon = math.atan2(sin_sigma*math.sin(ang_rad), cosU1*cos_sigma - sinU1*sin_sigma*math.cos(ang_rad))
    C = wgs84_f/16*(1-sinAlfa*sinAlfa)*(4+wgs84_f*(4-3*(1-sinAlfa*sinAlfa)))
    L = lon-(1-C)*wgs84_f*sinAlfa*(sigma+C*sin_sigma*(cos2sigma+C*cos_sigma *(-1+2*cos2sigma*cos2sigma)))

    lon2_rad = lon_rad + L

    ang2_rad = math.atan2(sinAlfa, -sqrt1)

    lat2 = math.degrees(lat2_rad)
    lon2 = math.degrees(lon2_rad)
    ang2 = math.degrees(ang2_rad)

    lat2 = round(lat2, 8)
    lon2 = round(lon2, 8)

    #print (f"GEO Result Point: N{lat2} E{lon2}") 
    
    lat_out = f"N{lat2}"  
    lon_out = f"E{lon2}" 
    
    return lat_out, lon_out
        
    
  