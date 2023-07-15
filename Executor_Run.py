from Executor import Executor as Executor

# Файл с кодом для тестирования.
TestScript = "Test/script.py"
TestScript_Encoding = "UTF-8"

# Файл с вводными данными.
TestInput = "Test/input.dat"
TestInput_Encoding = "UTF-8"

# Файл с ответами для вводных данных.
TestAnswers = "Test/output.dat"
TestAnswers_Encoding = "UTF-8"

# Получаем код для тестирования.
try: TestScript_String = open(TestScript, "r", encoding = TestScript_Encoding).read()
except FileNotFoundError: raise Exception("Тестовый скрипт не найден.")

# Получаем вводные данные для каждого теста.
try: TestInput_File = open(TestInput, "r", encoding = TestInput_Encoding)
except FileNotFoundError: raise Exception("Файл с вводными данными для теста не найден.")

# Получаем ответы для всех вводных данных.
try: TestAnswers_File = open(TestAnswers, "r", encoding = TestAnswers_Encoding)
except FileNotFoundError: raise Exception("Файл с проверенными результатами не найден.")

# Создаём исполнителя.
newExecutor = Executor()

# Проводим каждый тест и выводим результаты в консоль. В конце исполнитель сбрасывается.
testIndex = 1
while (testInputs := TestInput_File.readline()):
    testInputs = int(testInputs)
    maximumTime = -1
    inputArray = []
    for inputString in range(testInputs):
       inputArray.append(TestInput_File.readline().replace("\n", ""))
    newExecutor.executeFromString(TestScript_String, inputArray)
    print("{0:=^60}".format(" Тест #" + str(testIndex) + " "))
    executionTime = newExecutor.getExecutionTime()
    if newExecutor.output_console == "":
        print("[✝] Результат отсутствует.")
    else:
        testAnswers = TestAnswers_File.readline().split()
        if len(testAnswers) > 1:
            maximumTime = float(testAnswers[1])
        testAnswers = int(testAnswers[0])
        executionResult = newExecutor.output_console.split("\n")[:-1]
        print(executionResult)
        executionResultCount = len(executionResult)
        print("[{0}] Количество выходных строк: {1} / {2}".format("✓" if testAnswers == executionResultCount else "✝", executionResultCount, testAnswers))
        checkCount = testAnswers if testAnswers <= executionResultCount else executionResultCount
        checkSuccess = 0
        for resultIndex in range(checkCount):
            if TestAnswers_File.readline().replace("\n", "") == executionResult[resultIndex]: checkSuccess += 1
        for i in range(testAnswers - checkCount): TestAnswers_File.readline()
        print("[{0}] Выходных строк совпало: {1} / {2}".format("✓" if checkSuccess == checkCount else "✝", checkSuccess, checkCount))
    if maximumTime == -1:
        print("[⌚] Время: {0} с.".format(executionTime))
    else:
        print("[{0}] Время: {1} / {2} с.".format("✝" if executionTime > maximumTime else "✓", executionTime, maximumTime))
    if newExecutor.output_exception is not None:\
        print("Ошибка:", newExecutor.output_exception)
    print("="*60 + "\n")
    newExecutor.reset()
    testIndex += 1

input()
