import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.ticker import LinearLocator


class Plot:

    def __init__(self, plotType = "", figsize = (16,9)):
        self.plotType = plotType
        print("plotType:" + plotType)
        self.fig, self.ax = plt.subplots(figsize=figsize)
        self.fig.set_size_inches(figsize[0], figsize[1], forward=True)
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

        data_expenditures = (-1)*rule_expenditures.groupby([rule_expenditures.Date.dt.year,
                                                         rule_expenditures.Date.dt.month]).sum()

        data_expenditures = data_expenditures.fillna(0)

        data_gains = rule_gains.groupby([rule_gains.Date.dt.year,
                                         rule_gains.Date.dt.month]).sum()

        data_for_plot = data_expenditures.join(data_gains, how="outer", rsuffix="_revenues",
                                               lsuffix="_expenditures").fillna(0)

        xticklabels = range(len(data_for_plot.index))

        self.ax.bar(xticklabels,
                    data_for_plot["Cost_expenditures"],
                    bottom=data_for_plot["Cost_revenues"],
                    width=0.25,
                    align='edge',
                    label="Expenditures",
                    color='red', alpha=0.46)
        self.ax.bar(xticklabels,
                    data_for_plot["Cost_revenues"],
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
        self.ax.set_xticklabels([str(year) + '-' + str(month) for year, month in data_for_plot.index])

        self.ax.set_ylim(min(data_for_plot.Cost_expenditures + data_for_plot.Cost_revenues) * 1.05,
                         max(data_for_plot.Cost_revenues) * 1.05)
        self.fig.autofmt_xdate()

    def generatePlotOvertime(self, data):
        data.loc[data.Type == "Expense", "Cost"] = - data.loc[data.Type == "Expense", "Cost"]
        data = data.set_index("Date")
        dataOvertime = data.Cost.cumsum()

        self.ax.plot(dataOvertime)
        self.fig.autofmt_xdate()

        xlocator = LinearLocator(10)
        self.ax.xaxis.set_major_locator(xlocator)

    def show(self):
        plt.show()

