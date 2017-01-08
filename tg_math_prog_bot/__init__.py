import sys
import logging
import argparse
import os
from tg_math_prog_bot.tg_math_prog_bot import*

__version__ = "0.0.1.dev0"
logger = logging.getLogger(__name__)

def parse_arguments():
    parser = argparse.ArgumentParser(
        description = 'Telegram Bot for different calculations.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-q', '--quiet', action = 'store_const',
                        const = logging.CRITICAL, dest = 'verbosity',
                        help = 'Be quiet')

    parser.add_argument('-V', '--verbose', action = 'store_const',
                        const = logging.DEBUG, dest = 'verbosity',
                        help = 'Make a lot of noise')

    parser.add_argument('-v', '--version', action = 'version',
                        version = __version__,
                        help = 'Print version number and exit')

    return parser.parse_args()

def main():
    args = parse_arguments()

    logger.addHandler(logging.StreamHandler())
    
    if (args.verbosity):
        logger.setLevel(args.verbosity)
    else:
        logger.setLevel(logging.INFO)

    logger.debug('tg_math_prog_bot version: %s', __version__)
    logger.debug('python version: %s', sys.version.split()[0])

    try:
        with TgMathProgBot():
            pass
    except Exception as e:
        logger.critical('%s', e)
        if args.verbosity == logging.DEBUG:
            raise
        else:
            sys.exit(getattr(e, 'exitcode', 1))

