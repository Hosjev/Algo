""" Exceptions (custom) for number game """


class Error(Exception):
    pass


class ValueInteger(Error):
    pass


class ValueTooHigh(Error):
    pass


class ValueTooLow(Error):
    pass


class ValueSoClose(Error):
    pass
