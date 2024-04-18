# miniproject-2
## Вимірювання часу
### Зразок коду
```
import timeit
# Your code here
# For example:
code_to_measure = """
for i in range(1000000):
    pass
"""
# Measure the execution time
execution_time = timeit.timeit(code_to_measure, number=1)
print(f"Execution time: {execution_time} seconds")
```
## Вимірювання памʼяті
### Встановлюємо бібліотеку
```
pip install memory_profiler
```
### Використовуємо декоратор @profile
```
# my_script.py
import numpy as np
import time

@profile
def allocate_memory():
    a = np.random.rand(1000000)
    time.sleep(10)  # Simulate some computation

if __name__ == "__main__":
    allocate_memory()
```
### Запускаємо командою
```
mprof run my_script.py
```
### Дивимось результат
```
mprof plot
```

## Порядок дій
1) вставка початкового коду у файл original solution.py
2) запускаємо з модулем timeit та memory_profiler, записуємо час та в original_solution.txt, а скрін графіку памʼяті в свою папку з відповідною назвою
3) оптимізуємо чатом та джеміні по черзі, поки не буде покращення (за потреби створюємо нові файли attempt як у попередньому етапі)
4) результати записуємо у файл new_solution_chatgpt.py та new_solution_gemini.py
5) так само новий час записуємо у файл new_solution.txt а скріни памʼяті у папку, відповідно для чату та джеміні, підписані коментами хто де
6) профіт