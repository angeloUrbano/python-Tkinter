from tkinter import *

import tkinter as tk

import sqlite3

from tkinter import ttk

from tkinter import messagebox



"""miconexion=sqlite3.connect("BIBLIOTECA")

mi_cursor=miconexion.cursor()


mi_cursor.execute('''

	CREATE TABLE ADMINISTRADOR(
	NOMBRE VARCHAR(50) UNIQUE,
	APELLIDO VARCHAR(50),
	TELEFONO VARCHAR(70),
	PASSWORD VARCHAR(70),
	CORREO VARCHAR(70));
	''')

mi_cursor.execute("INSERT INTO ADMINISTRADOR VALUES ('angelo' , 'urbano' , 04125616872 , 'Angelo2611#' , 'angelourbannoo@gmail.com')")	
miconexion.commit()

miconexion.close()





miconexion=sqlite3.connect("BIBLIOTECA")

mi_cursor=miconexion.cursor()

mi_cursor.execute('''

	CREATE TABLE LIBROS(
	ID INTEGER  PRIMARY KEY AUTOINCREMENT,
	NOMBRE_LIBROS VARCHAR(100),
	Autor_del_Libro VARCHAR(70),
	Editorial_del_Libro VARCHAR(100),
	Cantidad_Existente INTEGER,
	Carrera VARCHAR(50),
	Numero_de_Estante INTEGER );

''')"""




#____________________________CRUD INTERNO _______________



