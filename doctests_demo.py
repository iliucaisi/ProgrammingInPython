class Calculator:
    '''
    >>> calc=Calculator()
    >>> calc.add(1, 2)
    3
    '''
    def add(self, a, b):
        '''
        >>> calc=Calculator()
        >>> calc.add(3, 2)
        5
        '''
 
        print "add"
        return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
