def count_lines_from_input():
    print("Введите текст (пустая строка для завершения ввода):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    print("Количество строк:", len(lines))

count_lines_from_input()