# Definir variables
num_mesa = 0
num_per = 0
num_orden = 0
num_ped = 0
num_tacos = [0] * 5
num_burros = [0] * 3
num_chonchos = [0] * 2
num_campechanos = [0] * 3
num_aguas = [0] * 10
num_refrescos = [0] * 5
num_cafe = [0]
num_postre = [0]
trab_nom = ''
pedidos = ''
valicup = ''
opc_categ = 'Z'
opc_ped = 0
opc_i = ''
opc_catbeb = ''
opc_nuevord = 'SI'
cupon = ''
opccupon = ''
ped_total = 0.0
agua_cost = 0.0
totaltotal = 0.0
prec_iva = 0.0
total_iva = 0.0
iva = 0.16
descuento = 0.05

# Arreglo cupones
cupones = ['PSXHSG', 'WOPXGT', 'AWIOLS', 'ESHAIW', 'WOUEDH']

# Arreglos para el menú
tacos = ['pastor', 'asada', 'suadero', 'longaniza', 'chicharon']
t_precio = [19.00, 19.00, 19.00, 19.00, 19.00]

burros = ['asada', 'pastor', 'chicharron']
b_precio = [49.00, 49.00, 49.00]

chonchos = ['asada', 'pastor']
c_precio = [160.00, 160.00]

campechanos = ['asada y pastor', 'longaniza y suadero', 'asada y salchicha']
cam_precio = [25, 25, 25]

agua_sabor = ['Horchata (chica)', 'Jamaica (chica)', 'Limón (chica)', 'Pepino y Limón (chica)', 'Piña (chica)',
              'Horchata (grande)', 'Jamaica (grande)', 'Limón (grande)', 'Pepino y Limón (grande)', 'Piña (grande)']
agua_costo = [25, 40]

otras_bebidas = ['Café', 'Refresco', 'Fresas con crema']
otras_bebidas_precio = [20.00, 25.00, 30.00]

refrescos_sab = ['Coca-Cola', 'Coca Light', 'Sprite', 'Fresca', 'Fanta']

# Interfaz
print('                    ---------------')
print('                    ->EL TOMATITO<-')
print('                    ---------------')

# Información del trabajador (mesero)
trab_nom = input('Ingrese el nombre del trabajador: ')
print('\n' * 100)  # Limpiar Pantalla

