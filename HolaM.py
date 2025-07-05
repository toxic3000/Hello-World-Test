while True:
    print("Hola mundo")
    print("Menú:")
    print("1. ¿Qué es Python?")
    print("2. ¿Qué es Visual Studio Code?")
    print("3. Diferencia entre Git y GitHub")
    print("4. Salir")
    
    opcion = input("Elige una opción (1, 2, 3 o 4): ")
    
    if opcion == "1":
        print("Python es un lenguaje de programación interpretado, de alto nivel y propósito general, conocido por su sencillez y legibilidad.")
    elif opcion == "2":
        print("Visual Studio Code es un editor de código fuente desarrollado por Microsoft, que soporta depuración, control de versiones y muchas extensiones.")
    elif opcion == "3":
        print("Git es un sistema de control de versiones distribuido, mientras que GitHub es una plataforma en línea para alojar repositorios Git y colaborar en proyectos.")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
    input("Presiona Enter para regresar al menú...")