class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def separate(cls, date):
        d = [int(x) for x in date.split('-')]
        return d

    @staticmethod
    def validate(date):
        if date[0] not in range(1, 32):
            raise ValueError()
        if date[1] not in range(1, 13):
            raise ValueError()
        if date[2] not in range(1, 9999):
            raise ValueError()



d = Date('5-05-2022')
dmy = Date.separate(d.date)
Date.validate(dmy)

