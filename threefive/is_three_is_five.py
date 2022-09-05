from typing import Union


def is_three_is_five(num: int) -> Union[int, str]:
    num_dict = {3: "three", 5: "five"}
    response_string = ""
    for key in num_dict:
        if num % key == 0:
            response_string += num_dict[key]
    if response_string == "":
        return num
    else:
        return response_string


def main():
    for num in range(1, 101):
        print(is_three_is_five(num))


if __name__ == "__main__":
    main()
