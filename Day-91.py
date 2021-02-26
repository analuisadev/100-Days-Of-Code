text = """\
Ouviram do Ipiranga as margens plácidas
De um povo heróico o brado retumbante,
E o sol da Liberdade, em raios fúlgidos,
Brilhou no céu da Pátria nesse instante.
Se o penhor dessa igualdade
Conseguimos conquistar com braço forte,
Em teu seio, ó Liberdade,
Desafia o nosso peito a própria morte!
Ó Pátria amada,
Idolatrada,
Salve! Salve!
Brasil, um sonho intenso, um raio vívido,
De amor e de esperança à terra desce,
Se em teu formoso céu, risonho e límpido,
A imagem do Cruzeiro resplandece.
Gigante pela própria natureza,
És belo, és forte, impávido colosso,
E o teu futuro espelha essa grandeza.
Terra adorada
Entre outras mil
És tu, Brasil,
Ó Pátria amada!
Dos filhos deste solo
És mãe gentil,
Pátria amada,
Brasil!
Deitado eternamente em berço esplêndido,
Ao som do mar e à luz do céu profundo,
Fulguras, ó Brasil, florão da América,
Iluminado ao sol do Novo Mundo!
Do que a terra mais garrida
Teus risonhos, lindos campos têm mais flores,
"Nossos bosques têm mais vida",
"Nossa vida" no teu seio "mais amores".
Ó Pátria amada,
Idolatrada,
Salve! Salve!
Brasil, de amor eterno seja símbolo
O lábaro que ostentas estrelado,
E diga o verde-louro dessa flâmula
– Paz no futuro e glória no passado.
Mas se ergues da justiça a clava forte,
Verás que um filho teu não foge à luta,
Nem teme, quem te adora, a própria morte.
Terra adorada
Entre outras mil
És tu, Brasil,
Ó Pátria amada!
Dos filhos deste solo
És mãe gentil,
Pátria amada,
Brasil!
"""
text = text.lower() #deixa as letras em maiúsculo
#Remove espaço, linha e símbolos de pontuações
text = text.replace(" ","")
text = text.replace("\n","")
text = text.replace(".","")
text = text.replace("!","")
text = text.replace("?","")
text = text.replace(",","")
text = text.replace(";","")
#remove acento e cedilha
text = text.replace("á","a")
text = text.replace("à","a")
text = text.replace("ã","a")
text = text.replace("é","a")
text = text.replace("ê","e")
text = text.replace("í","i")
text = text.replace("ó","o")
text = text.replace("ô","o")
text = text.replace("ú","u")
text = text.replace("ç","c")
vowels = 0
consonantS = 0
print('Contador de Letras - Vogais e Consoantes')
for caracter in text:
    if caracter in 'aeiou':
        vowels = vowels + 1
    else:
        consonantS = consonantS + 1

print('Vogais: %d' % vowels)
print('Consoantes: %d' % text)
print('Total de letras: %d - %d' % (len(text), (vowels+consonantS)))