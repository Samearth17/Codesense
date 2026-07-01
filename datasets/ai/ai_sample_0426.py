class Strategy:
    """The Strategy Pattern class"""

    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(self):
        """The default method that prints 'Hello world!'"""
        print("Hello world!")

# Replace by other strategies
def execute_replacement1():
    print("Hola mundo!")

def execute_replacement2():
    print("Mere saath kaam kar!")

# Instantiate the strategy
s1 = Strategy()
# Execute the strategy
s1.execute()

# Create replacement strategy 1
s2 = Strategy(execute_replacement1)
# Execute the strategy
s2.execute()

# Create replacement strategy 2
s3 = Strategy(execute_replacement2)
# Execute the strategy
s3.execute()