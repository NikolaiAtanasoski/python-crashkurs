#list
pokemon_list = ["pikachu", "glumanda", "bisaflor", "dragoran", "abra", "karnimani", "gengar"]

#tuple
dimensions = (200, 50)

trainer_0 = {"name": "pi", "pokemon" : "dragoran"}
trainer_1 = {"name": "nikolai", "pokemon" : "karnimani"}

favourite_languages = {
    "mo" : "python",
    "dzeno" : "C",
    "pauli" : "python",
    "phil" : "javascript",
}

trainers_pokemons = {"ash":"pikachu", "brock":"georok", "misti":"starmi"}

trainers = ["Nikolai","ash", "misti","Dzeno","pi"]

for trainer in trainers:
    if trainer in trainers_pokemons.keys():
        print(f"Good job training your pokemon {trainers_pokemons.get(trainer)}, {trainer}")
    else:
        print(f"{trainer} you need to find a pokemon first!")



