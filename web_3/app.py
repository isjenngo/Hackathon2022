from distutils.log import error
import sqlite3
from flask import Flask, escape, request, render_template, url_for, redirect
app = Flask(__name__)


conexion = sqlite3.connect("penguindb.db", check_same_thread=False) # conectar a base de datos

cursor = conexion.cursor() # cursor para activar execute
usuario = None #
nombre=None
cadena=None

@app.route('/profile', methods=['POST','GET'])
def profile(): #preguntar si este está bien
    '''Esta funcion es ver el profile'''
    '''nombre_db=cursor.execute("SELECT mail FROM users WHERE VALUES (?)",(email))
    print(nombre_db)'''
    if request.method=='GET':
        usuario=request.args.get('usuario')
        nombre=request.args.get('nombre')
        return render_template('profile_2.html',usuario=usuario,nombre=nombre)

@app.route('/login', methods=['POST','GET'])
def index():
    
    if request.method=='POST':
        correo=request.form["email"]
        contrasena=request.form["password"]
        if comparar_base_de_datos(correo,contrasena):
            '''Si se cumple que me abre el login'''
            listilla=[]
            nombre_del_usuario=cursor.execute("select name from users where mail like ?" , [correo])
            print(nombre_del_usuario)
            for row in nombre_del_usuario:
                listilla.append(row) #va metiendo en listilla
            conexion.commit()
            
            print(listilla)
            nombreget=str(listilla[0][0]) #me manda el nombre de usuario
            print(nombreget)
            print(type(nombreget))

            print("nombre_del_usuario",nombre_del_usuario)

            return redirect(url_for('profile', usuario=correo,nombre=nombreget))
        else:
            print("No se pudo")
    

    return render_template("loginvista.html")
#____________COMPARA LA INFORMACION INGRESADA EN LOS CAMPOS DEL LOGIN CON LA BASE DE DATOS-------#
def comparar_base_de_datos(correo,contrasena):
    '''
    ESTA FUNCION COMPARA LOS CAMPOS INGRESADOS EN LOGIN CON LA 
    INFORMACION DE LA BASE DE DATOS
    '''
    try:
        list_user=cursor.execute("select * from users where mail=? and password=?" , [correo,contrasena])
        '''print(list_user)
        list_user=cursor.execute("select * from users where password='%s'" % contrasena)
        print(list_user)
        print(correo)'''
        print(list_user)
        return True
    except ValueError:
        print(ValueError) #Guaedar en una variable para depsues mandar al htmml en caso de que no exista usuario
        return False

#---- Pantalla 1  ----#
@app.route('/desarrolladorweb')
def pantalla_1():
    return render_template('desarrolladorweb.html')
#---- Pantalla 2  ----#
@app.route('/desarrolladorvideo')
def pantalla_2():
    return render_template('desarrolladorvideo.html')
#---- Pantalla 3  ----#
@app.route('/programacionemb')
def pantalla_3():
    return render_template('programacionemb.html')
#---- Pantalla 4  ----#
@app.route('/datascience')
def pantalla_4():
    return render_template('datascience.html')
#---- Pantalla 5  ----#
@app.route('/fullstack')
def pantalla_5():
    return render_template('Fullstack.html')
#---- Pantalla 6  ----#
@app.route('/mobile')
def pantalla_6():
    return render_template('mobile.html')


#--------- TESTS----#
@app.route('/test', methods=["POST", "GET"])
def test():
    if request.method == "POST":
        dsuno = request.form["dsuno"]
        vuno = request.form["vuno"]
        fluno = request.form["fluno"]
        wduno = request.form["wduno"]
        auno = request.form["auno"]
        iuno = request.form["iuno"]
        dsdos = request.form["dsdos"]
        vdos = request.form["vdos"]
        fldos = request.form["fldos"]
        wddos = request.form["wddos"]
        ados = request.form["ados"]
        idos = request.form["idos"]
        dstres = request.form["dstres"]
        vtres = request.form["vtres"]
        fltres = request.form["fltres"]
        wdtres = request.form["wdtres"]
        atres = request.form["atres"]
        itres = request.form["itres"]
        dscalc = int(dsuno) + int(dsdos) + int(dstres)
        vcalc = int(vuno) + int(vdos) + int(vtres)
        flcalc = int(fluno) + int(fldos) + int(fltres)
        wdcalc = int(wduno) + int(wddos) + int(wdtres)
        acalc = int(auno) + int(ados) + int(atres)
        icalc = int(iuno) + int(idos) + int(itres)
        '''global results'''
        results = None
        if dscalc > vcalc and dscalc > flcalc and dscalc > wdcalc and dscalc > acalc and dscalc > icalc:
            results = '¡QUERES SER UN PROGRAMADOR DE ANALISIS DE DATOS E INTELIGENCIA ARTIFICAL!'
            num=1
        elif vcalc > dscalc and vcalc > flcalc and vcalc > wdcalc and vcalc > acalc and vcalc > icalc:
            results = '¡QUERES SER UN DESARROLLADOR DE VIDEOJUEGOS!'
            num=2
        elif flcalc > dscalc and flcalc > vcalc and flcalc > wdcalc and flcalc > acalc and flcalc > icalc:
            results = '¡QUERES SER UN PROGRAMADOR FULLSTACK!'
            num=3
        elif wdcalc > dscalc and wdcalc > vcalc and wdcalc > flcalc and wdcalc > acalc and wdcalc > icalc:
            results = '¡QUERES SER UN DESARROLLADOR WEB!'
            num=4
        elif acalc > dscalc and acalc > vcalc and acalc > wdcalc and acalc > flcalc and acalc > icalc:
            results = '¡QUERES SER UN DESARROLLADOR MOBILE!'
            num=5
        elif icalc > dscalc and icalc > vcalc and icalc > flcalc and icalc > wdcalc and icalc > acalc:
            results = '¡QUERES SER UN PROGRAMACION DE INCRUSTACION EMBEBIDA!'
            num=6

        return render_template('test.html', results=results,num=num)
    else:
        return render_template('test.html')






@app.route('/registrarvista', methods=['POST','GET'])
def register():
    
    if request.method=='POST':
        email = request.form["email"]
        nombre = request.form["nombre"]
        password= request.form["password"]
        # Insert a row of data
        cursor.execute("INSERT INTO users(mail,name,password) VALUES (?,?,?)",(email,nombre,password))
        conexion.commit()
        return render_template('loginvista.html')
    else:
        return render_template("registrarvista.html")



