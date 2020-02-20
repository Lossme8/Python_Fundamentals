favourite_languages ={
    'thabo': 'python',
    'katlego': 'c',
    'pheladi': 'ruby',
    'itumeleng': 'python',

    }
for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " +
        language.title() + ".")

print("\nThe list of names of people who enjoys various languages")
for name in favourite_languages:
    print(name.title())