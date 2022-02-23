def ingrese_numero(msg:str ="Ingrese un número decimal: " ) -> float:

    try:
        numero = float(input(msg))
        return numero
    except:
        print('Valida el ingrese del número, vuelvelo a intentar!')
        return ingrese_numero(msg)