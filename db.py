import sys

class DataBase:

    def __init__(self):
        self.dataBase = dict()
        self.transactions = list()

    def Set(self, variableName, value):
        self._updateTransaction(variableName)
        self.dataBase[variableName] = value


    def Get(self, variableName):
        return self.dataBase[variableName] if variableName in self.dataBase else None

    def Unset(self, variableName):
        self._updateTransaction(variableName)
        self.Set(variableName, None)


    def Counts(self, value):
        return self.dataBase.values().count(value)


    def Find(self, value):
        return [dbVariable for dbVariable, dbValue in self.dataBase.items() if dbValue == value]


    def Begin(self):
        self.transactions.append({})


    def Rollback(self):
        if self.transactions:
            lastTranscation = self.transactions.pop()
            for variableName, value in lastTranscation.items():
                self.dataBase[variableName] = value


    def Commit(self):
        self.transactions = []

    def _updateTransaction(self, variableName):
         if self.transactions and not self.transactions[-1].has_key(variableName):
            self.transactions[-1][variableName] = self.Get(variableName)


def run():
    db = DataBase()

    while True :
        query = sys.stdin.readline().strip()
        if query == '':
            return
        tokens = query.split(' ')
        if tokens[0] == 'END':
            return
        elif tokens[0] == 'SET':
            try:
                db.Set(tokens[1], tokens[2])
            except:
                pass
        elif tokens[0] == 'UNSET':
            try:
                db.Unset(tokens[1])
            except:
                pass
        elif tokens[0] == 'GET':
            try:
                result = db.Get(tokens[1])
                print result if result else 'NULL'
            except:
                pass
        elif tokens[0] == 'COUNTS':
            try:
                print db.Counts(tokens[1])
            except:
                pass    
        elif tokens[0] == 'FIND':
            try:
                print db.Find(tokens[1])
            except:
                pass
        elif tokens[0] == 'BEGIN':
            db.Begin()
        elif tokens[0] == 'ROLLBACK':
            db.Rollback()
        elif tokens[0] == 'COMMIT':
            db.Commit()


if __name__=='__main__':
    run()
