"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MiniCassandra:

    def __init__(self):
        self.db = {}
    """
    @param: row_key: a string
    @param: column_key: An integer
    @param: value: a string
    @return: nothing
    """

    def insert(self, row_key, column_key, value):
        columns = self.db.get(row_key, {})
        columns[column_key] = value
        self.db[row_key] = columns

    """
    @param: row_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """

    def query(self, row_key, column_start, column_end):
        columns = self.db.get(row_key, {})
        result = []
        for key, val in columns.items():
            if column_start <= key <= column_end:
                result.append((key, val))
        result = sorted(result, key=lambda x: x[0])
        return [Column(key, val) for key, val in result]