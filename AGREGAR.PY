def agregar(ruta:int, datos:dict):
  archivoExcel=load_workbook(ruta)

  hojaDatos=archivoExcel['Datos del crud']
  hojaDatos=hojaDatos['A2':'F'+str(hojaDatos.max_row+1)]
  hoja=archivoExcel.active

  titulo=2
  descripcion=3
  estado=4
  fechaInicio=5
  fechaFinalizado=6
  for i in hojaDatos:
    if not(isinstance(i[0].value,int)):
      identificador=i[0].row
      hoja.cell(row=identificador,column=1).value=identificador-1
      hoja.cell(row=identificador,column=titulo).value=datos['titulo']
      hoja.cell(row=identificador,column=descripcion).value=datos['descripcion']
      hoja.cell(row=identificador,column=estado).value=datos['estado']
      hoja.cell(row=identificador,column=fechaInicio).value=datos['fecha inicio']
      hoja.cell(row=identificador,column=fechaFinalizado).value=datos['fecha finalizacion']
      break
  archivoExcel.save(ruta)
  return




  elif accion==3:
    datosActualizados={'titulo':'','descripcion':'','estado':'','fecha inicio':'','fecha finalizacion':''}
    print('** Crear nueva Tarea **\n')
    print('** Titulo **\n')
    datosActualizados['titulo']=input('Indique el titulo de la tarea: ')
    print('\n** descripcion **')
    datosActualizados['descripcion']=input('Ingrese la descripcion de la tarea: ')
    print()
    datosActualizados['estado']='En espera'
    now = datetime.now()
    datosActualizados['fecha inicio']=str(now.day) +'/' + str(now.month)+'/'+str(now.year)
    agregar(rut,datosActualizados)