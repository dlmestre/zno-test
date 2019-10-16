import dateutil.parser


class DateException(Exception):
    pass

class Date:

    @staticmethod
    def parser(date):
        if not date:
            raise DateException('No date provided')
        return dateutil.parser.parse(date)
