import wikipedia
print(wikipedia.resumo("Wikipedia"))

wikipedia.search("Barack")

ny = wikipedia.págia("Nova York")
ny.title
ny.url
ny.contents
ny.links[0]
wikipedia.set_lang("fr")
wikipedia.resumo("Facebook", frases = 1)