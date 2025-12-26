print("module_a: top level")

def get_b():
    import module_b
    return module_b.B()

class A:
    def greet(self):
        b = get_b()
        return f"A: {b.greet()}"
