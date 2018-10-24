from RentTrackers.managers.LoggerManager import LoggerManager as logger
from RentTrackers.managers.ParserManager import ParserManager


class RentTrackers:
    """
    The main entry point into the application
    Responsible for validating the UseCase, and initializing/orchestrating the parsing jobs
    """

    # List of supported actions
    usecases = {'rent-parser'}

    def __init__(self, use_case: str, location: str, config: str):
        """
        
        :param use_case: the use case that we want to run
        :param location: the location to parse
        :param config: the configuration to run
        """

        self.use_case = use_case
        self.location = location
        self.config = config

        # Determine if we should run the use case
        if self.use_case in self.usecases:
            self.run_rent_parsers()
        else:
            ValueError("No Valid UseCase Found")

    @staticmethod
    def run_rent_parsers():
        logger.info(__name__, "Starting Rent Parsing")
        rent_parsers = ParserManager.get_rent_parsers()

        for parser in rent_parsers:
            parser.configure()

        for parser in rent_parsers:
            parser.parse()





