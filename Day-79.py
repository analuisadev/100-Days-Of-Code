#importação da biblioteca time 
import time 
#variavel que vai armazenar o dia, data, hora e ano atuais
localtime = time.asctime( time.localtime(time.time()) ) 
print("Local current time :", localtime)
