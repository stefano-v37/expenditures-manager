import os
import pandas as pd
from datetime import datetime as dt

from .utilities import get_configuration_entries, THIS_DIR


class Instance:
    def __init__(self, path=None, user='default'):
        self.user = user
        path_std, columns_std, name_std = get_configuration_entries(self.user)
        if path:
            if path == 'this':
                self.path = '\\'.join([str(x) for x in THIS_DIR.split('\\')][:-1]) + '\\output'
            else:
                self.path = path
        else:
            if path_std:
                self.path = os.environ.get(path_std)
            else:
                self.path = '\\'.join([str(x) for x in THIS_DIR.split('\\')][:-1]) + '\\output'

        self.new = not name_std in os.listdir(self.path)
        self.link = self.path + '\\' + name_std
        if self.new:
            self.data = pd.DataFrame(columns=['Date', 'Shop', 'Description', 'Event', 'Cost'])
        else:
            self.data = pd.read_csv(self.link)
        self.data['Date'] = pd.to_datetime(self.data.Date)

    def add_data(self,  **kwargs):
        success = False
        date = kwargs.get('date', dt.now())
        shop = kwargs.get('shop', '')
        description = kwargs.get('description', '')
        event = kwargs.get('event', '')
        cost = kwargs.get('cost', 0)
        new_line = {'Date' : pd.to_datetime(date), 'Shop' : shop, 'Description' : description, 'Event' : event, 'Cost' : cost}
        check = self.check_duplicates(new_line)
        if check:
            if kwargs.pop('force_writing', False):
                self.data = self.data.append(new_line, ignore_index=True)
                success = True
        else:
            self.data = self.data.append(new_line, ignore_index=True)
            success = True
        if success:
            print(str(pd.DataFrame(self.data.iloc[-1])) + '\n' + 'has been written in the db, please save to store the data')

    def check_duplicates(self, new_line):
        check = [y for _,y in new_line.items()]
        line_counter = 0
        duplicates = []
        for x in self.data.values:
            flag = set(x) == set(check)
            if flag:
                duplicates.extend([line_counter])
            line_counter += 1
        if duplicates:
            print('Values already present in db, check below (use **kwargs to force the writing)')
            print(self.data.loc[self.data.index.isin(duplicates)])

        if duplicates:
            return True
        else:
            return False


    def save_df(self):
        self.data.to_csv(self.link, index = False)