"""
lists and their union/ intersection/ remove elements present in L1 which are also present in L2  
"""
def unionify():
    lista = ['a', 'b', 'c', 'd', 'e']
    listb = ['b', 'd', 'f', 'h', 'i']

    for i in lista:
        if i in listb:
            lista.remove(i)
    return lista
if __name__ == "__main__":
    print unionify()