class ventana_interna():


	def __init__(self):


		self.raiz2=Tk()
		self.raiz2.title("Menu")
		self.cuaderno = ttk.Notebook(self.raiz2)

		#_____nombre variales_____________

		self.miid=StringVar()
		self.nombre=StringVar()
		self.autor=StringVar()
		self.editorial=StringVar()
		self.cantidad=StringVar()
		self.carrera=IntVar()
		self.numero_estante=StringVar()
		self.elemento_buscador=StringVar()


		#____seleccion RadioButton _
		#self.carrera.set(5)

		#______
		

		#_____FIN_____________


		self.pagina1=ttk.Frame(self.cuaderno)
		self.cuaderno.add(self.pagina1 , text="Guardar Libros")
		self.label1=Label(self.pagina1 , text="ingresar datos del libros:")
		self.label1.grid(row=2 , column=0 ,  padx=10 , pady=10)


		self.label2=Label(self.pagina1 , text="Nombre del Libro: ")
		self.label2.grid(row=3 , column=0 ,  padx=2 , pady=2)
		self.entrada2=Entry(self.pagina1 , textvariable=self.nombre)
		self.entrada2.grid(row=3, column=1 , padx=2 , pady=2)


		self.label3=Label(self.pagina1 , text="Autor del Libro: ")
		self.label3.grid(row=4 , column=0 ,  padx=2 , pady=2)
		self.entrada3=Entry(self.pagina1 , textvariable=self.autor)
		self.entrada3.grid(row=4, column=1 , padx=2 , pady=2)


		self.label4=Label(self.pagina1 , text="Editorial del Libro: ")
		self.label4.grid(row=5 , column=0 ,  padx=2 , pady=2)
		self.entrada4=Entry(self.pagina1 , textvariable=self.editorial)
		self.entrada4.grid(row=5, column=1 , padx=2 , pady=2)


		self.label5=Label(self.pagina1 , text="Cantidad Existente: ")
		self.label5.grid(row=6 , column=0 ,  padx=2 , pady=2)
		self.entrada5=Entry(self.pagina1 , textvariable=self.cantidad)
		self.entrada5.grid(row=6, column=1 , padx=2 , pady=2)



		self.radiobuton3=Radiobutton(self.pagina1 , text="Sistema" ,  variable=self.carrera , value=1)
		self.radiobuton3.place(x=150 , y=140)
		self.radiobuton4=Radiobutton(self.pagina1, text="telecon", variable=self.carrera , value=2)
		self.radiobuton4.place(x=230 , y=140)
		self.radiobuton5=Radiobutton(self.pagina1 , text="Literatura" , variable=self.carrera , value=3)
		self.radiobuton5.place(x=150 , y=170)
		self.radiobuton6=Radiobutton(self.pagina1 , text="Mecanica" , variable=self.carrera , value=4)
		self.radiobuton6.place(x=230 , y=170)
		self.radiobuton7=Radiobutton(self.pagina1, text="AGM" , variable=self.carrera , value=5)

		self.label_select=Label(self.pagina1 , text="Carrera:")
		self.label_select.place(x=30 , y=160)



		#self.label6=Label(self.pagina1 , text="Carrera: ")
		#self.label6.grid(row=7 , column=0 ,  padx=2 , pady=2)
		#self.entrada6=Entry(self.pagina1 , textvariable=self.carrera)
		#self.entrada6.grid(row=7, column=1 , padx=2 , pady=2)



		self.label7=Label(self.pagina1 , text="Numero de Estante : ")
		self.label7.place(x=30 , y=200)
		self.entrada7=Entry(self.pagina1 , textvariable=self.numero_estante)
		self.entrada7.place(x=160 , y=200)



		self.boton1=Button(self.pagina1 , text="Guardar" , command=self.creacion_de_libros)
		self.boton1.place(x=100 , y=250)

		self.boton_clean_space=Button(self.pagina1 , text="Limpiar" , command=self.creacion_de_libros)
		self.boton_clean_space.place(x=200 , y=250)

		self.miimagen2=PhotoImage(file="libros.png")

		
		self.label1=Label(self.pagina1,image=self.miimagen2)
		self.label1.place(x=580 , y=20)



		#__________________PAGINA DOS___________________




		self.pagina2=ttk.Frame(self.cuaderno , width=900,height=320)
		self.cuaderno.add(self.pagina2 , text="Lista de Libros")

		self.lista=ttk.Treeview(self.pagina2)

		self.lista["columns"]=("uno" , "dos" , "tres" , "cuatro" , "cinco" , "seis" )
		self.lista.column("#0" , width=30 , minwidth=50 )
		self.lista.column("uno" , width=270 , minwidth=270 )
		self.lista.column("dos" , width=150 , minwidth=150 )
		self.lista.column("tres" , width=250, minwidth=100 )
		self.lista.column("cuatro" , width=80 , minwidth=100)
		self.lista.column("cinco" , width=80 , minwidth=100 )
		self.lista.column("seis" , width=30 , minwidth=50 )

		self.lista.heading("#0" , text="ID"  , anchor=tk.W )
		self.lista.heading("uno" , text="Nombre libros"  , anchor=tk.W )
		self.lista.heading("dos" , text="Autor libros" , anchor=tk.W)
		self.lista.heading("tres" , text="Editorial" , anchor=tk.W)
		self.lista.heading("cuatro" , text="Cantidad", anchor=tk.W)
		self.lista.heading("cinco" , text="Carrera", anchor=tk.W)
		self.lista.heading("seis" , text=" Nro.Estante", anchor=tk.W)


		#self.folder1=self.lista.insert("" , tk.END  , text="Folder1")
		


		self.lista.pack(side=tk.TOP , fill=tk.X)

		self.label8=Label(self.pagina2 , text="ID : ")
		self.label8.pack()
		self.entrada8=Entry(self.pagina2,  textvariable=self.miid)
		self.entrada8.pack()


		self.label2=Label(self.pagina2 , text="Nombre del Libro: ")
		self.label2.pack()
		self.entrada2=Entry(self.pagina2 ,   textvariable=self.nombre)
		self.entrada2.pack()


		self.label3=Label(self.pagina2 , text="Autor del Libro: ")
		self.label3.pack()
		self.entrada3=Entry(self.pagina2 ,   textvariable=self.autor)
		self.entrada3.pack()


		self.label4=Label(self.pagina2 , text="Editorial del Libro: ")
		self.label4.pack()
		self.entrada4=Entry(self.pagina2 ,  textvariable=self.editorial)
		self.entrada4.pack()


		self.label5=Label(self.pagina2 , text="Cantidad Existente: ")
		self.label5.pack()
		self.entrada5=Entry(self.pagina2 ,   textvariable=self.cantidad)
		self.entrada5.pack()



		self.label6=Label(self.pagina2 , text="Carrera: ")
		self.label6.pack()
		self.entrada6=Entry(self.pagina2 ,  textvariable=self.carrera)
		self.entrada6.pack()


		self.label7=Label(self.pagina2 , text="Numero de Estante : ")
		self.label7.pack()
		self.entrada7=Entry(self.pagina2 ,  textvariable=self.numero_estante)
		self.entrada7.pack()


		self.boton1=Button(self.pagina2 , text="Editar"  , command=self.actuallizar_elemento )
		self.boton1.pack()

		self.boton3=Button(self.pagina2 , text="leer"  , command=self.leer )
		self.boton3.pack()

		self.boton2=Button(self.pagina2 , text="Actualizar Lista"  , command=self.actuallizar_datos_lista )
		self.boton2.pack()


		self.botonBuscador=Button(self.pagina2 , text="Buscador:" , command=self.buscadorLibros)
		self.botonBuscador.place(x=50 , y=300 )

		self.entrada15=Entry(self.pagina2  , textvariable=self.elemento_buscador)
		self.entrada15.place(x=150 , y=300 )





		self.pagina3=ttk.Frame(self.cuaderno)
		self.cuaderno.add(self.pagina3 , text="Prestamo de Libros")



		#__________________RADIOBUTTON__________________________

		self.seleccion=IntVar()
		#self.seleccion.set(2)


		self.radiobuton1=Radiobutton(self.pagina3 , text="Estudiante"  , variable=self.seleccion , value=1 )
		self.radiobuton1.place(x=50 , y=300 )

		self.radiobuton2= Radiobutton(self.pagina3 , text="Profesor" , variable=self.seleccion , value=2)
		self.radiobuton2.place(x=150 , y=300 )

		#______________________________________________________________

		#______________VAR NAME OF LOAN_____________________
		self.name_loan=StringVar()
		self.surname_loan=StringVar()
		self.career= StringVar()
		self.book_loan=IntVar()
		self.date=StringVar()
		self.number_fom= StringVar()
		self.email=StringVar()
		self.DNI=IntVar()

		#_____________________select career_______

		self.option_career=StringVar()

		self.name_career=("Sistema" ,"Telecon" , "Literatura" , "Mecanica")


		#________________________



		self.label9=Label(self.pagina3 , text="nombre: ")
		self.label9.place(x=50 , y=350 )
		self.entrada9=Entry(self.pagina3  , textvariable=self.name_loan)
		self.entrada9.place(x=130 , y=350 )


		self.label10=Label(self.pagina3 , text="Apellido:")
		self.label10.place(x=50 , y=400 )
		self.entrada10=Entry(self.pagina3 , textvariable=self.surname_loan)
		self.entrada10.place(x=130 , y=400 )


		


		self.label11=Label(self.pagina3 , text="Carrera: ")
		self.label11.place(x=50 , y=450 )
		self.combobox1=ttk.Combobox(self.pagina3 , width=10 , textvariable=self.option_career , values=self.name_career)
		self.combobox1.place(x=130 , y=450 )

		self.label12=Label(self.pagina3 , text="Libro solicitado: ")
		self.label12.place(x=30 , y=500 )
		self.entrada12=Button(self.pagina3  , width="20" ,  text="Select", command=self.new_window)
		self.entrada12.place(x=130 , y=500 )


		self.label13=Label(self.pagina3 , text="cedula")
		self.label13.place(x=50 , y=550 )
		self.entrada13=Entry(self.pagina3  , textvariable=self.DNI)
		self.entrada13.place(x=130 , y=550 )

		self.label_number_fom=Label(self.pagina3 , text="Telefono")
		self.label_number_fom.place(x=275 , y=350)
		self.entry_number_fom=Entry(self.pagina3 ,textvariable= self.number_fom)
		self.entry_number_fom.place(x=330 , y=350)

		self.label_email=Label(self.pagina3 , text="Email")
		self.label_email.place(x=275 , y=400 )
		self.entry_email=Entry(self.pagina3 , textvariable= self.email)
		self.entry_email.place(x=330 , y=400)





		self.boton4= Button(self.pagina3 , text="Guardar"  , command=self.save_date_of_loan)
		self.boton4.place(x=300 , y=550)

		self.boton5= Button(self.pagina3 , text="Limpiar"   , command=self.clean_date)
		self.boton5.place(x=300 , y=500)






		self.lista2=ttk.Treeview(self.pagina3)

		self.lista2["columns"]=("uno" , "dos" , "tres" , "cuatro" , "cinco" , "seis" )
		self.lista2.column("#0" , width=30 , minwidth=50 )
		self.lista2.column("uno" , width=270 , minwidth=270 )
		self.lista2.column("dos" , width=150 , minwidth=150 )
		self.lista2.column("tres" , width=250, minwidth=100 )
		self.lista2.column("cuatro" , width=80 , minwidth=100)
		self.lista2.column("cinco" , width=80 , minwidth=100 )
		self.lista2.column("seis" , width=30 , minwidth=50 )

		self.lista2.heading("#0" , text="ID"  , anchor=tk.W )
		self.lista2.heading("uno" , text="Nombre"  , anchor=tk.W )
		self.lista2.heading("dos" , text="Apellido" , anchor=tk.W)
		self.lista2.heading("tres" , text="Genero" , anchor=tk.W)
		self.lista2.heading("cuatro" , text="Carrera", anchor=tk.W)
		self.lista2.heading("cinco" , text="Nombre Libro", anchor=tk.W)
		self.lista2.heading("seis" , text="Fecha", anchor=tk.W)

		self.lista2.pack(side=tk.TOP , fill=tk.X)








		self.cuaderno.grid(column=0, row=0)

		self.raiz2.mainloop()
		print("este es el dato de la funcion" , self.book_loan)

	def new_window(self):



		self.my_connect= sqlite3.connect("BIBLIOTECA")

		self.my_cursor=self.my_connect.cursor()

		self.my_cursor.execute("SELECT ID , NOMBRE_LIBROS FROM LIBROS ")

		self.list_date_id_book=self.my_cursor.fetchall()
		print(self.list_date_id_book)

		self.raiz3=Toplevel(self.raiz2)
		self.raiz3.title("Seleccion de libros ")


		self.listBox1=Listbox(self.raiz3)
		self.listBox1.grid(row=3, column=3)

		for x in range(len(self.list_date_id_book)):

			self.listBox1.insert(self.list_date_id_book[x][0] , self.list_date_id_book[x][1])
		

		self.button_select_objeto=Button(self.raiz3 , text="Aceptar"  , command=self.button_select_book)

		self.button_select_objeto.grid(row=1, column=1)


		self.raiz3.mainloop()


	def button_select_book(self):


		if len(self.listBox1.curselection())!=0:

			print(self.listBox1.get(self.listBox1.curselection()[0]))

			for date in range(len(self.list_date_id_book)):

				if self.list_date_id_book[date][1]==self.listBox1.get(self.listBox1.curselection()[0]):

					self.book_loan =self.list_date_id_book[date][0]


			self.raiz3.destroy()

					





	def clean_date(self):
	

		self.name_loan.set("")
		self.surname_loan.set("")
		self.career.set("")
		self.book_loan=0
		self.date.set("")
		self.number_fom.set("")
		self.email.set("")
		self.DNI.set("")
		self.option_career.set("")


	def combobox_analisate(self):

		self.option_carrer1=0

		if self.option_career.get()== "Sistema":

			self.option_carrer1=1
			return self.option_carrer1

		else:

			if self.option_career.get()=="Telecon":
				self.option_carrer1=2
				return self.option_carrer1

			else:

				if self.option_career.get()=="Literatura":
					self.option_carrer1=3
					return self.option_carrer1

				else:

					self.option_carrer1=4
					return self.option_carrer1

				






	def save_date_of_loan(self):


		self.date_recive=self.combobox_analisate()
		print(self.date_recive)

		self.my_connect= sqlite3.connect("BIBLIOTECA")

		self.my_cursor=self.my_connect.cursor()
		
		if self.seleccion.get()==1:
			#print("estoy viendo si el valor del libros tiene algun dato " , self.)

			

			list_save_date_estudens_or_prfesor=[
				(self.name_loan.get() , self.surname_loan.get() ,self.DNI.get()  , self.number_fom.get() , self.email.get() , self.date_recive  , self.book_loan)

			]

			self.my_cursor.executemany("INSERT INTO alumnos VALUES (NULL , ?,?,?,?,?,?,? ) " , list_save_date_estudens_or_prfesor)

			self.my_connect.commit()
			self.my_connect.close()

			self.my_connect= sqlite3.connect("BIBLIOTECA")

			self.my_cursor=self.my_connect.cursor()

			self.my_cursor.execute("SELECT id , ID_LIBROS FROM ALUMNOS")


			self.var_date_send_to_table_loan=self.my_cursor.fetchall()

			list_date_send_table_loan=[

				(self.var_date_send_to_table_loan[-1][0] ,self.var_date_send_to_table_loan[-1][1])


			]

			self.my_cursor.executemany("INSERT INTO ALUMMNO_PRESTAMO VALUES (NULL, ?,?)" , list_date_send_table_loan)

			self.my_connect.commit()

			
		else:


			

			list_save_date_estudens_or_prfesor=[
				(self.name_loan.get() , self.surname_loan.get() ,self.DNI.get()  , self.number_fom.get() , self.email.get() , self.date_recive , self.book_loan)

			]

			self.my_cursor.executemany("INSERT INTO PROFESORES VALUES (NULL , ?,?,?,?,?,?,? ) " , list_save_date_estudens_or_prfesor)

			self.my_connect.commit()
			self.my_connect.close()


			self.my_connect= sqlite3.connect("BIBLIOTECA")

			self.my_cursor=self.my_connect.cursor()

			self.my_cursor.execute("SELECT id , ID_LIBROS FROM ALUMNOS")


			self.var_date_send_to_table_loan=self.my_cursor.fetchall()

			list_date_send_table_loan=[

				(self.var_date_send_to_table_loan[-1][0]  ,self.var_date_send_to_table_loan[-1][1])


			]

			self.my_cursor.executemany("INSERT INTO profesor_prestamo VALUES (NULL, ?,?)" , list_date_send_table_loan)

			self.my_connect.commit()
			#pritn("hecho")



			

	def creacion_de_libros(self):
		str(self.carrera)
		#int(self.numero_estante)

		

		self.miconexion=sqlite3.connect("BIBLIOTECA")

		self.mi_cursor=self.miconexion.cursor()
		list_save=[

			(self.nombre.get(), self.autor.get() , self.editorial.get() , self.cantidad.get() , self.carrera.get() , self.numero_estante.get()  )

		]

		self.mi_cursor.executemany("INSERT INTO LIBROS VALUES(NULL,?,?,?,?,?,?)" , list_save)

		

		self.miconexion.commit()

		messagebox.showinfo("BBDD" , "Regstr guardado")	

		self.nombre.set("")

		self.autor.set("")

		self.editorial.set("")

		self.cantidad.set("")

		self.carrera.set("")

		self.numero_estante.set("")

	def actuallizar_datos_lista(self):

		record =self.lista.get_children()

		for elemento in record:

			self.lista.delete(elemento)

		self.miconexion=sqlite3.connect("BIBLIOTECA")

		self.mi_cursor=self.miconexion.cursor()

		self.mi_cursor.execute("SELECT * FROM LIBROS")

		lista=self.mi_cursor.fetchall()
		
		for x in range(len(lista)):

			self.lista.insert("" , 0 ,text=lista[x][0] , values=(lista[x][1] ,lista[x][2] ,lista[x][3] , lista[x][4], lista[x][5] , lista[x][6]  ))
		


	def leer(self):

		self.miconexion=sqlite3.connect("BIBLIOTECA")

		self.mi_cursor=self.miconexion.cursor()

		try:

			self.mi_cursor.execute("SELECT  * FROM LIBROS WHERE ID=" + self.miid.get())

			lista=self.mi_cursor.fetchall()
		

			for elemento in lista:

			#self.miid.set(elemento[0])

				self.nombre.set(elemento[1])

				self.autor.set(elemento[2])

				self.editorial.set(elemento[3])

				self.cantidad.set(elemento[4])

				self.carrera.set(elemento[5])

				self.numero_estante.set(elemento[6])

		except:	

			messagebox.showwarning("BBDD" , "DEBE SELECCIONAR ID DEL LIBROS QUE DESEA ACTUALIZAR")	
	
	def actuallizar_elemento(self):
		


		self.miconexion = sqlite3.connect("BIBLIOTECA")


		self.mi_cursor=self.miconexion.cursor()

		try:


			self.mi_cursor.execute("SELECT * FROM LIBROS WHERE ID=" + self.miid.get())
			lista_sin_editar=self.mi_cursor.fetchall()
			self.verificacion()
			self.mi_cursor.execute("UPDATE LIBROS SET NOMBRE_LIBROS='" + self.nombre.get() +
			"',  Autor_del_Libro='" + self.autor.get()+
			"' , Editorial_del_Libro='" + self.editorial.get()+
			"' , Cantidad_Existente='" + self.cantidad.get()+
			"' , Carrera='" + self.carrera.get() +
			"' , Numero_de_Estante='" + self.numero_estante.get()+
			"'  WHERE ID=" + self.miid.get() )


			nombre1=self.nombre.get()
			autor1=self.autor.get()
			editorial1=self.editorial.get()
			cantidad1=self.cantidad.get()
			carrera1=self.carrera.get()
			numero_estante1=self.numero_estante.get()
			#print(lista_sin_editar)
			#print("estoy en la parte que confirma que se actualiza")
			#print(self.nombre.get())

		except:

			messagebox.showwarning("BBDD" , "DEBE SELECCIONAR ID DEL LIBROS QUE DESEA ACTUALIZAR")



		if self.nombre.get() == "" or self.autor.get()=="" or self.editorial.get() == "" or self.cantidad.get()==""	 or self.carrera.get()=="" or self.numero_estante.get()=="":

			messagebox.showwarning("BBDD" ," !ERRON¡ Algun Campo Se Encuentra Vacio")

		else:
				#self.verificacion()	

			if self.lista_verificacion[0] == lista_sin_editar[0][1]  and self.lista_verificacion[1] == lista_sin_editar[0][2] and self.lista_verificacion[2] == lista_sin_editar[0][3] and self.lista_verificacion[3] == lista_sin_editar[0][4] and self.lista_verificacion[4] == lista_sin_editar[0][5] and self.lista_verificacion[5] == lista_sin_editar[0][6]:
				
				messagebox.showwarning("BBDD" , "No ha ralizado cambios , Desea Seguir")
				
				self.miid.set("")

				self.nombre.set("")

				self.autor.set("")

				self.editorial.set("")

				self.cantidad.set("")

				self.carrera.set("")

				self.numero_estante.set("")
				print(" no actualice")
				print(self.lista_verificacion)
				print(lista_sin_editar)

				print()
				print()

				"""print(self.lista_verificacion[0] ,lista_sin_editar[0][1] )
				print(self.lista_verificacion[1] ,lista_sin_editar[0][2] )
				print(self.lista_verificacion[2] ,lista_sin_editar[0][3] )
				print(self.lista_verificacion[3] ,lista_sin_editar[0][4] )	
				"""

			else:
				
				print("actualice")
				self.miconexion.commit()
				messagebox.showinfo("BBDD" ,"Registro actualizado con exito" )
				

				self. miid.set("")

				self.nombre.set("")

				self.autor.set("")

				self.editorial.set("")

				self.cantidad.set("")

				self.carrera.set("")

				self.numero_estante.set("")
				#print(self.lista_verificacion)
				#print(lista_sin_editar)
				"""print(self.lista_verificacion[0] )
				print(lista_sin_editar[0][1])
				print(self.lista_verificacion[1] )
				print(lista_sin_editar[0][2])
				print(self.lista_verificacion[2] )
				print(lista_sin_editar[0][3])
				print(self.lista_verificacion[3] )
				print(lista_sin_editar[0][4])
				print(self.lista_verificacion[4] )
				print(lista_sin_editar[0][5])
				print(self.lista_verificacion[5] )
				prit(lista_sin_editar[0][6])
				"""


		



	def verificacion(self):

		self.lista_verificacion=[]
		self.lista_verificacion.append(self.nombre.get())
		self.lista_verificacion.append(self.autor.get())
		self.lista_verificacion.append(self.editorial.get())
		self.lista_verificacion.append(int(self.cantidad.get()))
		self.lista_verificacion.append(self.carrera.get())
		self.lista_verificacion.append(int(self.numero_estante.get()))


	def buscadorLibros(self):
		
		qw=self.elemento_buscador.get()
		self.miconexion=sqlite3.connect("BIBLIOTECA")
		self.mi_cursor=self.miconexion.cursor()
		
		

		self.mi_cursor.execute("SELECT * FROM LIBROS WHERE NOMBRE_LIBROS LIKE  '" + self.elemento_buscador.get() + "%' ")

		lista=self.mi_cursor.fetchall()
		print(lista)

		record =self.lista.get_children()

		for elemento in record:

			self.lista.delete(elemento)

		

		
		for x in range(len(lista)):

			self.lista.insert("" , 0 ,text=lista[x][0] , values=(lista[x][1] ,lista[x][2] ,lista[x][3] , lista[x][4], lista[x][5] , lista[x][6]  ))
		
		


	





		



