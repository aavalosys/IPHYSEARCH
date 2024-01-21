from envirvars import varse
 
def main():
    filepath= open(varse.pathhosts)
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            print(line)
            line = fp.readline()
     

if __name__ == "__main__":
    main()

menu_options = {
    1: 'Extraer IPs del Backup',
    2: 'Extraer Tabla MAC',
    3: 'Extraer Tabla ARP',
    4: 'Exit',
}

def print_menu():
    print('----------------------------------------------------') 
    for key in menu_options.keys():
        print (key, '-', menu_options[key] )

def option1():
     print('\x1b[2J')
     print('----------------------------------------------------')
     print('Llamando al modulo extraer ips del backup')

def option2():
     print('----------------------------------------------------')
     print('Llamando al modulo extraer tabla MAC')

def option3():
     print('----------------------------------------------------')
     print('Llamando al modulo extraer tabla ARP')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Opción no existe, vuelva a intentarlo')
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('MENSAJE ANTES DE SALIR')
            exit()
        else:
            print('Opción invalida debe seleccionar del  1 and 4.')