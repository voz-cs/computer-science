import numpy
import pylab
from datetime import datetime

# Du lieu goc tu MIT (cat bot de file do nang)
data = [(4.9,'2011/03/12 23:57:34'),
(4.9,'2011/03/12 23:53:45'),
(5.0,'2011/03/12 23:51:24'),
(5.2,'2011/03/12 23:40:49'),
(5.1,'2011/03/12 23:37:24'),
(6.1,'2011/03/12 23:24:50'),
(5.4,'2011/03/12 23:20:42'),
(3.0,'2011/03/12 23:12:18'),
(4.7,'2011/03/12 22:53:35'),
(4.8,'2011/03/12 22:42:39'),
(5.6,'2011/03/12 22:31:27'),
(6.3,'2011/03/12 22:12:46')]
# ... tiep tuc voi cac du lieu khac neu can ...

xdata = []
ydata = []

# Dinh dang ngay thang trong data
date_format = "%Y/%m/%d %H:%M:%S"

for t in data:
    # t[0] la Magnitude (Y)
    ydata.append(t[0])
    # t[1] la String ngay/thang -> Chuyen sang doi tuong datetime (X)
    dt_obj = datetime.strptime(t[1], date_format)
    xdata.append(dt_obj)

# Ve bieu do voi ca X va Y
pylab.plot(xdata, ydata, marker='o', linestyle='-', color='b')

# Them cac chi dan vinh quang
pylab.title('Earthquake Magnitude in Japan (Real Time)')
pylab.xlabel('Exact Time')
pylab.ylabel('Magnitude')
pylab.xticks(rotation=45) # Xoay nhan truc X cho de doc
pylab.tight_layout() # Tu thi thiet lap vung dem cho dep
pylab.show()
