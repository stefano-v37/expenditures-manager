import matplotlib.pyplot as plt

class Plot:

    def __init__(self, plotType = "", figsize = (16,9)):
        self.plotType = plotType
        print("plotType:" + plotType)
        self.fig, self.ax = plt.subplots(figsize=figsize)

    def generate(self, data):
        if self.plotType == "month plot":
            self.generateMonthPlot(data)
        elif self.plotType == "plot overtime":
            self.generatePlotOvertime(data)

    def generateMonthPlot(self, data):
        rule_expenditures = data.loc[data.Type == "Expense"]
        rule_gains = data.loc[data.Type == "Revenue"]

        data_expenditures = - rule_expenditures.groupby([rule_expenditures.Date.dt.year,
                                                       rule_expenditures.Date.dt.month]).sum()
        data_expenditures = data_expenditures.reindex(data_expenditures.index).fillna(0)

        data_gains = rule_gains.groupby([rule_gains.Date.dt.year,
                                         rule_gains.Date.dt.month]).sum()
        data_gains = data_gains.reindex(data_expenditures.index).fillna(0)

        xticklabels = range(len(data_expenditures.index))
        self.ax.bar(xticklabels,
                    data_expenditures.Cost,
                    bottom=data_gains.Cost,
                    width=0.25,
                    align='edge',
                    color='red', alpha=0.46)
        self.ax.bar(xticklabels,
                    data_gains.Cost,
                    width=-0.25,
                    align='edge',
                    color='blue', alpha=0.46)
        self.ax.axhline(0,
                        color='black',
                        ls='dotted')
        #
        #
        # self.ax.plot([0,1], [1,3])
        self.ax.set_ylabel("Euro\n(€)")

    def generatePlotOvertime(self, data):
        data.loc[data.Type == "Expense", "Cost"] = - data.loc[data.Type == "Expense", "Cost"]
        data = data.set_index("Date")
        dataOvertime = data.Cost.cumsum()

        self.ax.plot(dataOvertime)
        self.ax.set_ylabel("Euros\n(€)")
        self.fig.autofmt_xdate()

    def show(self):
        plt.show()
