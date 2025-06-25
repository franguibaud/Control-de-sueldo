import os 
import json

def CargarDatos():
    Datos=[]
    if os.path.exists("Gastos-ingresos.json"):
        with open("Gastos-ingresos.json","r",encoding= "utf-8") as f:
            contenido= f.read().strip()
            if contenido:
                Datos= json.loads(contenido)
        return Datos
    

def GuardarDatos():
    with open("Gastos-ingresos.json","w",encoding= "utf-8") as f:
        json.dump(Datos,f, ensure_ascii=False, indent=4 )



def Menu():
    print("*Control de gastos*")
    print("1. Ingresar Datos")
    print("2. Ver ingresos")
    print("3. Ver gastos")
    print("4. Ver saldo actual")
    print("5. Ver historial")
    print("6. Salir")


Datos= CargarDatos()
    

def ingresoDatos(Datos):
    movimiento= input("ingresar tipo de movimiento: ").lower()
    categoria= input("ingresar tipo de categoria: ").lower()
    monto= (input("ingrese el monto: "))
    fecha= input("ingresar la fecha del ingreso/gasto: ")
    dato= {"movimiento": movimiento, "categoria": categoria, "monto": monto, "fecha": fecha}
    Datos.append(dato)
    GuardarDatos()
    print("Datos guardados")




def VerIngresos():
    SumaIngresos=0
    
    for dato in Datos: 
        
        if dato["movimiento"].lower()=="ingreso":
            monto= int(dato['monto'])
            SumaIngresos+= monto
        
        if SumaIngresos==0:
            print("No hay ingresos cargados")
        else:
            print(f"El monto de los ingresos: {SumaIngresos}")

def VerGastos():
    SumaGastos=0
    
    for dato in Datos:
        if dato["movimiento"].lower()=="gasto":
            monto= int(dato['monto'])
            SumaGastos+= monto
        if SumaGastos==0:
            print("No hay gastos cargados")
        else:
            print(f"El monto de los gastos: {SumaGastos}")

def SueldoActual():
    SumaSaldo=0
    for dato in Datos:
        tipo= dato["movimiento"].lower()
        monto= int(dato['monto'])

        if tipo=="ingreso":
            SumaSaldo+= monto
        elif tipo=="gasto":
            SumaSaldo-= monto
        
    print(f"Sueldo Actual: {SumaSaldo}")

def Historial():
    if len(Datos)==0:
        print("no hay movimientos cargados")
    else:

        for i,dato in enumerate(Datos):
            if dato["movimiento"].lower()=="ingreso" or dato["movimiento"].lower()=="gasto":
                            
                print(f"Dato: {i+1} ")
                print(f"Movimiento: {dato['movimiento']}")
                print(f"Categoria: {dato['categoria']}")
                print(f"Monto: {dato['monto']}")
                print(f"Fecha: {dato['fecha']}")


CargarDatos()


salir= False

while not salir:
    Menu()
    opcion= input("ingrese una opcion [1-5]: ")


    if opcion.isdigit():
        opcion= int(opcion)
        if opcion==1:
            ingresoDatos(Datos)
        elif opcion==2:
            VerIngresos()
        elif opcion==3:
            VerGastos()
        elif opcion==4:
            SueldoActual()
        elif opcion==5:
            Historial()
        elif opcion==6:
            print("apagando el programa...")
            salir=True
        else:
            print("elija una opcion correcta")
    else:
        print("elija un numero")

    if not salir:
        input("aprete Enter para continuar")