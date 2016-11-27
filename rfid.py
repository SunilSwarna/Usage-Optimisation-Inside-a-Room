import serial
import MySQLdb
import os
db=MySQLdb.connect("localhost","root","lion123","test")
cursor=db.cursor()
scr=serial.Serial('/dev/ttyACM1',9600)
ls=[]
ks=[]
ds=[]
count=0;
q1="drop table Tags_ID"
q2="create table Tags_ID(ID VARCHAR(40),count INT)"
q3="update appliance set flag=%d where APPLI=2"
cursor.execute(q1)
db.commit()
cursor.execute(q2)
db.commit()
while(1):
	ini= scr.readline()
	if(len(ini)>0):
		ls=ini.split()
		if(len(ls)>0):
			ks=ini.split(':')
			if(ks[0]=='1'):			
				print ks[1]
				count+=1
				print "Total persons" + str(count)
				if count>3:
					cursor.execute(q3%(1))
					db.commit()
					os.system('gpio -g write 17 1')
				else:
					cursor.execute(q3%(0))
					db.commit()
					os.system('gpio -g write 17 0')
			if(ks[0]=='2'):
				print ks[1]
				some="select count(*) from Tags_ID where ID='%s'"%(ks[1])
				cursor.execute(some)
			        db.commit()
        			res=cursor.fetchall()
        			for row in res:
               			 
                			if(row[0]==0):
						print "ok"
						some1="insert into Tags_ID(ID,count) values('%s',%d)"%(ks[1],1)
                        			cursor.execute(some1)
						db.commit()
					else:
						some3="update Tags_ID set count=count+1 where ID='%s'"%(ks[1])
						cursor.execute(some3)
						db.commit()
                        			


			
