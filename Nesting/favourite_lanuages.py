favorite_languages = {
    'Itumeleng': ['python', 'c'],
    'katlego': ['ruby'],
    'thabo': ['ruby', 'go'],
    'pheladi': ['python', 'haskel'],
}

for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())