import random

# Listes de mots pour le générateur de poèmes
sujets = ["Le chat", "L'enfant", "La lune", "Un oiseau", "Un poisson"]
verbes = ["chante", "danse", "vole", "nage", "rêve"]
adjectifs = ["bleu", "silencieux", "joyeux", "triste", "mystérieux"]
compléments = ["dans la nuit", "sur la mer", "au bord du lac", "dans le jardin", "sous les étoiles"]
adverbes = ["doucement", "rapidement", "calmement", "bruyamment", "silencieusement"]
prépositions = ["avec", "sans", "pour", "contre", "sur"]
noms = ["l'amour", "la tristesse", "le bonheur", "le vent", "la pluie"]

# Structures de vers possibles
structures = [
    "{sujet} {verbe} {adjectif} {complément}.",
    "{sujet} {verbe} {adverbe} {complément}.",
    "{sujet} {verbe} {préposition} {nom}.",
    "{adverbe}, {sujet} {verbe} {complément}.",
    "{sujet}, {adjectif}, {verbe} {complément}."
]

def generer_vers():
    structure = random.choice(structures)
    vers = structure.format(
        sujet=random.choice(sujets),
        verbe=random.choice(verbes),
        adjectif=random.choice(adjectifs),
        complément=random.choice(compléments),
        adverbe=random.choice(adverbes),
        préposition=random.choice(prépositions),
        nom=random.choice(noms)
    )
    return vers

def generer_poeme(nombre_de_vers=4):
    poeme = [generer_vers() for _ in range(nombre_de_vers)]
    return "\n".join(poeme)

# Générer un poème de 4 vers
print(generer_poeme())
