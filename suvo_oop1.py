# public
class abc():
    var=10
    def display(self):
        print("ok")
        print(self)

# private
class private():
    _var=10
    def _display(self):
        _var=30
        return _var
    def display(self):
        print(f"the value of private variable is {private._display(self)}")
        

private_obj=private()
private_obj.display()
