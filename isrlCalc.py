
def tipo_afp(afp_tipo):
    """
    Esta funcion devuelve el tipo de afp solicitado en el que esta el 
    asalariado
    """
    if afp_tipo == 1:
        return 7.25, 'Crecer'
    elif afp_tipo == 2:
        return 7.25, 'Confia'
    elif afp_tipo == 3:
        return 6.0, 'IPSFA'
    elif afp_tipo == 4:
        return 7.0, 'ISSS'

def tabla_afp(grabado):
    """
    Esta funcion ubica en que escalafon de la tabla de AFP se encuentra el
    asalariado
    """

    if grabado >= 0.01 and grabado <= 472.01:
        porcentaje = 0.00
        sexceso = 0
        cfija = 0.00
    elif grabado >= 472.01 and grabado <= 895.24:
        porcentaje = 0.1
        sexceso = 472.00
        cfija = 17.67
    elif grabado >= 895.25 and grabado <= 2038.10:
        porcentaje = 0.2
        sexceso = 895.24
        cfija = 60.00
    else:
        porcentaje = 0.3
        sexceso = 2038.10
        cfija = 288.57

    return porcentaje, sexceso, cfija


def islr(sueldo,afp_tipo):
    """
    Esta funcion se encarga de calcular el desgloce de salario en El Salvador
    segun el sueldo por mes que se tiene
    sueldo int 
    afp_tipo int
    return int
    """
    results = []
    #calculo de AFP
    tp_afp, nombre_afp = tipo_afp(afp_tipo)
    calc_afp = round(((sueldo * tp_afp) / 100),2)

    #calculo de ISSS
    isss =round((sueldo * 0.03),2)

    #Calculo de grabado
    grabado =round((sueldo - calc_afp - isss),2)

    #Calculo de retension segun tabla de retenciones
    porcentaje, sexceso, cfija = tabla_afp(grabado)
    exceso = round((grabado - sexceso),2)

    #Porcentaje de exceso
    pexceso = round((exceso * porcentaje),2)
    #Calculo de retencion
    retencion =round((pexceso + cfija),2)

    #Total de descuentos
    descuento_total = round((calc_afp + isss + retencion),2)

    #Sueldo neto mensual
    sueldo_neto = round((sueldo - descuento_total),2)

    #Retorno
    results.append(nombre_afp)
    results.append(calc_afp)
    results.append(isss)
    results.append(grabado)
    results.append(porcentaje)
    results.append(sexceso)
    results.append(exceso)
    results.append(pexceso)
    results.append(retencion)
    results.append(descuento_total)
    results.append(sueldo_neto)

    #Presentacion de datos
    """
    print(f'Remuneracion no agrabada AFP {nombre_afp} : ${calc_afp} ')
    print(f'Remuneracion no agrabada ISSS: ${isss}')
    print(f'Remuneracion grabada : ${grabado}')
    print(f'Porcentaje a aplicar: {porcentaje*100}')
    print(f'Sobre el exceso : ${sexceso}')
    print(f'Exceso : ${exceso}')
    print(f'Porcentaje del exceso: ${pexceso}')
    print(f'Retencion mensual: ${retencion}')
    print(f'Descuento total mensual: ${descuento_total}')
    print(f'Sueldo neto a recibir mensual: ${sueldo_neto}')
    """
    return results


if __name__ == '__main__':
    sueldo = float(input('Ingrese sueldo: '))
    afp = int(input("""
    Tipo de afp:
    1 - Crecer
    2 - Confia
    3 - IPSFA
    4 - ISSS
    """))

    calc_islr = islr(sueldo,afp)
    print(f'Remuneracion no agrabada AFP {str(calc_islr[0])} : ${str(calc_islr[1])} ')
    print(f'Remuneracion no agrabada ISSS: ${str(calc_islr[2])}')
    print(f'Remuneracion grabada : ${str(calc_islr[3])}')
    print(f'Porcentaje a aplicar: {str(calc_islr[4]*100)}')
    print(f'Sobre el exceso : ${str(calc_islr[5])}')
    print(f'Exceso : ${str(calc_islr[6])}')
    print(f'Porcentaje del exceso: ${str(calc_islr[7])}')
    print(f'Retencion mensual: ${str(calc_islr[8])}')
    print(f'Descuento total mensual: ${str(calc_islr[9])}')
    print(f'Sueldo neto a recibir mensual: ${str(calc_islr[10])}')
