# Gestor-de-Notas-Acad-micas
El proyecto Gestor de Notas Académicas tiene como idea principal crear un programa que funcione desde la consola y ayude a llevar un control ordenado de los cursos y calificaciones de un estudiante. A través de un menú con 13 opciones, se podrá registrar, consultar, modificar, borrar y revisar notas de forma rápida y sin complicaciones.

Además de ser útil, este proyecto también pone en práctica conceptos importantes de algoritmos y estructuras de datos, como pilas, colas, búsquedas y métodos de ordenamiento. Por ejemplo, se usará una cola para manejar las solicitudes de revisión de notas y otra estructura para guardar un historial de cambios. Todo esto con el objetivo de aplicar lo aprendido en el segundo semestre de ingeniería, programando todo en Python.

Funcionales:

Agregar un curso con su nota.

Ver todas las notas guardadas.

Cambiar la nota de un curso.

Borrar un curso con su nota.

No funcionales:

El programa se va a usar desde la consola y estará hecho en Python.

No va a usar librerías externas.

Va a funcionar con bucles y condicionales.

Antes de hacerlo, se va a escribir todo en pseudocódigo.

INICIO
    MIENTRAS opcion != 6 HACER
        IMPRIMIR "===== GESTOR DE NOTAS ACADÉMICAS ====="
        IMPRIMIR "1. Agregar curso y nota"
        IMPRIMIR "2. Ver todas las notas"
        IMPRIMIR "3. Modificar nota de un curso"
        IMPRIMIR "4. Eliminar curso"
        IMPRIMIR "5. Revisar historial de cambios"
        IMPRIMIR "6. Salir"
        IMPRIMIR "Elige una opción:"
        LEER opcion

        SI opcion == 1 ENTONCES
            <lógica para agregar curso y nota>
        SINO SI opcion == 2 ENTONCES
            <lógica para mostrar todas las notas>
        SINO SI opcion == 3 ENTONCES
            <lógica para modificar una nota>
        SINO SI opcion == 4 ENTONCES
            <lógica para eliminar un curso>
        SINO SI opcion == 5 ENTONCES
            <lógica para revisar historial de cambios>
        SINO SI opcion == 6 ENTONCES
            IMPRIMIR "Saliendo del programa..."
        SINO
            IMPRIMIR "Opción no válida, intenta de nuevo."
        FIN_SI
    FIN_MIENTRAS
FIN
