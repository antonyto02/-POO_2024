from funciones import *
from autos.auto import *
from clientes.cliente import *
from revisiones.revision import *
from usuarios.usuario import *
import getpass


def menu_principal():
    while True:
        usuario_correcto = False
        borrarPantalla()
        print(f"..:: BIENVENIDO A Chevrolet ::..")
        print(f"1.- LOGIN ")
        print(f"2.- REGISTRO ")
        opcion= input("INGRESE UNA OPCIÓN: ")
        if opcion == "1":
            usuario = int(input("Ingrese su número de usuario: "))
            contrasena = input("Ingrese su contraseña: ")
            inicio_sesion = Usuarios.iniciarSesion(usuario, contrasena)
            if inicio_sesion:
                usuario_correcto = True
                borrarPantalla()
                print(f"..:: MENÚ GERENTES ::..")
                print(f"1.- ADMINISTRAR CLIENTES ")
                print(f"2.- ADMINISTRAR USUARIOS ")
                print(f"3.- ADMINISTRAR AUTOS ")
                print(f"4.- ADMINISTRAR SERVICIOS")
                print(f"5.- SALIR")
                opcion= input("INGRESE UNA OPCIÓN: ")
                if opcion == "1":
                    borrarPantalla()
                    print(f" ADMINISTRAR CLIENTES")
                    print(f" ")
                    print(f"1.- Agregar Cliente ")
                    print(f"2.- Mostrar Cliente ")
                    print(f"3.- ACtualizar Cliente ")
                    print(f"4.- Eliminar Cliente ")
                    opcion= input("INGRESE UNA OPCIÓN: ")    

                    if opcion == "1":
                        borrarPantalla()
                        print(f"Agregar Cliente")
                        print(f" ")
                        nif = int(input("Ingrese el nif: "))
                        nombre = input("Ingrese el nombre: ")
                        direccion =input("Ingrese la direccion: ")
                        ciudad =input("Ingrese la ciudad: ")
                        tel =input("Ingrese el teléfono: ")
                        cliente=Clientes(nif, nombre, direccion, ciudad, tel)
                        resultado = cliente.agregarCliente()
                        if resultado:
                            print("CLIENTE AGREGADO CORRECTAMENTE")
                        else:
                            print("Error")
                        esperarTecla()

                    elif opcion == "2":
                        borrarPantalla()
                        print(f" Mostrar Clientes")
                        clientes = Clientes.mostrarClientes()
                        if len(clientes) > 0:
                            print(f"Lista de clientes: ")
                            for i in clientes:
                                print(f"Nif: {i[0]}, Nombre: {i[1]}, direccion: {i[2]}, ciudad: {i[3]}, tel: {i[4]}")
                        else:
                            print(f"No existen clientes registrados...")
                        esperarTecla()
                
                    elif opcion == "3":
                        borrarPantalla()
                        print(f"Actualizar Clientes")
                        nif = int(input("Ingrese el nif: "))
                        nombre = input("Ingrese el nombre: ")
                        direccion =input("Ingrese la direccion: ")
                        ciudad =input("Ingrese la ciudad: ")
                        tel =input("Ingrese el teléfono: ")
                        cliente=Clientes(nif, nombre, direccion, ciudad, tel)
                        resultado = Clientes.actualizarCliente(nif, nombre, direccion, ciudad, tel)
                        if resultado:
                            print(f"El cliente con nif {nif} se actualizó correctamente." )
                        else:
                            print(f"Por favor inténtelo de nuevo más tarde")
                        esperarTecla()

                    elif opcion == "4":
                        borrarPantalla()
                        print(f"Eliminar Cliente")
                        nif = input(f"nif del cliente a eliminar: ")
                        resultado = Clientes.eliminarCliente(nif)
                        if resultado:
                            print(f"El cliente con {nif} se eliminó correctamente." )
                        else:
                            print(f"Por favor inténtelo de nuevo más tarde")
                        esperarTecla()



                elif opcion == "2":
                    borrarPantalla()
                    print(f" ADMINISTRAR USUARIOS")
                    print(f" ")
                    print(f"1.- Agregar usuario ")
                    print(f"2.- Mostrar usuarios ")
                    print(f"3.- ACtualizar usuario ")
                    print(f"4.- Eliminar usuario ")
                    opcion= input("INGRESE UNA OPCIÓN: ")    

                    if opcion == "1":
                        borrarPantalla()
                        print(f"Agregar usuario")
                        print(f" ")
                        usuario = input("Ingrese el usuario: ")
                        contrasena =input("Ingrese la contrasena: ")
                        nombre =input("Ingrese el nombre: ")
                        usuarioo=Usuarios(usuario, contrasena, nombre)
                        resultado = usuarioo.agregarUsuario()
                        if resultado:
                            print("USUARIO AGREGADO CORRECTAMENTE")
                        else:
                            print("Error")
                        esperarTecla()

                    elif opcion == "2":
                        borrarPantalla()
                        print(f" Mostrar Usuarios")
                        usuarios = Usuarios.mostrarUsuarios()
                        if len(usuarios) > 0:
                            print(f"Lista de clientes: ")
                            for i in usuarios:
                                print(f"ID: {i[0]}, Usuario: {i[1]}, contraseña: {i[2]}, nombre: {i[3]}")
                        else:
                            print(f"No existen usuarios registrados...")
                        esperarTecla()
                
                    elif opcion == "3":
                        borrarPantalla()
                        print(f"Actualizar Uusario")
                        id = int(input("Ingrese el id del usuario a actualizar: "))
                        usuario = input("Ingrese el usuario: ")
                        contrasena =input("Ingrese la contrasena: ")
                        nombre =input("Ingrese el nombre: ")
                        resultado = Usuarios.actualizarUsuario(id, usuario, contrasena, nombre)
                        if resultado:
                            print(f"El usuario con ID {id} se actualizó correctamente." )
                        else:
                            print(f"Por favor inténtelo de nuevo más tarde")
                        esperarTecla()

                    elif opcion == "4":
                        borrarPantalla()
                        print(f"Eliminar Usuario")
                        id = input(f"id del usuario a eliminar: ")
                        resultado = Clientes.eliminarCliente(id)
                        if resultado:
                            print(f"El usuario con {id} se eliminó correctamente." )
                        else:
                            print(f"Por favor inténtelo de nuevo más tarde")
                        esperarTecla() 



                elif opcion == "3":
                    borrarPantalla()
                    print(f" ADMINISTRAR AUTOS")
                    print(f" ")
                    print(f"1.- Agregar auto ")
                    print(f"2.- Mostrar autos ")
                    print(f"3.- ACtualizar auto ")
                    print(f"4.- Eliminar auto ")
                    opcion= input("INGRESE UNA OPCIÓN: ")    

                    if opcion == "1":
                        borrarPantalla()
                        print(f"Agregar auto")
                        print(f" ")
                        matricula = input("Ingrese la matricula: ")
                        marca = input("Ingrese la marca")
                        modelo =input("Ingrese el modelo: ")
                        color =input("Ingrese el color: ")
                        nif =input("Ingrese el nif del propietario: ")
                        auto=Autos(matricula, marca, modelo, color, nif)
                        resultado = auto.agregarAuto()
                        if resultado:
                            print("AUTO AGREGADO CORRECTAMENTE")
                        else:
                            print("Error")
                        esperarTecla()

                    elif opcion == "2":
                        borrarPantalla()
                        print(f" Mostrar Autos")
                        autos = Autos.mostrarAutos()
                        if len(autos) > 0:
                            print(f"Lista de autos: ")
                            for i in autos:
                                print(f"Matrícula: {i[0]}, Nif dueño: {i[4]}, marca: {i[1]}, modelo: {i[2]}, color: {i[3]}")
                        else:
                            print(f"No existen autos registrados...")
                        esperarTecla()
                
                    elif opcion == "3":
                        borrarPantalla()
                        print(f"Actualizar Auto")
                        matricula = input("Ingrese la matricula del auto a actualizar: ")
                        marca = input("Ingrese la marca")
                        modelo =input("Ingrese el modelo: ")
                        color =input("Ingrese el color: ")
                        nif =input("Ingrese el nif del propietario: ")
                        auto=Autos(matricula, marca, modelo, color, nif)
                        resultado = Autos.actualizarAuto(matricula, marca, modelo, color, nif, auto)
                        if resultado:
                            print(f"El auto con {matricula} se actualizó correctamente." )
                        else:
                            print(f"Por favor inténtelo de nuevo más tarde")
                        esperarTecla()

                    elif opcion == "4":
                        borrarPantalla()
                        print(f"Eliminar Auto")
                        matricula = input(f"Matricula del auto a actualizar: ")
                        resultado = Autos.eliminarAuto(matricula)
                        if resultado:
                            print(f"El auto con {matricula} se eliminó correctamente." )
                        else:
                            print(f"Por favor inténtelo de nuevo más tarde")
                        esperarTecla()

                elif opcion == "4":
                    borrarPantalla()
                    print(f" REVISONES")
                    print(f" ")
                    print(f"1.- Agregar revison ")
                    print(f"2.- Mostrar revision ")
                    print(f"3.- ACtualizar revison ")
                    print(f"4.- Eliminar revison ")
                    opcion= input("INGRESE UNA OPCIÓN: ")    

                    if opcion == "1":
                        borrarPantalla()
                        print(f"Agregar revisión")
                        print(f" ")
                        no_revision = input("Ingrese el número de revisión: ")
                        cambiofiltro = input("Cambio de filtro (S/N): ")
                        cambioaceite =input("Cambio de aceite (S/N): ")
                        cambiofrenos =input("Cambio de frenos (S/N): ")
                        otros =input("Otro servicio: ")
                        matricula =input("Ingrese la matricula: ")
                        revision=Revisiones(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
                        resultado = revision.agregarServicio()
                        if resultado:
                            print("SERVICIO AGREGADO CORRECTAMENTE")
                        else:
                            print("Error")
                        esperarTecla()

                    elif opcion == "2":
                        borrarPantalla()
                        print(f" Mostrar revisiones")
                        revisiones = Revisiones.mostrarServicios()
                        if len(revisiones) > 0:
                            print(f"Lista de revisiones: ")
                            for i in revisiones:
                                print(f"No revision: {i[0]}, Cambio filtro: {i[1]}, Cambio aceite: {i[2]}, Cambio frenos: {i[3]}, otros: {i[4]}, matricula {i[5]}")
                        else:
                            print(f"No existen autos registrados...")
                        esperarTecla()
                
                    elif opcion == "3":
                        borrarPantalla()
                        print(f"Actualizar Servicio")
                        no_revision = input("Ingrese el número de revisión: ")
                        cambiofiltro = input("Cambio de filtro (S/N): ")
                        cambioaceite =input("Cambio de aceite (S/N): ")
                        cambiofrenos =input("Cambio de frenos (S/N): ")
                        otros =input("Otro servicio: ")
                        matricula =input("Ingrese la matricula: ")
                        resultado = Revisiones.actualizarServicio(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
                        if resultado:
                            print(f"El servicio con ID {no_revision} se actualizó correctamente." )
                        else:
                            print(f"Por favor inténtelo de nuevo más tarde")
                        esperarTecla()

                    elif opcion == "4":
                        borrarPantalla()
                        print(f"Eliminar servicio")
                        no_revision = input(f"No de servicio a eliminar: ")
                        resultado = Revisiones.eliminarServicio(no_revision)
                        if resultado:
                            print(f"El auto con {matricula} se eliminó correctamente." )
                        else:
                            print(f"Por favor inténtelo de nuevo más tarde")
                        esperarTecla()



                elif opcion == "5":
                    print(f"Gracias...")
                    break            
                    
                    

                else: 
                    print(f"Opcion no válida... Intente de nuevo")

        elif opcion == "2":
            borrarPantalla()
            print(f"Agregar usuario")
            print(f" ")
            usuario = input("Ingrese el número usuario: ")
            contrasena =input("Ingrese la contrasena: ")
            nombre =input("Ingrese el nombre: ")
            usuarioo=Usuarios(usuario, contrasena, nombre)
            resultado = usuarioo.agregarUsuario()
            if resultado:
                print("USUARIO AGREGADO CORRECTAMENTE")
            else:
                print("Error")
                esperarTecla()

        

            
        
if __name__ == "__main__":
    menu_principal()