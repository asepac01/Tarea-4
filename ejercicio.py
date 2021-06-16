class For:

    def __init__(self):
        pass

    def usoFor(self):
        nombre = "Daniel"
        dato = ["Daniel", 50, True]
        numeros = (2, 5.6, 4, 1)
        profesor = {"nombre": "Daniel", "edad": 50, "fac": "faci"}
        lista_notas = [(30, 40), [20, 40] ,(50, 40)]
        lista_estudiantes = [{"nombre": "Erick", "final": 70}, {"nombre": "Yady", "final": 60}, {"nombre": "Danny", "final": 90}]

        # for i in range(5):
        #     print("i: {}".format(i))
        
        # print("")
        # for i in range(2, 10):
        #     print("i: {}".format(i))
        
        print("")
        for i in range(4, 10, 2):
            print("i: {}".format(i), end="  ")


obj_for = For()
obj_for.usoFor()
