from loguru import logger


def add(num1: float, num2: float) -> float:
    """
    Performs arithmetic addition of two floating point numbers
    """

    if not isinstance(num1, float) or not isinstance(num2, float):
        raise TypeError

    logger.debug('Performing addition')
    return num1 + num2
