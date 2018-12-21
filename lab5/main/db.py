
import MySQLdb

class db:
    def __init__(self,dbname,host='localhost',user='root',password=''):
        self.db = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=dbname
        )
        self.db.set_character_set('utf8')

        self.c = self.db.cursor()

    def insert(self,table,**values):
        col = ''
        val = ''
        for ind in range(len(values.keys())):
            if ind == len(values.keys()) - 1:
                val += '\'' + list(values.values())[ind] + '\''
                col += list(values.keys())[ind]
            else:
                col += list(values.keys())[ind] + ', '
                val += '\'' + list(values.values())[ind] + '\', '

        print('INSERT INTO {} ({}) VALUES ({});'.format(table, col, val))
        self.c.execute('INSERT INTO {} ({}) VALUES ({});'.format(table, col, val))
        self.db.commit()

    def get(self,table,**ifs):
        if len(ifs)>0:
            self.c.execute('SELECT * FROM {} WHERE {}=\'{}\' ;'.format(table,list(ifs.keys())[0],list(ifs.values())[0]))
        else:
            self.c.execute(
                'SELECT * FROM {};'.format(table))
        data = self.c.fetchall()
        normalData = []
        for i in range(len(data)):
            buf = {}
            for j in range(len(data[i])):
                buf[str(j)] = data[i][j]
            normalData.append(buf)
        return normalData

    def query(self,query):
        self.c.execute(query)
        data = self.c.fetchall()
        return data


database = db(
    dbname='rip_lab4',
    password='1'
)

print(database.get('Comments',post='mailru'))
