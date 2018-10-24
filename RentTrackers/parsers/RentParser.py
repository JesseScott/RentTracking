import abc


class RentParser(object):
    """
    An abstract class defining a parser - a class that holds an instance of a target data source (website)
    and a spider (scrapy crawler)
    """
    def __init__(self, location=None):
        self.location = location
        if location is None:
            raise ValueError('Location cannot be empty')

        self.spider = None

    @abc.abstractmethod
    def configure(self, config):
        pass

    @abc.abstractmethod
    def parse(self, location):
        pass

