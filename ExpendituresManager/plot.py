import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.ticker import LinearLocator


class Plot:

    def __init__(self, plotType = "", figsize = (16,9)):
        self.plotType = plotType
        print("plotType:" + plotType)
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.ax.set_ylabel("Euro\n(€)")
        self.ax.grid(axis="y")

    def generate(self, data):
        if len(data) > 0:
            if self.plotType == "month plot":
                self.generateMonthPlot(data)
            elif self.plotType == "plot overtime":
                self.generatePlotOvertime(data)

    def generateMonthPlot(self, data):
        rule_expenditures = data.loc[data.Type == "Expense"]
        rule_gains = data.loc[data.Type == "Revenue"]

        data_expenditures = - rule_expenditures.groupby([rule_expenditures.Date.dt.year,
                                                       rule_expenditures.Date.dt.month]).sum()

        data_expenditures = data_expenditures.fillna(0)

        data_gains = rule_gains.groupby([rule_gains.Date.dt.year,
                                         rule_gains.Date.dt.month]).sum()
        data_gains = data_gains.fillna(0)

        xticklabels = range(len(data_expenditures.index))
        self.ax.bar(xticklabels,
                    data_expenditures["Cost"],
                    bottom=data_gains["Cost"],
                    width=0.25,
                    align='edge',
                    label = "Expenditures",
                    color='red', alpha=0.46)
        self.ax.bar(xticklabels,
                    data_gains["Cost"],
                    width=-0.25,
                    align='edge',
                    label="Revenues",
                    color='blue', alpha=0.46)
        self.ax.axhline(0,
                        color='black',
                        ls='dotted')

        self.ax.legend(ncol=2, bbox_to_anchor=(0.5, 1),
                  loc='lower center')
        self.ax.xaxis.set_major_locator(ticker.FixedLocator(xticklabels))
        self.ax.set_xticklabels([str(year) + '-' + str(month) for year, month in data_expenditures.index])

        self.ax.set_ylim(min(data_expenditures.Cost+data_gains.Cost)*1.05, max(data_gains.Cost)*1.05)

    def generatePlotOvertime(self, data):
        data.loc[data.Type == "Expense", "Cost"] = - data.loc[data.Type == "Expense", "Cost"]
        data = data.set_index("Date")
        dataOvertime = data.Cost.cumsum()

        self.ax.step(dataOvertime.index,
                     dataOvertime)
        self.fig.autofmt_xdate()

        xlocator = LinearLocator(10)
        self.ax.xaxis.set_major_locator(xlocator)

    def show(self):
        plt.show()
