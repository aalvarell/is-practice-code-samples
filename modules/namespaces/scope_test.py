x = 'global'

def f():
    x = 'enclosing'

    def g(): # función definida dentro de la función f
        x = 'local'
        print(x)

    g() # f llama a g
    print(x)

f()

print(x)