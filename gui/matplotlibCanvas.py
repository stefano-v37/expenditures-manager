'''
Adapted from https://stackoverflow.com/a/64165197/14387100
'''

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, **kwargs):
        self.dpi = kwargs.get("dpi", 120)
        self.fig = kwargs["fig"]
        self.ax = kwargs["ax"]
        super(MatplotlibCanvas,self).__init__(self.fig)