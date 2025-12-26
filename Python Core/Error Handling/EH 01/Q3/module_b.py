print("module_b: top level")

def get_a():
    import module_a
    return module_a.A()

class B:
    def greet(self):
        a = get_a()
        return f"B: {a.greet()}"
