import inspect 
import logging

def logger(log_level=logging.DEBUG):
    """Get the name of the class or method from the place 
        logger has been called"""
    logName = inspect.stack()[1][3]
    logger = logging.getLogger(logName)

    #Aim to log all messages
    logger.setLevel(logging.DEBUG)

    #Each handler is responsible for sending messages of a specific severity to a specific location
    logHandler = logging.FileHandler(filename='automation_ajax.log', mode='w')
    logHandler.setLevel(log_level)
    
    #selects a Formatter object for this handler to use
    logformatter = logging.Formatter('%(asctime)s: - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
    
    logHandler.setFormatter(logformatter)
    logger.addHandler(logHandler)

    return logger 
