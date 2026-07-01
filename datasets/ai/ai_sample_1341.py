import pegjs

if __name__ == "__main__":
    parser = pegjs.generate('''
        Expression   
            = Sequence ( Operator Sequence )* 
        Sequence       
            = "(" Expression ")" 
            / Number 
        Operator
            = Add / Subtract / Multiply / Divide 
        Add
            = "+" 
        Subtract
            = "-" 
        Multiply
            = "*" 
        Divide
            = "/" 
        Number
            = [0-9]+
    ''') 
    result = parser.parse('2 * (3 + 4)')
    print(result)