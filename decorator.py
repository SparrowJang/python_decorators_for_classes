# -*- coding: utf-8 -*-

class Canvas( object ):
    """
    Define a sample canvas for terminal.
    """
 
    def __init__( self, width=15, height=5 ):
        """
        Init a params.
        """
 
        self.__data = []
        self.__width = width
        self.__height = height
        self.__setup( width, height )
 
 
    def __setup( self, width, height ):
        """
        Create a data block.
        """
 
        for hi in range( height ):
 
            self.__data.append( [] )
 
            for wi in range( width ):
 
                self.__data[ hi ].append( " " )
 
 
 
    def draw( self, content, x, y ):
        """
        Draw content to data block.
        """
 
        width = self.__width
 
        for char in content:
 
            if x >= width:
 
                break
 
            self.__data[y][x] = char
 
            x = x + 1
 
 
    def show( self ):
        """
        Print to terminal.
        """
 
        for hi in range( self.__height ):
 
            print "".join( self.__data[ hi ] )


class View( object ):
    """
    Define a sample view.
    """
 
    def setY( self, y ):
        """
        Set a position of y.
        """
 
        self._y = y
 
    def getY( self ):
        """
        Get a position of y.
        """
 
        return self._y
 
    def setX( self, x ):
        """
        Set a position of x.
        """
 
        self._x = x
 
    def getX( self ):
        """
        Get a position of x.
        """
 
        return self._x
 
    def getWidth( self ):
        """
        Get the view width.
        """
 
        return 0
 
    def drawTo( self, canvas, parent = None ):
        """
        Draw something to canvas.
        """
 
        pass



class ViewDecorator( object ):
    """
    Decorator of View.
    """
 
    def __init__( self, *views ):
 
        self.__views = views
 
 
 
    def __call__( self, drawTo ):
        views  = self.__views;
 
        def draw_chain( base_view, canvas ):
 
            drawTo( base_view, canvas )
 
            for view in views:
 
                view.drawTo( canvas, base_view )
 
             
 
        return draw_chain


class Border( View ):
    """
    Extend a View.
    """
 
    def drawTo( self, canvas, parent = None ):
        """
        Draw a border to canvas by parent position.
        """
 
        if parent:
 
            width = parent.getWidth()
            x = parent.getX()
            y = parent.getY()
            canvas.draw( "[", x - 1 , y )
            canvas.draw( "]", width + x , y )
         
 
 
class Text( View ):
    """
    Extend a view.
    """
 
    def __init__( self, content ):
        """
        Set a text.
        """
 
        self.__content = content
 
    def getWidth( self ):
        """
        Get a width of text.
        """
 
        return len( self.__content )
 
    @ViewDecorator( Border() )
    def drawTo( self, canvas, parent = None ):
        """
        Draw a text to canvas.
        """
        canvas.draw( self.__content, self.getX(), self.getY() )


canvas = Canvas()
text = Text( "Sparrow" )
text.setX( 3 )
text.setY( 2 )
text.drawTo( canvas )
canvas.show()
