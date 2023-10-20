cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 11248839,
        'fact': 'old name is batavia',
    },

    'bandung': {
        'country': 'indonesia',
        'population': 2674000,
        'fact': 'so many beutiful places',
    },

    'cirebon': {
        'country': 'indonesia',
        'population': 332000,
        'fact': 'so many seafood'
    }
}

for city, info in cities.items():
    print(f"here information about {city}")
    nation = f"{info['country']}"
    people = f"{info['population']}"
    fun_fact = f"{info['fact']}"
    
    print(f"\t{nation.title()}")
    print(f"\t{people}")
    print(f"\t{fun_fact.title()}")