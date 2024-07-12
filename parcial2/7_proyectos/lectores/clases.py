class Lectores:
    def __init__(self,nombre,direccion,tel):
        self.nombre=nombre
        self.direccion=direccion
        self.tel=tel

    def reservar(self):
        print(f"Esta reservado el libro por: {self.getNombre()} y su telefono es: {self.getTel()}")

    def entregar(self):
        print(f"Esta entregado el libro por: {self.getNombre()} y su telefono es: {self.getTel()}")     

    def getNombre(self):
      return self.nombre
    def getDireccion(self):
      return self.direccion
    def getTel(self):
      return self.tel
    def setNombre(self,nombre):
      self.nombre=nombre
    def setDireccion(self,direccion):
      self.direccion=direccion
    def setTel(self,tel):
      self.tel=tel

class Estudiantes(Lectores):
   def __init__(self,nombre,direccion,tel,carrera,matricula):
     super().__init__(nombre,direccion,tel)
     self._carrera=carrera
     self._matricula=matricula

   def reservar(self):
        print(f"El estudiante: {self.getNombre()} reservo un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

   def entregar(self):
        print(f"El estudiante: {self.getNombre()} entrego un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

   def getCarrera(self):
      return self._carrera
   def getMatricula(self):
      return self._matricula
   
   def setCarrera(self,carrera):
      self._carrera=carrera
   def setMatricula(self,matricula):
      self._matricula=matricula     

class Docentes(Lectores):
   def __init__(self,nombre,direccion,tel,modalidad,num_empleado):
     super().__init__(nombre,direccion,tel)
     self.__modalidad=modalidad
     self.__num_empleado=num_empleado

   def reservar(self):
        print(f"El docente: {self.getNombre()} reservo un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

   def entregar(self):
        print(f"El docente: {self.getNombre()} entrego un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

   def getModalidad(self):
      return self.__modalidad
   def getNum_empleado(self):
      return self.__num_empleado
   
   def setModalidad(self,modalidad):
      self.__modalidad=modalidad
   def setMatricula(self,num_empleado):
      self.__num_empleado=num_empleado