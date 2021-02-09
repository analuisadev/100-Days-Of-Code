#importação da urllib para acessar o link do perfil @eidev.oficial
import urllib
import urllib.request
#Usando o Try para acessar o perfil 
try: 
    site = urllib.request.urlopen('https://www.instagram.com/eidev.oficial/')
#Caso o link do perfil não esteja disponível, aparecerá essa mensagem.
except urllib.error.URLError:
    print ('Tivemos um problema para acessar o site :(')
#Se não der erro, aparecerá essa mensagem
else: 
    print ('Site acessado com sucesso!')
#Comando para exibir os códigos em HTML do perfil/site
    #print (site.read())
