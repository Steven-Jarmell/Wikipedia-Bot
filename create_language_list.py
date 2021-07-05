import wikipedia

language_abbreviations_file = open('Language List', 'w', encoding='utf-8')

for language in wikipedia.languages():

    abbreviations = language + " " + wikipedia.languages()[language]
    language_abbreviations_file.write(abbreviations + '\n')

language_abbreviations_file.close()