print("module_b: top level")

def get_a():
    import module_a
    return module_a.A()

class B:
    def greet(self):
        a = get_a()
        return f"B: {a.greet()}"


if __name__ == "__main__":
    import module_a

if __name__ == "module_b":
    print("")