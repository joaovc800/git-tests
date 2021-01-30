import subprocess

class p_loader():

    def __init__(self, arg):
        self.arg = arg
       
    def check_in(self):
        return self.arg.stdout

    def square(self, x):
        """Squares X."""
        return x * x
    
    if __name__ == '__main__':
        import doctest
        doctest.testmod()

