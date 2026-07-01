#encoding=utf-8

import MySQLdb, os
from django.core.checks.registry import Tags

def insertDomain(db):
    cursor = db.cursor()
    sql = "insert into %(table)s (%(para)s) values ('%(value)s')"
    insertValues = {'table' : 'quotation_domain', 'para' : 'name', 'value' : 'CD'}
    f = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'domain', 'r+')
    for line in f.readlines():
        line = line.strip()
        if('' != line):
            insertValues['value'] = line
            exesql = sql % insertValues
            cursor.execute(exesql)
    db.commit()
    db.close()
    
def insertSubDomain(db):
    cursor = db.cursor()
    sql = "insert into %(table)s (%(para)s) values ('%(value)s')"
    insertValues = {'table' : 'quotation_domain', 'para' : 'name', 'value' : 'CD'}
    insertValues['table'] = 'quotation_subdomain'
    f = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'subdomain', 'r+')
    for line in f.readlines():
        line = line.strip()
        if('' != line):
            insertValues['value'] = line
            exesql = sql % insertValues
            cursor.execute(exesql)
    db.commit()
    db.close()
    
def insertRegion(db, tableName, valueTag, fileName):
    cursor = db.cursor()
    sql = "insert into %(table)s (%(valueTag)s) values ('%(value)s')"
    insertValues = {'table' : tableName, 'valueTag' : valueTag, 'value' : 'xxxxx'}
    #print sql % insertValues
    f = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + fileName, 'r+')
    for line in f.readlines():
        line = line.strip()
        if('' != line):
            para = line.split('**')
            if(len(para) > 1):
                insertValues['value'] = para[0].strip()
                cursor.execute(sql % insertValues)
    db.commit()
    db.close()

def insertValuesWithForignKey(db, table, tagValue, tagForKey, f_table, f_tagvalue, fileName = 'unitid'):
    cursor = db.cursor()
    sql = "insert into %(table)s (" + tagValue + "," + tagForKey + ") values ('%(" + tagValue + ")s', %(" + tagForKey + ")s)"
    insertValues = {'table' : table, tagValue : 'OMS CD', tagForKey : 1}
    
    f = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + fileName, 'r+')
    
    f_id = -1
    exeTimes = 0
    for line in f.readlines():
        exeTimes += 1
        line = line.strip()
        if('' != line):
            para = line.split('**')
            if(len(para) > 1):
                f_name = para[0].strip()
                cursor.execute("select id from %s where %s='%s'" % (f_table, f_tagvalue, f_name))
                f_id = cursor.fetchone()[0]
                insertValues[tagValue] = para[1].strip().replace('\'', "\\'")
                insertValues[tagForKey] = f_id
                print sql % insertValues
            else:
                insertValues[tagValue] = para[0].strip().replace('\'', "\\'")
                insertValues[tagForKey] = f_id
                print sql % insertValues
            cursor.execute(sql % insertValues)
        
        if(exeTimes % 10 == 0):
            db.commit()
            #pass
    db.commit()
    db.close()

def insertWorkcenter(db, tableName, fileName, *tags):
    if(4 != len(tags)):
        return False
    else:
        cursor = db.cursor()
        sql = "insert into %(tableName)s (" + tags[0] + "," + tags[1] + "," + tags[2] + "," + tags[3] + ") values ('%(" + tags[0] + ")s','%(" + tags[1] + ")s','%(" + tags[2] + ")s','%("+ tags[3] +")s')".encode('utf-8')
        insertDatas = {
                       'tableName' : tableName,
                       tags[0] : '',
                       tags[1] : '',
                       tags[2] : '',
                       tags[3] : ''
                       }
        f = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + fileName, 'r+')
        
        cIndex = 0
        for line in f.readlines():
            cIndex += 1
            if('' != line):
                para = line.split('**')
                if(len(para) > 3):
                    insertDatas[tags[0]] = para[0].strip().replace("\'", "\\'").encode('utf-8')
                    insertDatas[tags[1]] = para[1].strip().replace("\'", "\\'").encode('utf-8')
                    insertDatas[tags[2]] = para[2].strip().replace("\'", "\\'").encode('utf-8')
                    insertDatas[tags[3]] = para[3].strip().replace("\'", "\\'").encode('utf-8')
                    #print (sql % insertDatas).encode('utf-8')
                    cursor.execute((sql % insertDatas).encode('utf-8'))
            if(cIndex % 10 == 0):
                db.commit()
        db.commit()
        db.close()

def insertPostatus(db, fileName):
    cursor = db.cursor()
    sql = "insert into quotation_postatus (name) values ('%s')"
    f = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + fileName, 'r+')
    for line in f.readlines():
        line = line.strip()
        if('' != line):
            exesql = sql % line
            cursor.execute(exesql)
    db.commit()
    db.close()

def insertOrderingcompany(db, fileName):
    cursor = db.cursor()
    sql = "insert into quotation_orderingcompany (name) values ('%s')"
    f = open(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + fileName, 'r+')
    
    cIndex = 0
    for line in f.readlines():
        cIndex += 1
        line = line.strip()
        if('' != line):
            exesql = sql % line
            #print exesql
            cursor.execute(exesql)
        if( 0 == cIndex % 10):
            db.commit()
    db.commit()
    db.close()

if __name__ == '__main__':
    host = "localhost"
    passwd = "tatool"
    user = "tatool"
    dbname = "eeep"
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname)
    
    #insertDomain(db)
    #insertSubDomain(db)
    #insertValuesWithForignKey(db, 'quotation_unitid', 'name', 'domain_id', "quotation_domain", "name")
    #insertRegion(db, 'quotation_region', 'name', 'regionandcountry')
    #insertValuesWithForignKey(db, 'quotation_country', 'name', 'region_id', "quotation_region", "name", 'regionandcountry')
    #insertWorkcenter(db, 'quotation_workcenter', 'workcenter', 'number', 'descworkcenter', 'icrrbactivitytype', 'intracompanyactivitytyoe')
    #insertPostatus(db, 'postatus')
    insertOrderingcompany(db, 'orderingcompany')