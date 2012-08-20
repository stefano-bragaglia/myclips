'''
Created on 05/aug/2012

@author: Francesco Capozzo
'''
import myclips.parser.Types as types
from myclips.functions.Function import Function
from myclips.FunctionsManager import FunctionDefinition, Constraint_MinArgsLength,\
    Constraint_ArgType

class GreaterThan(Function):
    '''
    The > function returns the symbol TRUE if for all its arguments, argument n- 1 is greater than argument n, 
    otherwise it returns the symbol FALSE. 
    Note that > compares only numeric values and will convert integers to floats when necessary for comparison.
    @see: http://www.comp.rgu.ac.uk/staff/smc/teaching/clips/vol1/vol1-12.1.html#Heading210
    '''
    def __init__(self, *args, **kwargs):
        Function.__init__(self, *args, **kwargs)
        
    def do(self, theEnv, theValue, *args, **kargs):
        """
        handler of the GreaterThan function
        """
        
        # resolve to the python value
        theValue = self.resolve(theEnv, 
                                self.semplify(theEnv, theValue, types.Number, ("1", 'number')))

        for theArg in args:
            # resolve the real value
            # before comparison
            # resolve to the python value
            theArg = self.resolve(theEnv, 
                                    self.semplify(theEnv, theArg, types.Number, ("ALL", 'number')))
            
            
            # compare the python type (so 3. == 3)
            if theValue <= theArg:
                return types.Symbol("FALSE")
            
        return types.Symbol("TRUE")


GreaterThan.DEFINITION = FunctionDefinition("?SYSTEM?", ">", GreaterThan(), types.Symbol, GreaterThan.do ,
            [
                Constraint_MinArgsLength(2),
                Constraint_ArgType(types.Number)
            ],forward=False)
