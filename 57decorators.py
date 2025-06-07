# (08:07:33)

# decorators: fuction that extends behaviour of another function without modifying base function

def add_sprinkles(funt):
    def wrapper(*args , **kwargs):
        print("You add sprinkles")
        funt(*args , **kwargs)
    return wrapper

def add_fudge(funt):
    def wrapper(*args , **kwargs):
        print("You add fudge")
        funt(*args , **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} Icecream")

get_ice_cream("vanilla")