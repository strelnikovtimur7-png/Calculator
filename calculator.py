def get_number(prompt):
    #Ввод числа с обработкой ошибок
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['exit', 'quit', 'history', 'clear']:
            return user_input
        try:
            return float(user_input)
        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число.")

def get_operator(prompt):
    #Безопасный ввод оператора.
    valid_operators = ['+', '-', '*', '/', '**', '//', '%']
    while True:
        op = input(prompt).strip().lower()
        if op in ['exit', 'quit', 'history', 'clear']:
            return op
        if op in valid_operators:
            return op
        print(f"Ошибка: Неверный оператор. Допустимые: {', '.join(valid_operators)}")

def calculate(num1, op, num2):
    #Выполнение арифм. операций.
    if op == '+': return num1 + num2
    if op == '-': return num1 - num2
    if op == '*': return num1 * num2
    if op == '/':
        if num2 == 0: raise ZeroDivisionError("Деление на ноль невозможно.")
        return num1 / num2
    if op == '**': return num1 ** num2
    if op == '//':
        if num2 == 0: raise ZeroDivisionError("Целочисленное деление на ноль невозможно.")
        return num1 // num2
    if op == '%':
        if num2 == 0: raise ZeroDivisionError("Нахождение остатка от деления на ноль невозможно.")
        return num1 % num2

def show_history(history):
    #Вывод истории операций.
    if not history:
        print("\nИстория операций пуста.")
    else:
        print("\n--- История операций ---")
        for idx, item in enumerate(history, 1):
            print(f"{idx}. {item}")
        print("------------------------")

def main():
    history = []
    print("Добро пожаловать в мой навороченный супер дупер ультра мега гипер калькулятор типов")
    print("Доступные команды в любой момент: history — история, clear — очистить историю, exit/quit — выход.\n")
    
    #Выбор режима работы
    while True:
        mode = input("Выберите режим работы (1 — Обычный, 2 — Цепочка вычислений): ").strip()
        if mode in ['1', '2']:
            break
        print("Ошибка: введите 1 или 2.")

    current_result = None  # Для режима цепочки

    while True:
        #1: Получение первого числа
        if mode == '2' and current_result is not None:
            num1 = current_result
            print(f"\nТекущее число (результат): {num1}")
        else:
            val = get_number("\nВведите первое число: ")
            if val in ['exit', 'quit']: break
            if val == 'history': show_history(history); continue
            if val == 'clear': history.clear(); print("История очищена."); continue
            num1 = val

        #2: Получение оператора
        op = get_operator("Введите оператор (+, -, *, /, **, //, %): ")
        if op in ['exit', 'quit']: break
        if op == 'history': show_history(history); continue
        if op == 'clear': history.clear(); print("История очищена."); continue

        #3: Получение второго числа
        val = get_number("Введите второе число: ")
        if val in ['exit', 'quit']: break
        if val == 'history': show_history(history); continue
        if val == 'clear': history.clear(); print("История очищена."); continue
        num2 = val

        #4:Вычисление и вывод результата
        try:
            res = calculate(num1, op, num2)
            #убираем .0 если число целое blablabla
            formatted_res = int(res) if res.is_integer() else res
            formatted_num1 = int(num1) if isinstance(num1, float) and num1.is_integer() else num1
            formatted_num2 = int(num2) if num2.is_integer() else num2
            
            record = f"{formatted_num1} {op} {formatted_num2} = {formatted_res}"
            print(f"Результат: {formatted_res}")
            
            history.append(record)
            
            if mode == '2':
                current_result = res
            else:
                # В обычном режиме спрашиваем продолжать ли работу. ОПЯТЬ РАБОТА?!
                choice = input("\nХотите продолжить? (нажмите Enter чтобы продолжить, или введите exit для выхода): ").strip().lower()
                if choice in ['exit', 'quit']:
                    break

        except ZeroDivisionError as e:
            print(f"Ошибка вычисления: {e}")
            if mode == '2':
                print("Цепочка сброшена. Начните заново с ввода первого числа.")
                current_result = None  #Сбрасываем цепочку при ошибке деления на ноль. ЗОЛОТАЯ ЧАША ЗОЛОТЫЕ ЦЕПИИИИИ

    print("\nНу ты пользовался калькулятором молодец пока.")

if __name__ == '__main__':
    main()

