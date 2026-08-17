# GEOPointDA
Расчет координаты от заданной точки по расстоянию и азимуту

# RU
Для заданной начальной точки координаты (Lat Lon), начального азимута и расстояния получаем конечную точку (Lan2 Lon2)
Для получения используется прямая задача (проблема) по формуле Винсенти 
https://en.wikipedia.org/wiki/Vincenty%27s_formulae

Если при запуске в буфере обмена есть координаты, но он их использует не предалая ввести координаты
Если координаты не заданы, то предлагается в одну строку ввести начальные коорданаты
Далее вводится расстояние до рассчитываемой точки в метрах
затем вводится истинный азимут в градусах

1. Координаты [Буфер Обмена/Ввод в ручную] (обязательно)
Доступный формат
   - N52°15'58.7542" E104°18'35.9373"
   - N52°15.979238' E104°18.598956'
   - N52.26632063° E104.30998260°
   - N52.26632063 E104.30998260
2. Расстояние в метрах (обязательно)
3. Азимут [120RM10.8]
   - 120 угол в градусах (обязательно)
   - R - обратный азимут (не обязательно)
   - M10.8 - магнитное склонение для расчета магнитного азимута (не обязательно)
  
Результат выводится в консоль и копируется в буфер обмена

# EN
Calculating coordinates from a given point based on distance and azimuth

Given a starting point (Lat, Lon), an initial azimuth, and a distance, we determine the destination point (Lat2, Lon2).
This is calculated using the direct geodetic problem based on Vincenty's formulae.  

If coordinates are present in the clipboard upon startup, the app uses them directly without prompting for manual entry.
If no coordinates are set, the user is prompted to enter the starting coordinates in a single line.
Next, enter the distance to the target point in meters.
Then, enter the true azimuth in degrees.

1. Coordinates [Clipboard / Manual Entry] (required)
Supported formats:
   - N52°15'58.7542" E104°18'35.9373"
   - N52°15.979238' E104°18.598956'
   - N52.26632063° E104.30998260°
   - N52.26632063 E104.30998260
2. Distance in meters (required)
3. Azimuth [120RM10.8]
   - 120: angle in degrees (required)
   - R: back azimuth (optional)
   - M10.8: magnetic declination for calculating magnetic azimuth (optional)
  
The result is output to the console and copied to the clipboard.
