import wikipedia as wiki

#print(wiki.search('Shah Rukh'))

wiki.set_lang('en')
print(wiki.suggest('movi'))

print(wiki.summary('Movies'))