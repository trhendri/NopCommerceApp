import logging

class LogGen:
    # logging.basicConfig(filename="Logs/automation.log",
    #                     format='%(asctime)s: %(levelname)s: %(message)s,'
    #                     datefmt= '%m/%d/%Y %I:%M:%S %p')
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='Logs/mylog.log', mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt=' %m/%d/%Y %I:%M:%S%p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger