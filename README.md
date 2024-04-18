# miniproject-2
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

### Порядок дій
1) вставка початкового коду у файл original solution.py
2) запускаємо з модулем timeit, записуємо час в original_solution.txt
3) оптимізуємо чатом та джеміні по черзі, поки не буде покращення (за потреби створюємо нові файли attempt як у попередньому етапі)
4) результати записуємо у файл new_solution.py (обидва в один файл, але чат і джеміні відповідно підписані коментами)
5) так само новий час записуємо у файл new_solution.txt відповідно для чату та джеміні
6) профіт