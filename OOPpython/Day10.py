
class Vactor(object):
    
    def __init__(self, *args):

        if len(args) == 0:
            self._x, self._y = 0, 0
        else :
            self._x, self._y =  args
    
    def __repr__(self):
        return 'Vactor(%r, )'