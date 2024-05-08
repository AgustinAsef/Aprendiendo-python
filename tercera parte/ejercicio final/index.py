import pandas as pd
def print_space():
  print('------------------------------------------------------')

def init_program():
  print_space()
  df = use_new_file()
  do_now = input("""Que te gustaria hacer con este archivo? (ingresa el numero de la opcion)
    1: obtener puntaje aproximado
    2: obtener cantidad de operaciones
    Opcion: """)
  
  print_space()
  
  if do_now == '1':
    get_score(df)
  if do_now == '2':
    get_operations(df)

def use_new_file():
  new_file = input('Cual es el nombre del archivo que te gustaria importar?: ')
  try:
    df = pd.read_csv(f"C:\\Users\\agust\Desktop\\avtividades\\python\\ejercicio final\\archivos\\archivo_personal\\{new_file}.csv")
    df = df[["POS", "Vendedor", "Legajo", "Activado", "Id", "Op_Tipo", "SS", "Plan"]]
    return df
  except:
    print('No se encontro un archivo con ese nombre, intentalo nuevamente')
    init_program()

def get_score(df):
  score_repro_counter = df[(df["Op_Tipo"] == 'REPRO')].shape[0] * 34
  score_cater_counter = df[df["Op_Tipo"] == 'CATER'].shape[0] * 134
  score_altan_counter = df[df["Op_Tipo"] == 'ALTAN'].shape[0] * 200
  score_porta_counter = df[df["Op_Tipo"] == 'PORTA'].shape[0] * 64
  score_bam_counter = df[df["Op_Tipo"] == 'BAM'].shape[0] * 70
  total_score = score_repro_counter + score_cater_counter + score_altan_counter + score_porta_counter + score_bam_counter
  print(f"tu puntaje aproximado es de {total_score}")  
  
def get_operations(df):
  repro_counter = df[df["Op_Tipo"] == 'REPRO'].shape[0]
  cater_counter = df[df["Op_Tipo"] == 'CATER'].shape[0]
  altan_counter = df[df["Op_Tipo"] == 'ALTAN'].shape[0]
  porta_counter = df[df["Op_Tipo"] == 'PORTA'].shape[0]
  bam_counter = df[df["Op_Tipo"] == 'BAM'].shape[0]

  print(f"""Has realizado:
        {repro_counter} lineas nuevas,
        {cater_counter} caters,
        {altan_counter} altas con equipo
        {porta_counter} portabilidades
        {bam_counter} fibras""")
  print_space()
  
  see_detail = input("""Te gsutaria ver el detalle?
    1: Si
    2: No
    Opcion: """)
  
  if see_detail == '1':
    get_operations_detail(df)
  if see_detail == '2':
    init_program()
  else:
    get_operations(df)
  
def get_operations_detail(df):
  print_space()
  operation = input("""Que operacion te gustaria ver? (ingresa el numero de la opcion)
    1: REPRO
    2: CATER
    3: ALTAN
    4: PORTA
    5: BAM
    Opcion: """)
  
  print_space()
  if operation == "1": print(df[df["Op_Tipo"] == 'REPRO'])
  if operation == "2": print(df[df["Op_Tipo"] == 'CATER'])
  if operation == "3": print(df[df["Op_Tipo"] == 'ALTAN'])
  if operation == "4": print(df[df["Op_Tipo"] == 'PORTA'])
  if operation == "5": print(df[df["Op_Tipo"] == 'BAM'])
  
init_program()