class ordenamiento:
    def __init__(self, lista):
        self.lista= lista
    def burbuja(self):
        n= len(self.lista)
        for i in range(n):
            for j in range (0, n-i-1):
                if self.lista[j]>self.lista[j+1]:
                    self.lista[j],self.lista[j+1]=self.lista[j+1], self.lista[j]
        return self.lista
    def insercion(self):
        n= len(self.lista)
        for i in range(1,n):
            actual= self.lista[i]
            j=i-1
            while j>=0 and actual<self.lista[j]:
                self.lista[j+1]=self.lista[j]
                j-=1
            self.lista[j+1]=actual
        return self.lista
    def seleccion(self):
        for i in range(0, len(self.lista)-1):
            minimo = i
            for j in range(i+1, len(self.lista)):
                if self.lista[j] < self.lista[minimo]:
                    minimo = j
            self.lista[i], self.lista[minimo] = self.lista[minimo], self.lista[i]
        return self.lista
    def mergesort(self, l, r):
        if l < r:
            # Encontrar el punto medio
            m = l + (r - l) // 2

            # Ordenar la primera mitad
            self.mergesort(l, m)

            # Ordenar la segunda mitad
            self.mergesort(m + 1, r)

            # Fusionar las dos mitades
            temp = []
            i = l
            j = m + 1

            while i <= m and j <= r:
                if self.lista[i] <= self.lista[j]:
                    temp.append(self.lista[i])
                    i += 1
                else:
                    temp.append(self.lista[j])
                    j += 1

            while i <= m:
                temp.append(self.lista[i])
                i += 1

            while j <= r:
                temp.append(self.lista[j])
                j += 1

            for i in range(len(temp)):
                self.lista[l + i] = temp[i]

        return self.lista