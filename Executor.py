from sys import stdout as sysStdout
from time import time as getTimestamp

# Класс исполнителя тестируемого скрипта.
class Executor:

    # Инициализация.
    def __init__(self):
        self.reset()

    # Полный сброс исполнителя.
    def reset(self):
        self.output_console = ""
        self.timestamp_Start = self.timestamp_End = None
        self.pythonMethod_Print = print
        self.pythonMethod_Input = input
        self.output_exception = None

    # Установка времени начала работы тестируемого скрипта.
    def setTimestampStart(self):
        self.timestamp_Start = getTimestamp()
        
    # Установка времени завершения работы тестируемого скрипта.
    def setTimestampEnd(self):
        self.timestamp_End = getTimestamp()

    """
        Получение итогового времени исполнения тестируемого скрипта в секундах.
        Возвращаемые значения:
          > ∞ - работа скрипта не была завершена.
          > {разница времени завершения и начала исполнения} - работа скрипта завершена успешно.
          > None - скрипт не запускался.
    """
    def getExecutionTime(self):
        if self.timestamp_Start:
            if self.timestamp_End: return self.timestamp_End - self.timestamp_Start
            return float("inf")
        return None

    # Исполнение кода из текста.
    def executeFromString(self, string, inputArray = []):
        inputArray = list(reversed(inputArray))
        def executorPrint(*object, sep = " ", end = "\n", file = sysStdout, flush = False):
            self.output_console += sep.join([str(i) for i in list(object)]) + end
        def executorInput(prompt = ""):
            if inputArray: return inputArray.pop()
            else: raise Exception("Исполняемый код запросил больше вводных данных, чем предоставлено.")
        try:
            self.setTimestampStart()
            try: exec(string, { "print": executorPrint, "input": executorInput })
            except Exception as outputException:
                self.output_exception = outputException
        except Exception as outputException:
            self.output_exception = Exception("В исполняемом коде произошла ошибка.")
        self.setTimestampEnd()