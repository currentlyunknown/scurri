def is_three_is_five(num: int) -> [int, str]:
    num_dict = {3: 'three', 5: 'five'}
    string = ""
    for key in num_dict:
        if num % key == 0:
            string += num_dict[key]
    if string == "":
        return num
    else:
        return string


def main():
    for num in range(1, 101):
        print(is_three_is_five(num))


if __name__ == '__main__':
    main()
