'class Cola:
    def __init__(self):
        self.cola = []
        self.colaVip = []
        self.colaNormal = []
#metodo para agregar elementos en la estructura tipo cola
    def agregar(self, elemento):
        self.cola.append(elemento)

    def ingreso(self):
        while True:
            frecuente = input("  ¿Es cliente frecuente? (s/n):  ")
            if frecuente == "s" or frecuente == "S" or frecuente == "SI" or frecuente == "si":
                tipo = "Cliente frecuente"

            elif frecuente == "n" or frecuente == "N" or frecuente == "NO" or frecuente == "no":
                tipo = "Otro tipo"

            else:
                print("[Error] Ingrese si o no.")
                continue

            nombre = input("  Nombre de cliente:  ")
            apellido = (input("  Apellido:  "))

            if tipo == "Cliente frecuente":
                self.colaVip.append(nombre)
                self.colaVip.append(apellido)
                self.colaVip.append(tipo)

                self.consultarlistaVip()

                print("======================")
                preguntar = input("¿Desea agregar otro cliente?: ")
                if preguntar == "s" or preguntar == "S" or preguntar == "SI" or preguntar == "si":
                    continue
                elif preguntar == "n" or preguntar == "N" or preguntar == "NO" or preguntar == "no":
                    break

            elif tipo == "Otro tipo":
                self.colaNormal.append(nombre)
                self.colaNormal.append(apellido)
                self.colaNormal.append(tipo)

                self.consultarlistaNormal()

                print("======================")
                preguntar = input("¿Desea agregar otro cliente?: ")
                if preguntar == "s" or preguntar == "S" or preguntar == "SI" or preguntar == "si":
                    continue
                elif preguntar == "n" or preguntar == "N" or preguntar == "NO" or preguntar == "no":
                    break

    def consultarlistaNormal(self):
        return print(self.colaNormal)

    def consultarlistaVip(self):
        return print(self.colaVip)

'Cola().ingreso() 
