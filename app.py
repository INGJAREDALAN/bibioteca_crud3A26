from dao.libro_dao import LibroDAO
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

def ver_libros():
    try: 
        libro_dao = LibroDAO()
        
        libros = libro_dao.obtener_todos()

        print(" === libros en la biblioteca ===")

        if len(libros) == 0:
            print("No hay libros registrados.")
        else:
            for libro in libros: 
                print("--------------------------------")
                print(
                    f"ID: {libro.id}, Titulo: {libro.titulo}, "
                    f"Autor: {libro.autor}, ISBN: {libro.isbn}, "
                    f"Disponible: {'Si' if libro.disponible else 'No'}"
                )
                print("-------------------------------")
        print("\n Conexion Exitosa a la Base de Datos")
    except Exception as e:
        print("Cual es el Error:")
        print(e)

def insertar_libro():
    titulo = input("Escrribe el titulo del libro: ")
    autor = int(input("Escribe el nombre del autor: "))
    isbn = input("Escriba el isbn del nuevo libro: ")
    disponible = True
    try:

        libro_dao = LibroDAO()
        id = libro_dao.obtener_ultimo_id() + 1
        print(f"ID: {id}")
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.insertar(libro)
        print("Insercion realizada con éxito")
    except Exception as e:
        print("Error al inssrtar un nuevo libro")
        print(e)

def actualizar_libro():
    print("Selecciona el libro a actualizar")
    try:
        libro_dao = LibroDAO()
        ver_libros()
        libros = libro_dao.obtener_todos()
        id = int(input("Escribe el id del libro a actualizar: "))
        titulo = input("Escribe el nuevo titulo")
        autor = input("Escribe el nuevo autor")
        isbn = input("Escribe el nuevo ISBN")
        disponible = bool(input("Escribe el nuevo valor disponible"))
        libro = Libro(id, titulo,autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print(f"El libro {id} se ha actualizado exitosamente")

    except Exception as e:
        print("Error al actualizar un libro")
        print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles:")
        ver_libros()
        id = int(input("Escribe el id del libro a elimar: "))
        libro_dao.eliminar(id)
        print(f"El libro {id} ha sido eliminado con exito")
    except Exception as e:
        print(f"Error al eliminar el libro {id}")
        print(e)



def ver_usuario():
    try: 
        usuario_dao = UsuarioDAO()
        
        usuarios = usuario_dao.obtener_todos()

        print(" === usuarios en la biblioteca ===")

        if len(usuarios) == 0:
            print("No hay usuarios registrados.")
        else:
            for usuario in usuarios: 
                print("--------------------------------")
                print(
                    f"ID: {usuario.id}, Nombre: {usuario.nombre}, "
                    f"Usuario: {usuario.matricula}, Carrera: {usuario.carrera}, "
                    f"Correo Electronico: {usuario.correo}"
                )
                print("-------------------------------")
        print("\n Conexion Exitosa a la Base de Datos")
    except Exception as e:
        print("Cual es el Error:")
        print(e)


def menu_libro():
    print("1. Ver todos los libros")
    print("2. Insertar un nuevo libro disponible")
    print("3. Actualizar un libro disponible")
    print("4. Eliminar un libro disponible")
    opcion = int(input("Selecciona una opción (1-4): "))

    match opcion:
        case 1:
            ver_libros()
        case 2: 
            insertar_libro()
        case 3:
            actualizar_libro()
        case 4: 
            eliminar_libro()

def insertar_usuario():
    nombre = input("Escribe el nombre del usuario: ")
    matricula = input("Escribe el numero de la matrucla: ")
    carrera = int(input("Escriba la carrera del nuevo usuario: "))
    correo = input("Escribe el correo del nuevo usuario: ")
    try:

        usuario_dao = UsuarioDAO()
        id = usuario_dao.obtener_ultimo_id() + 1
        print(f"ID: {id}")
        usuario = Usuario(id, nombre, matricula, carrera, correo)
        usuario_dao.insertar(usuario)
        print("Insercion realizada con éxito")
    except Exception as e:
        print("Error al inssrtar un nuevo libro")
        print(e)

def actualizar_usuario():
    print("Selecciona el usuario a actualizar")
    try:
        usuario_dao = UsuarioDAO()
        ver_usuario()
        libros = usuario_dao.obtener_todos()
        id = int(input("Escribe el id del usuario a actualizar: "))
        nombre = input("Escribe el nuevo nombre")
        matricula = input("Escribe la nueva matricula")
        carrera = int(input("Escribe la nueva carrera"))
        correo = input("Escribe el nuevo correo ")
        usuario = Usuario(id, nombre,matricula, carrera, correo)
        usuario_dao.actualizar(usuario)
        print(f"El usuario {id} se ha actualizado exitosamente")

    except Exception as e:
        print("Error al actualizar el usuario ")
        print(e)

def eliminar_usuario():
    try:
        usuario_dao = UsuarioDAO()
        print("Lista de usuarios: ")
        ver_usuario()
        id = int(input("Escribe el id del usuario a elimar: "))
        usuario_dao.eliminar(id)
        print(f"El usuario {id} ha sido eliminado con exito")
    except Exception as e:
        print(f"Error al eliminar usuario {id}")
        print(e)
    



def menu_usuarios():
    print("1. Ver todos los usuarios")
    print("2. Insertar un nuevo usuario")
    print("3. Actualizar un usuario existente")
    print("4. Eliminar un usuario existente")
    opcion = int(input("Selecciona una opción (1-4): "))

    match opcion:
        case 1:
            ver_usuario()
        case 2: 
            insertar_usuario()
        case 3:
            actualizar_usuario()
        case 4: 
            eliminar_usuario()

def main():
    print("=== BIBLIOTECA UNIVERSITARIA ===")
    print("Menu de opciones")
    print("1 - Libros")
    print("2 - Usuarios")
    option = int(input("Selecciona una opción 1 o 2: "))

    match option:
        case 1:
            menu_libro()
        case 2:
            menu_usuarios()
    
    
if __name__ == "__main__":
    main()