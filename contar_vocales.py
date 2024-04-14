import unittest


# def contar_vocales(mi_string):
#     resultado = {}
#     for letra in mi_string:
#         if letra == 'a':
#             if 'a' not in resultado:
#                 resultado['a'] = 0
#             resultado['a'] = resultado['a'] + 1
#         if letra == 'e':
#             if 'e' not in resultado:
#                 resultado['e'] = 0
#             resultado['e'] = resultado['e'] + 1
#     return resultado

def contar_vocales(palabra): #palabra es un string
    palabra = palabra.lower()
    vocales = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú') #vocales es tupla
    resultado = {}
    for letra in palabra:
        # if letra in 'aeiou':
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('zzz')
        self.assertEqual(resultado, {})

    def test_contar_a(self):
        resultado = contar_vocales('cas')
        self.assertEqual(resultado, {'a': 1})

    def test_contar_aa(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado, {'a': 2})

    def test_contar_bese(self):
        resultado = contar_vocales('bese')
        self.assertEqual(resultado, {'e': 2})

    def test_contar_besa(self):
        resultado = contar_vocales('besa')
        self.assertEqual(resultado, {'a': 1, 'e': 1})

    def test_contar_casanova(self):
        resultado = contar_vocales('casanova')
        self.assertEqual(resultado, {'a': 3, 'o': 1})

    def test_contar_mUrciElago(self):
        resultado = contar_vocales('mUrciElago')
        self.assertEqual(resultado, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})
    
    #nuevos tests

    def test_aguante_River_Plate(self):
        resultado = contar_vocales('aguante River Plate')
        self.assertEqual(resultado, {'a': 3, 'e': 3, 'i': 1, 'u': 1})
    
    def test_contar_vocales_mayusculas(self):
        resultado = contar_vocales('GALLARDO')
        self.assertEqual(resultado, {'a': 2, 'o': 1})
   
    def test_contar_vocales_acentuadas(self):
        resultado = contar_vocales('música')
        self.assertEqual(resultado, {'ú': 1, 'i': 1, 'a': 1})

    def test_contar_vocales_mezcla(self):
        resultado = contar_vocales('Música')
        self.assertEqual(resultado, {'ú': 1, 'i': 1, 'a': 1})

    def test_contar_vocales_vacias(self):
        resultado = contar_vocales('')
        self.assertEqual(resultado, {})

unittest.main()

# while(True):
#     palabra = input('Ingrese palabra: ')
#     print(contar_vocales(palabra))

