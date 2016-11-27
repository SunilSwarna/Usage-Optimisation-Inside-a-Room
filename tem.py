import serial
import MySQLdb
import time
import os 
db=MySQLdb.connect("localhost","root","lion123","test") 
cursor=db.cursor()
ser=serial.Serial('/dev/ttyACM0',9600)
l=[]
new=[]
tem=0.0
while(1):
	x=ser.readline()
	l=x.split(':')
	for i in l:
		new=i.split()
	tem=float(''.join(new))
	print tem
#	time.sleep(2)
	sql="INSERT INTO temperature(TIME,DATA) VALUES('%s','%f')"%(str(time.ctime()),tem)
	sql1="UPDATE appliance SET FLAG=%d WHERE APPLI=1"
	cursor.execute(sql)
	db.commit()
	if (tem>32.0):
		os.system('gpio -g write 4 0')
		cursor.execute(sql1%(1))
		db.commit()
		
	else:
		os.system('gpio -g write 4 1')
		cursor.execute(sql1%(0))
		db.commit()
db.close()
