import Splitter

class Norman(object):

    def __init__(self, rules):

        self.splitter = Splitter.Splitter()
        self.columns = None
        self.columnRules = None
        self.rules = rules

    def normalize(self, filepath):
        
        # get lines of file
        lines = open(filepath).readlines()

        # set columns
        self.columns = self.convertLineToArray(lines[0])

        data = lines[1:]

        output = ""
        for line in data:
            # Convert to normalized row
            row = self.normalizeRow(self.convertLineToArray(line))

            # Add linebreak in not last line
            if line is data[-1]:
                row += '/n'

        print(output)

    def normalizeRow(self, row):
        newRow = ''
        fields = enumerate(row)
        for index, datum in fields:
            for rule in self.getColumnRules()[index]:
                rule.normalize(datum)

            if index is not fields[-1]:
                newRow += ','

        return newRow

    def convertLineToArray(self, line):
        #strip
        stripped = line.rstrip()

        # validate quotes are even
        if not stripped.count('"') % 2 and not stripped.count("'") % 2:
            return self.splitter.split(line)

        # throw exception for invalid!

    def getColumnRules(self, reset = False):

        if self.columnRules == None or reset:
            
            columnRules = {}

            print(self.columns)
            for column in self.columns:
                print(column)
                print(self.rules[column])

                names = self.rules[column].split('|')
                modules = []
                for name in names:
                    modules.append(getattr(columnRule + 'Rule', columnRule + 'Rule'))

                columnRules[column] = modules

            self.columnRules = columnRules
        return self.columnRules