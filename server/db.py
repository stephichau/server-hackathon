from pymongo import MongoClient
client = MongoClient()
db = client.test


users = [{"name":"Alejandra", "last_name":'Contreras', 'cellnumber':'+56968788625', 'career':'Ingenieria Civil Industrial', 'id':0, 'mail':'acontreras@uc.cl'},
         {"name":"Felipe", "last_name":'Pezao', 'cellnumber':'+56998261204', 'career':'Ingenieria Civil Computacion', 'id':1, 'mail':'fpezao@uc.cl'},
         {"name":"Francisca", "last_name":'Rios', 'cellnumber':'+5688798323', 'career':'Ingenieria Civil Mecanica', 'id':2, 'mail':'frios@uc.cl'},
         {"name":"Andres", "last_name":'Bustos', 'cellnumber':'+56999798775', 'career':'Ingenieria Civil Matematica', 'id':3, 'mail':'abustos@uc.cl'},
         {"name":"Catalina", "last_name":"Poblete", "cellnumber":"+56931221358", "career":"Ingenieria Civil Industrial", "id":4, 'mail':'cpoblete@uc.cl'}]

teachers = [{'id':3, 'curriculum':'He sido ayudante de MAT1610, MAT1620 y MAT1630.'},
            {'id':0, 'curriculum':'Actual ayudante de MAT1640 y MAT1203'}]

courses = [{'sigla':'MAT1610', 'name':'Calculo I', 'teachers':[3]},
           {'sigla':'MAT1620', 'name':'Calculo II', 'teachers':[3]},
           {'sigla':'MAT1630', 'name':'Calculo III', 'teachers':[3]},
           {'sigla':'MAT1640', 'name':'Ecuaciones Diferenciales', 'teachers':[0]},
           {'sigla':'MAT1203', 'name':'Algebra Lineal', 'teachers':[0]}]

def fill_db():
    for user in users:
        db.users.insert_one(user)
    for teacher in teachers:
        db.teachers.insert_one(teacher)
    for course in courses:
        db.courses.insert_one(course)

#a = db.users.find()
#db.users.delete_many({'name':'Alejandra'})

def delete_db():
    pass

if __name__ == '__main__':
    fill_db()