# Toma de órdenes
while opc_nuevord.upper() == 'SI':
    num_orden += 1
    totaltotal = 0
    for i in range(10):
        if i < 5:
            num_tacos[i] = 0
        if i < 1:
            num_cafe[i] = 0
        if i < 3:
            num_burros[i] = 0
        if i < 2:
            num_chonchos[i] = 0
        if i < 3:
            num_campechanos[i] = 0
        if i < 10:
            num_aguas[i] = 0
        if i < 5:
            num_refrescos[i] = 0
        if i < 1:
            num_postre[i] = 0

    print('Mesero que atiende:', trab_nom)
    print('Nueva orden', ' ' * 40, 'N.Orden:', num_orden)
    print('                    -->IDENTIFICAR LA MESA<--')
    num_mesa = int(input('Ingrese el numero de mesa a tomar la orden: '))
    num_per = int(input('Ingrese el numero de personas: '))
    print('                    -->TOMAR LA ORDEN<--')

    while True:
        print('                    -->Lista de menús<--')
        print('Seleccione la letra de acuerdo a la categoría de menú que corresponda:')
        print('[A] Tacos [B] Burros [C] Chonchos [D] Campechanos [E] Bebidas [F] Postres [X] Para terminar pedido')
        opc_categ = input().upper()

        if opc_categ == 'A':
            while True:
                print('                    -->MENÚ DE TACOS<--')
                for i in range(5):
                    print(f'[{i + 1}] Tacos de {tacos[i]}..........$ {t_precio[i]}')
                print('[O] PARA SALIR')
                opc_ped = input()
                if opc_ped == 'O':
                    break
                opc_ped = int(opc_ped)
                if 1 <= opc_ped <= 5:
                    print(f'Tacos de {tacos[opc_ped - 1]}')
                    num_ped = int(input('Ingrese el numero de tacos pedidos (por platillo): '))
                    num_tacos[opc_ped - 1] += num_ped
                else:
                    print('Opción no valida. Verifique[!]')
            print('\n' * 100)  # Limpiar Pantalla

        elif opc_categ == 'B':
            while True:
                print('                    -->MENÚ DE BURROS<--')
                for i in range(3):
                    print(f'[{i + 1}] Burros de {burros[i]}..........$ {b_precio[i]}')
                print('[O] PARA SALIR')
                opc_ped = input()
                if opc_ped == 'O':
                    break
                opc_ped = int(opc_ped)
                if 1 <= opc_ped <= 3:
                    print(f'Burros de {burros[opc_ped - 1]}')
                    num_ped = int(input('Ingrese el numero de burros pedidos (por platillo): '))
                    num_burros[opc_ped - 1] += num_ped
                else:
                    print('Opción no valida. Verifique[!]')
            print('\n' * 100)  # Limpiar Pantalla

        elif opc_categ == 'C':
            while True:
                print('                    -->MENÚ DE CHONCHOS<--')
                for i in range(2):
                    print(f'[{i + 1}] Chonchos de {chonchos[i]}..........$ {c_precio[i]}')
                print('[O] PARA SALIR')
                opc_ped = input()
                if opc_ped == 'O':
                    break
                opc_ped = int(opc_ped)
                if 1 <= opc_ped <= 2:
                    print(f'Chonchos de {chonchos[opc_ped - 1]}')
                    num_ped = int(input('Ingrese el numero de chonchos pedidos (por platillo): '))
                    num_chonchos[opc_ped - 1] += num_ped
                else:
                    print('Opción no valida. Verifique[!]')
            print('\n' * 100)  # Limpiar Pantalla

        elif opc_categ == 'D':
            while True:
                print('                    -->MENÚ DE CAMPECHANOS<--')
                for i in range(3):
                    print(f'[{i + 1}] Campechanos de {campechanos[i]}..........$ {cam_precio[i]}')
                print('[O] PARA SALIR')
                opc_ped = input()
                if opc_ped == 'O':
                    break
                opc_ped = int(opc_ped)
                if 1 <= opc_ped <= 3:
                    print(f'Campechanos de {campechanos[opc_ped - 1]}')
                    num_ped = int(input('Ingrese el numero de campechanos pedidos (por platillo): '))
                    num_campechanos[opc_ped - 1] += num_ped
                else:
                    print('Opción no valida. Verifique[!]')
            print('\n' * 100)  # Limpiar Pantalla

        elif opc_categ == 'E':
            while True:
                print('                    -->MENÚ DE BEBIDAS<--')
                print('[A] AGUA FRESCA')
                print('[B] REFRESCOS')
                print('[C] CAFE')
                print('[X] PARA SALIR')
                opc_catbeb = input().upper()

                if opc_catbeb == 'A':
                    while True:
                        print('                    -->MENÚ DE AGUAS FRESCAS<--')
                        for i in range(10):
                            print(f'[{i + 1}] Agua fresca de {agua_sabor[i]}')
                        print('[O] PARA SALIR')
                        opc_ped = input()
                        if opc_ped == 'O':
                            break
                        opc_ped = int(opc_ped)
                        if 1 <= opc_ped <= 10:
                            print(f'Agua fresca de {agua_sabor[opc_ped - 1]}')
                            num_ped = int(input('Ingrese el numero de aguas pedidos (por sabor): '))
                            num_aguas[opc_ped - 1] += num_ped
                        else:
                            print('Opción no valida. Verifique[!]')
                    print('\n' * 100)  # Limpiar Pantalla

                elif opc_catbeb == 'B':
                    while True:
                        print('                    -->MENÚ DE REFRESCOS<--')
                        for i in range(5):
                            print(f'[{i + 1}] Refresco de {refrescos_sab[i]}..........$ {otras_bebidas_precio[1]}')
                        print('[O] PARA SALIR')
                        opc_ped = input()
                        if opc_ped == 'O':
                            break
                        opc_ped = int(opc_ped)
                        if 1 <= opc_ped <= 5:
                            print(f'Refresco de {refrescos_sab[opc_ped - 1]}')
                            num_ped = int(input('Ingrese el numero de refrescos pedidos (por sabor): '))
                            num_refrescos[opc_ped - 1] += num_ped
                        else:
                            print('Opción no valida. Verifique[!]')
                    print('\n' * 100)  # Limpiar Pantalla

                elif opc_catbeb == 'C':
                    print('                    -->MENÚ DE CAFÉ<--')
                    print('[1] Café..........$ 20.00')
                    num_ped = int(input('Ingrese el numero de cafés pedidos: '))
                    num_cafe[0] += num_ped
                    print('\n' * 100)  # Limpiar Pantalla

                elif opc_catbeb == 'X':
                    break
                else:
                    print('Opción no valida. Verifique[!]')
            print('\n' * 100)  # Limpiar Pantalla

        elif opc_categ == 'F':
            print('                    -->MENÚ DE POSTRES<--')
            print('[1] Fresas con crema..........$ 30.00')
            num_ped = int(input('Ingrese el numero de postres pedidos: '))
            num_postre[0] += num_ped
            print('\n' * 100)  # Limpiar Pantalla

        elif opc_categ == 'X':
            break
        else:
            print('Opción no valida. Verifique[!]')
    print('\n' * 100)  # Limpiar Pantalla

    # Cálculo del total
    ped_total = 0.0
    for i in range(5):
        if num_tacos[i] > 0:
            ped_total += num_tacos[i] * t_precio[i]
    for i in range(3):
        if num_burros[i] > 0:
            ped_total += num_burros[i] * b_precio[i]
    for i in range(2):
        if num_chonchos[i] > 0:
            ped_total += num_chonchos[i] * c_precio[i]
    for i in range(3):
        if num_campechanos[i] > 0:
            ped_total += num_campechanos[i] * cam_precio[i]
    for i in range(10):
        if num_aguas[i] > 0:
            if i < 5:
                agua_cost = agua_costo[0]
            else:
                agua_cost = agua_costo[1]
            ped_total += num_aguas[i] * agua_cost
    for i in range(5):
        if num_refrescos[i] > 0:
            ped_total += num_refrescos[i] * otras_bebidas_precio[1]
    if num_cafe[0] > 0:
        ped_total += num_cafe[0] * otras_bebidas_precio[0]
    if num_postre[0] > 0:
        ped_total += num_postre[0] * otras_bebidas_precio[2]

    # Descuento con cupón
    cupon_valido = False
    if input('¿Tiene algún cupón de descuento? (SI/NO): ').upper() == 'SI':
        cupon = input('Ingrese el cupón: ').strip()
        if cupon in cupones:
            ped_total *= (1 - descuento)
            cupon_valido = True

    # Calcular IVA
    total_iva = ped_total * iva
    totaltotal = ped_total + total_iva

    # Imprimir resumen de la orden
    print('---------------')
    print(f'Número de mesa: {num_mesa}')
    print(f'Número de personas: {num_per}')
    print(f'Mesero que atiende: {trab_nom}')
    print(f'Total sin IVA: $ {ped_total:.2f}')
    if cupon_valido:
        print('Cupón aplicado: 5% de descuento')
    print(f'IVA: $ {total_iva:.2f}')
    print(f'Total con IVA: $ {totaltotal:.2f}')
    print('---------------')

    opc_nuevord = input('¿Desea registrar otra orden? (SI/NO): ').upper()
    print('\n' * 100)  # Limpiar Pantalla

print('Fin del programa. Gracias por usar El Tomatito.')
