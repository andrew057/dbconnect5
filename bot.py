import os
import mysql.connector
import datetime
import calendar
import pytz
import time





def sqlQuery( query, number ):
   ps = os.environ.get('PASSWORD')
   conn = mysql.connector.connect( host = '46.174.50.9', user = 'u11230_testonlik', password = str(ps), database = 'u11230_testonlik' )
   cursor = conn.cursor()
   cursor.execute(query)
   if number == 1:
       result = cursor.fetchall()
       return result
   if number == 2:
       conn.commit()
       cursor.close()
       conn.close()
def timez():
    x = str( datetime.datetime.now(pytz.timezone("Europe/Moscow")) )
    return int( x[11:13]), int( x[14:16]), int( x[17:19])
def mounth():
    x = str( datetime.datetime.now(pytz.timezone("Europe/Moscow")) )
    return int( x[5:7] )
def chislo():
    x = str( datetime.datetime.now(pytz.timezone("Europe/Moscow")) )
    return int( x[8:10] )
def hoursMinutes():
    now = str( datetime.datetime.now(pytz.timezone("Europe/Moscow")) )
    res = now[11:16]
    return int( res[0:2] ) * 60 + int( res[3:5] )
def tostring( string ):
    resa = ''
    for i in range(0, len(string) - 1 ):
        if string[i] == ' ' and string[i+1] == ' ':
            break
        else:
            resa = resa + string[i]
    if string[len(string) - 1] != ' ':
        resa = resa + string[len(string) - 1]
    return resa
result = sqlQuery( "Select id from everyData where Works = '1'", 1 )
i = 0
while True:
    x, y, z = timez()
    if x == 0 and y == 0 and z == 0:
        time.sleep(1)
        if chislo() == 1:
            tmpmounth = mounth() - 1
            number = calendar.monthrange(2019,tmpmounth)[1]
        else:
            number = chislo() - 1
            tmpmounth = mounth()
        if tmpmounth < 10:
            tmpmounth = '0' + str( tmpmounth )
        else:
            tmpmounth = str( tmpmounth )
        if number < 10:
           number = '0' + str( number )
        else:
           number = str( number )
        res = number + '.' + tmpmounth
        players = sqlQuery( "Select id from everyData where Works = '1'", 1 )
        i = 0
        while True:
            try:
               onlik = 1440 - int( sqlQuery( "Select lastGoing from everyData where id = '"+str(players[i][0])+"'", 1 )[0][0] )
               if tostring( str( sqlQuery( 'Select `'+str(res)+'`'+" from everyData where id = '"+str(players[i][0])+"'", 1)[0][0] ) ) == 'None':
                  sqlQuery( 'Update everyData set `' +str(res)+'` =' +"'0'" +"where id = '"+str(players[i][0]) + "'", 2 )
               summ = onlik + int( sqlQuery( 'Select `'+str(res)+'`'+" from everyData where id = '"+str(players[i][0])+"'", 1)[0][0] )
               sqlQuery( "Update everyData set lastGoing = '0' where id = '" + str( players[i][0]) + "'", 2 )
               sqlQuery( 'Update everyData set `' +str(res)+'` = ' + "'"+str(summ)+"'" +"where id = '"+str(players[i][0]) + "'", 2 )
               i = i + 1
            except Exception:
                break
        if chislo() == 5:
            mounths = int( mounth() ) - 1
            mes = ''
            if mounths < 10:
                mes = '0' 
            mes = mes + str( mounths )
            for i in range( 1, calendar.monthrange( 2019,mounths )[1] + 1 ):
                try:
                    if i < 10:
                        day = '0' + str( i )
                    else:
                        day = str( i )
                    tmpkha = str( day ) + '.' + str( mes )
                    sqlQuery( 'alter table everyData drop column `'+str(tmpkha) +'`', 2 )
                except Exception:
                    break
            mounths = mounth()
            mes = ''
            if mounths < 10:
                mes = '0' 
            mes = mes + str( mounths )
            for i in range( 6, calendar.monthrange( 2019,mounths )[1] + 1 ):
                try:
                    if i < 10:
                        day = '0' + str( i )
                    else:
                        day = str( i )
                    tmpkha = str( day ) + '.' + str( mes )
                    sqlQuery( 'alter table everyData add `'+str(tmpkha) +'` varchar(10)', 2 )
                except Exception:
                    break
            mounths = mounth() + 1
            mes = ''
            if mounths < 10:
                mes = '0'
            mes = mes + str( mounths )
            for i in range( 1, 6 ):
                try:
                    day = '0' + str( i )
                    tmpkha = str( day ) + '.' + str( mes )
                    sqlQuery( 'alter table everyData add `'+str(tmpkha) +'` varchar(10)', 2 )
                except Exception:
                    break
