from hashlib import sha256



class Bloque():
    def __init__(self, id, transaccion, fecha, bloque_anterior):
        sefl.id = id
        self.transaccion = transaccion
        self.fecha = fecha
        sefl.bloque_anterior = bloque_anterior

#encriptacion de los bloques
    def clac_hash(self):
        hash_bloque = json.dumpa(self.__dict__, sort_keys=True)
        return sha256(hash_bloque.encode()).hexdigest()


class multi_media():
    dificultad = 2

    def __init__(self):
        self.cadena = []

    def crear_bloque_genecis(self):

        bloque_genecis = Bloque(0,[],0,"0")
        bloque_genecis.hash = bloque_genecis.calc_hash()
        self.cadena.append(bloque_genecis)

    @property
    def ultimo_bloque(self):
        return self.cadena(-1)

    def prueba_trabajo(self, bloque):
        bloque.nonce = 0

        calcular_hash = bloque.calc_hash()
        while not calcular_hash.startswith('0' * multi_media.dificultad):
            bloque.nonce +=1
            calcular_hash = bloque.calc_hash()

        return calcular_hash
