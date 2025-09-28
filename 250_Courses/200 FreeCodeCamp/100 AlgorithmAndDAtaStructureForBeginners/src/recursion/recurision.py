def sum_recursive(items: list[int]) -> int:
    if len(items) == 1:
        return items[0]
    return items[0] + sum_recursive(items[1:])


def main():
    vals = [1, 2, 3, 4, 5]
    result = sum_recursive(vals)
    print(result)
    assert result == 15 and result == sum(vals), f"expected 15 got {result}"

if __name__ == '__main__':
    main()
