'''
Adapted from https://stackoverflow.com/a/64165197/14387100
'''
from matplotlib import ticker
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self, data, type, **kwargs):
        self.data = data
        self.dpi = kwargs.get("dpi", 120)
        self.fig, self.ax = plt.subplots(dpi = self.dpi)
        super(MatplotlibCanvas,self).__init__(self.fig)
        if len(self.data) > 0:
            self.plot(type)
        self.fig.tight_layout()

    def plot(self, type):
        if type == "month plot":
            self.plotMonthPlot()
        elif type == "plot overtime":
            self.overTimePlot()

    def plotMonthPlot(self):
        rule_expenditures = self.data.loc[self.data.Type == "Expense"]
        rule_gains = self.data.loc[self.data.Type == "Revenue"]

        data_expenditures = rule_expenditures.groupby([rule_expenditures.Date.dt.year,
                                                         rule_expenditures.Date.dt.month]).sum()
        data_expenditures = data_expenditures.reindex(data_expenditures.index).fillna(0)

        data_gains = rule_gains.groupby([rule_gains.Date.dt.year,
                                           rule_gains.Date.dt.month]).sum()
        data_gains = data_gains.reindex(data_expenditures.index).fillna(0)

        xticklabels = range(len(data_expenditures.index))
        self.ax.bar(xticklabels,
               data_expenditures.Cost,
                    width=0.5,
                    align = 'edge',
               color='red', alpha=0.46)
        self.ax.bar(xticklabels,
               data_expenditures.Cost,
                    bottom=data_gains.Cost,
                    width=-0.5,
                    align='edge',
               color='blue', alpha=0.46)
        self.ax.axhline(0,
                   color='black',
                   ls='dotted')

        self.ax.xaxis.set_major_locator(ticker.FixedLocator(xticklabels))
        self.ax.set_xticklabels(set([str(year) + '-' + str(month) for year, month in data_expenditures.index]))
        self.ax.set_ylabel("Euro\n(€)")

    def overTimePlot(self):
        self.ax.plot([0,10], [1,2])