from decouple import config

API_POKEMON = config("POKEMON")
API_KEY = config("KEY")
DEBUG_MODE = config("DEBUG_MODE", default=False, cast=bool)

print(API_POKEMON)
print(API_KEY)
