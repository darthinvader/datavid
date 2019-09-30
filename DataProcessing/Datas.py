import pandas as pd


class Datas:
    def __init__(self, file, encoding = 'ISO-8859-1'):
        """
        The constructor of the Datas object.
        :param file: the file we want to read as csv and store it into a pandas dataframe.
        :param encoding: the encoding of the csv.
        """
        self.df = pd.read_csv(file, encoding=encoding)
        self.selected_df = None
        self.selected_columns = None
        self.column_categories = list()

    def select_columns(self, columns):
        """
        This function takes the selected columns and places them into a second dataframe.
        :param columns: the columns we select.
        :return: None
        """
        self.selected_columns = columns
        self.selected_df = self.df[columns].copy()

    def add_column_category(self, column, category):
        """
        This function takes a column name and a category and adds them as a tuple in a list. This is done
        to know which column has which data for visualization.
        :param column: the column.
        :param category: the category.
        :return: None
        """
        self.column_categories.append((column, category))

    def get_dataframe(self):
        """
        Returns the original dataframe.
        :return: the original dataframe.
        """
        return self.df

    def set_dataframe(self, file, encoding = 'ISO-8859-1'):
        """
        This function sets a new dataframe overriding the old one.
        :param file: the csv we want to read.
        :param encoding: the encoding of the csv.
        :return:
        """
        self.df = self.df = pd.read_csv(file, encoding=encoding)
