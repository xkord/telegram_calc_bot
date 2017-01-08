import logging
import os
import sys
import time
import telepot
from simpleeval import*
import ast
import operator
import hashlib
import base64
import math

logger = logging.getLogger(__name__)

class TgMathProgBot:

    def __init__(self):
        self.simple_eval = SimpleEval()
        self.simple_eval.functions = {'double': self.__double, \
                                      'hex' : self.__hex, 'Hex' : self.__hex, 'HEX' : self.__hex, \
                                      'int' : self.__int, 'Int' : self.__int, 'INT' : self.__int, \
                                      'md5' : self.__md5, 'Md5' : self.__md5, 'MD5' : self.__md5, \
                                      'sin' : self.__sin, 'Sin' : self.__sin, 'SIN' : self.__sin, \
                                      'cos' : self.__cos, 'Cos' : self.__cos, 'COS' : self.__cos, \
                                      'sqrt' : self.__sqrt, 'Sqrt' : self.__sqrt, 'SQRT' : self.__sqrt, \
                                      'pi' : self.__pi, 'Pi' : self.__pi, 'PI' : self.__pi, \
                                      'e' : self.__e, 'E' : self.__e, \
                                      'f' : self.__factorial, 'F' : self.__factorial, \
                                      'sha256' : self.__sha256, 'Sha256' : self.__sha256, 'SHA256' : self.__sha256, \
                                      'base64enc' : self.__base64enc, 'base64dec' : self.__base64dec }
        self.simple_eval.operators[ast.BitXor] = operator.xor
        TOKEN = '283433447:AAHMgnQY-A3YqE09s4-flt54WqfhcSvDkO4'
        try:
            self.bot = telepot.Bot(TOKEN)
        except Exception as e:
            logger.critical('%s', e)

    def __enter__(self):
        logger.debug('Starting MathProgBot')
        self.bot.message_loop(self.__message_handle)
        while 1:
            time.sleep(10)

    def __exit__(self, type, value, traceback):
        pass

    def __message_handle(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        logger.debug('Content Type: %s; Chat Type: %s; Chat ID: %s', \
                     content_type, chat_type, chat_id)
        if content_type == 'text':
            input_text = msg['text']
            logger.debug('Input Text: %s', input_text);
            if input_text.lower() == "/help":
                answer =  self.bot_info()
            elif input_text.lower() == "/start":
                answer =  "Bot is working. Enter /help."
            else:
                answer = "Operation is not supported."
                try:
                    if input_text.lower()[0:5] == "/calc":
                        answer = self.__calculate(input_text[6:])
                    else:
                        answer = self.__calculate(input_text)
                except Exception as e:
                    logger.critical('%s', e)
            try:
                if (len(str(answer)) < 4096):
                    self.bot.sendMessage(chat_id, answer)
                else:
                    answer = "Operation result is too long."
                    self.bot.sendMessage(chat_id, answer) 
            except Exception as e:
                logger.critical('%s', e)
                return None
    def bot_info(self):
        info =  "Bot for different calculations. \r\n" + \
                "Supported operations: \r\n" + \
                "x + y \r\n" + \
                "x - y \r\n" + \
                "x * y \r\n" + \
                "x / y \r\n" + \
                "x % y \r\n" + \
                "x ** y \r\n" + \
                "x == y \r\n" + \
                "x < y \r\n" + \
                "x > y \r\n" + \
                "x <= y \r\n" + \
                "x >= y \r\n" + \
                "sin(x) \r\n" + \
                "cos(x) \r\n" + \
                "sqrt(x) \r\n" + \
                "pi() , where π = 3.141592...\r\n" + \
                "e() , where e = 2.718281...\r\n" + \
                "f(x) , factorial x! \r\n" + \
                "hex(x) \r\n" + \
                "int(x) \r\n" + \
                "base64enc(\"string\") \r\n" + \
                "base64dec(\"c3RyaW5n\") \r\n" + \
                "md5(\"string\") \r\n" + \
                "sha256(\"string\") \r\n" + \
                "\r\nExample: base64dec(base64enc(hex(int((((2**3) + 12)/172 - 99)**2))))\r\n" + \
                "\r\nP.S. Bot is in development state."
        return info

    def __calculate(self, input_text):
        try:
            result = self.simple_eval.eval(input_text)
        except Exception as e:
            logger.critical('%s', e)
            return "Operation is not supported."
        return result

    def __sin(self, x):
        return math.sin(x)

    def __cos(self, x):
        return math.cos(x)

    def __sqrt(self, x):
        return math.sqrt(x)

    def __pi(self):
        return math.pi

    def __e(self):
        return math.e

    def __double(self, x):
        return x * 2

    def __hex(self, x):
        return hex(x)

    def __int(self, x):
        return int(x)

    def __md5(self, x):
        return hashlib.md5(x.encode()).hexdigest()

    def __sha256(self, x):
        return hashlib.sha256(x.encode()).hexdigest()

    def __base64enc(self, x):
        return base64.b64encode(x.encode())

    def __base64dec(self, x):
        return base64.b64decode(x).decode() 

    def __factorial(self, x):
        return math.factorial(x)