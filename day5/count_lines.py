def count_lines_from_input():
    print("Введите текст (пустая строка для завершения ввода):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    print(f"\nКоличество строк: {len(lines)}")

if __name__ == "__main__":
    count_lines_from_input()