#ventana_interna1=ventana_interna()

#ventana_interna1.creacion_de_ventana()


#____________________________CRUD INTERNO _______________






#____________________________loggin_______________




class loggin():

	def __init__(self):
		
		self.miconexion=sqlite3.connect("BIBLIOTECA")
		self.mi_cursor=self.miconexion.cursor()

		self.raiz=Tk()
		self.raiz.title("LOGIN")
		self.raiz.resizable(0,0)
		self.raiz.iconbitmap("imagen.ico")
		self.raiz.geometry("950x650")

		self.nombre=StringVar()
		self.contrasena=StringVar()

		self.miimagen=PhotoImage(file="loginimagen.png")

		
		self.label1=Label(self.raiz,image=self.miimagen)
		self.label1.pack()

		self.name=Label(self.raiz , text="Nombre" )
		self.name.place(x=380 , y=300)

		self.name_entry=Entry(self.raiz , textvariable=self.nombre)
		self.name_entry.place(x=450 , y=300)

		self.password=Label(self.raiz , text="Password" ,  padx=2 , pady=2 )
		self.password.place(x=380 , y=330)

		

		self.password_Entry=Entry(self.raiz , textvariable=self.contrasena)
		self.password_Entry.place(x=450 , y=330)
		self.password_Entry.config(show="*")

		self.boton=Button(self.raiz , text="INGRESAR" , command=self.comprobar)
		self.boton.place(x=450 , y=360)
		

		self.label15=Label(self.raiz , text="Ingresa tus Datos: ")
		self.label15.place(x=420 , y=270)
		self.raiz.mainloop()
	

	def comprobar(self):

		nombre1=self.nombre.get()
		password1=self.contrasena.get()
		#print(nombre1)
		#print(password1)

		self.mi_cursor.execute("SELECT NOMBRE, PASSWORD FROM ADMINISTRADOR ")

		lista=self.mi_cursor.fetchall()
		
		#print(lista) 


		if nombre1  == lista[0][0]  and  password1 == lista[0][1]:
			self.raiz.destroy()
			self.creacion_de_ventana1=ventana_interna()
			
			print("aqui	")
			#self.ventana_interna1.creacion_de_ventana()
			#self.label1.config(text="Correcto")
			
			
		else:

			if ((nombre1  in lista[0][0])  and  not(password1 in lista[0][1])):

				self.contrasena.set("")
				self.label1.config( bg="red")

				self.label15.config(text="contraseña Equivocada" , bg="red")

			else:

				if nombre1== "" or password1=="":
					self.label1.config( bg="red")

					self.label15.config(text="Algun Campo Esta Vacio" , bg="red")


				else:
					self.label1.config( bg="red")	

					self.label15.config(text="No Se Encuentra  Registrado" , bg="red")

					self.contrasena.set("")	

					self.nombre.set("")
				 




		



login1=loggin()

#____________________________loggin_______________





