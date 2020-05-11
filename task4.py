# К реализованному классу Matrix в Домашнем задании 3 добавить следующее:
# 1. __add__ принимающий второй экземпляр класса Matrix и возвращающий сумму матриц, если передалась на вход матрица
# другого размера - поднимать исключение MatrixSizeError (по желанию реализовать так, чтобы текст ошибки содержал
# размерность 1 и 2 матриц - пример: "Matrixes have different sizes - Matrix(x1, y1) and Matrix(x2, y2)")

# 2. __mul__ принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр/

# 3. __str__ переводящий матрицу в строку. Столбцы разделены между собой табуляцией, а строки — переносами строк
# (символ новой строки). При этом после каждой строки не должно быть символа табуляции и в конце не должно быть переноса
# строки.

class Matrix:

    def __init__(self, initial: list = None):
        self.value = initial

    def size(self):

        prev_l = None
        for _ in self.value:
            l = len(_)

            if prev_l != None and l != prev_l:
                raise Exception("Length of X is not compliance")
            else:
                prev_l = l

        return len(self.value), l


    def __add__(self, other = None):

        len_x, len_y = self.size()

        if other != None:
            other_len_x, other_len_y = other.size()
            if (other_len_x != len_x or other_len_y != len_y):
                raise Exception(f"Different sizes: ({len_x},{len_y}) and ({other_len_x},{other_len_y})")


        arr1 = []
        result = []

        for x in range(len_x):
            for y in range(len_y):
                summ = self.value[x][y] + other.value[x][y]
                arr1.append(summ)
            result.append(arr1)
            arr1 = []

        return result

    def __mul__(self, other):

        len_x, len_y = self.size()
        arr1 = []
        result = []

        for x in range(len_x):
            for y in range(len_y):
                mull = self.value[x][y]* other
                arr1.append(mull)
            result.append(arr1)
            arr1 = []

        return result


    def __str__(self):

        len_x, len_y = self.size()

        result = f''

        for x in range(len_x):
            for y in range(len_y):
                num = self.value[x][y]
                result += f'{num}'
                if y < len_y-1:
                    result += f'\t'
                else:
                    result += f'\n'

        return result


if __name__ == "__main__":

    k = 2.45

    m_obj1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m_obj2 = Matrix([[5, 7, 8], [9, 0, 3]])

    # Перезагрузка __add__()
    print(m_obj1 + m_obj2)

    # Перезагрузка __mul__()
    print(m_obj1*k)

    # Перезагрузка __str__()
    print(m_obj1)

