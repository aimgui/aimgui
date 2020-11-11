from pyo import *

from .. import Page


class MathOps(Page):
    """
    05-math-ops.py - Audio objects and arithmetic expresssions.

    This script shows how a PyoObject reacts when used inside an
    arithmetic expression.

    Multiplication, addition, division and substraction can be applied
    between pyo objects or between pyo objects and numbers. Doing so
    returns a Dummy object that outputs the result of the operation.

    A Dummy object is only a place holder to keep track of arithmetic
    operations on audio objects.

    PyoObject can also be used in expression with the exponent (**),
    modulo (%) and unary negative (-) operators.

    """

    def do_reset(self):
        # Drops the gain by 20 dB.
        self.server.amp = 0.1

        # Full scale sine wave
        a = Sine()

        # Creates a Dummy object `b` with `mul` attribute
        # set to 0.5 and leaves `a` unchanged.
        self.b = b = a * 0.5

        # Instance of Dummy class
        print(b)

        # Computes a ring modulation between two PyoObjects
        # and scales the amplitude of the resulting signal.
        c = Sine(300)
        self.d = d = a * c * 0.3

        # PyoObject can be used with Exponent operator.
        self.e = e = c ** 10 * 0.4

        # Displays the ringmod and the rectified signals.
        sp = self.gui.spectrum([d, e])
        sc = self.gui.scope([d, e])

    def do_start(self):
        self.b.out()
        self.d.out()
        self.e.out()
