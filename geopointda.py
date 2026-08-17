import pyperclip
import geovincent as geo 

copied_text = pyperclip.paste()
print (f"{copied_text}")
print (f"{copied_text.find('N')}")

if copied_text.find('N') == -1 and copied_text.find('E') == -1 and copied_text.find('°') == -1:
    lat_lon = input('Координаты [Lat Lon] ')
else:
    lat_lon = copied_text

print (f"задано: {lat_lon}")

len_str = input('Расстояние (м) ')
azim_str = input ('Угол  ')

Rerevse = False
Magnetic = 0

if azim_str.find('r') > 0 or azim_str.find('R') > 0:
    Rerevse = True

    azim_str = azim_str.replace('R', '')
    azim_str = azim_str.replace('r', '')
    
if azim_str.find('m') > 0 or azim_str.find('M') > 0:
    
    m = azim_str.find('m')
    
    if m==0:
        m = azim_str.find('M')
        
    Magnetic = float(azim_str[m+1:])
    azim_str = azim_str[0:m]
    
(lat2, lon2) = geo.GetSecondPoint(lat_lon, len_str, azim_str, Rerevse, Magnetic)

result = f"{lat2} {lon2}"
print (result) 
pyperclip.copy(result)
        
# 
# N52°15.979238' E104°18.598956'
# N52.26632063° E104.30998260°
# N52.26632063 E104.30998260
