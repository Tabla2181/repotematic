import os
import ProxyCloud

BOT_TOKEN = '5277008415:AAFVOIjwftp59g3XODLR9olnnzadsMdkxMo' #Aqui va el token del bot
API_ID =  15558101 #Tu api id de telegram
API_HASH = 'c2cbb2f07c44fe466076fbe65e3c00cc' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','Elnietodecacha').split(';')


  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['Elnietodecacha'] = 0

