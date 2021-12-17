import pymysql.cursors
import uuid
import os

class PhoneBook:
    def __init__(self):
        self.namafile = 'phonebook.db'
        self.db = pymysql.connect(host=os.environ['DB_ADDRESS'],
                                    user=os.environ['DB_USERNAME'],
                                    password=os.environ['DB_PASSWORD'],
                                    database=os.environ['DB_NAME'],
                                    port=int(os.environ['DB_PORT']),
                                    cursorclass=pymysql.cursors.DictCursor,
                                    autocommit=False)

    def list(self):
        data = []
        try:
            with self.db.cursor() as cursor:
                cursor.execute('SELECT id, nama, alamat, notelp from phonebook') 
                
                data = cursor.fetchall()

            return dict(status='OK',data=data)
        except:
            return dict(status='ERR',msg='Error')

    def create(self,info):
        try:
            id = str(uuid.uuid1())

            with self.db.cursor() as cursor:
                cursor.execute('INSERT INTO phonebook (id, nama, alamat, notelp) VALUES(%s, %s, %s, %s)', 
                    (id,info['nama'],info['alamat'],info['notelp'],)) 

                self.db.commit()

            return dict(status='OK',id=id)
        except Exception as e:
            return dict(status='ERR',msg='Tidak bisa Create')

    def delete(self,id):
        try:
            with self.db.cursor() as cursor:
                cursor.execute('DELETE FROM phonebook WHERE id = %s', (id,)) 

                self.db.commit()
                
            return dict(status='OK',msg='{} deleted' . format(id), id=id)
        except:
            return dict(status='ERR',msg='Tidak bisa Delete')

    def update(self,id,info):
        try:
            str_set_update = ""
            first = True

            for i in info:
                if not first:
                    str_set_update += ", "
                else :
                    first = False

                str_set_update +=  i + " = '" + info[i] + "' "
            
            with self.db.cursor() as cursor:
                cursor.execute('UPDATE phonebook SET {} WHERE id = %s'.format(str_set_update), (id,)) 

                self.db.commit()

            return dict(status='OK',msg='{} updated' . format(id), id=id)
        except:
            return dict(status='ERR',msg='Tidak bisa Update')

    def read(self,id):
        try:
            data = None
            with self.db.cursor() as cursor:
                cursor.execute('SELECT id, nama, alamat, notelp from phonebook WHERE id = %s', (id,)) 
                
                data = cursor.fetchone()
            return dict(status='OK',id=id,data=data)
        except:
            return dict(status='ERR',msg='Tidak Ketemu')

    def measure(self):
        data = None
        with self.db.cursor() as cursor:
            cursor.execute('SELECT COUNT(*) FROM phonebook') 
            
            data = cursor.fetchone()

        return dict(status="OK",data=dict(record=data))



if __name__=='__main__':
    pd = PhoneBook()
#    ----------- create
#    result = pd.create(dict(nama='royyana',alamat='ketintang',notelp='6212345'))
#    print(result)
#    result = pd.create(dict(nama='ibrahim',alamat='ketintang',notelp='6212341'))
#    print(result)
#    result = pd.create(dict(nama='Ananda', alamat='Dinoyo Sekolahan', notelp='6212345'))
#    print(result)
#    ------------ list
    print(pd.list())
    print(pd.measure())
#    ------------ info
#    print(pd.read('c516b780-2fa2-11eb-bf35-7fc0bd24c845'))



