"""冒泡排序示例：支持升序/降序，并附带结果校验。"""

from __future__ import annotations


def bubble_sort(nums: list[int], *, reverse: bool = False) -> list[int]:
    """使用冒泡排序返回新列表，不修改原始输入。

    Args:
        nums: 待排序整数列表。
        reverse: True 时按降序排序；False 时按升序排序。

    Returns:
        排序后的新列表。
    """
    arr = nums[:]
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            should_swap = arr[j] < arr[j + 1] if reverse else arr[j] > arr[j + 1]
            if should_swap:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # 本轮没有发生交换，说明已经有序
        if not swapped:
            break

    return arr


def _demo() -> None:
    sample = [64, 34, 25, 12, 22, 11, 90, 22, -3]

    asc = bubble_sort(sample)
    desc = bubble_sort(sample, reverse=True)

    print("原始数组:", sample)
    print("升序结果:", asc)
    print("降序结果:", desc)

    # 与 Python 内置排序对比，方便快速验证正确性
    print("升序校验:", asc == sorted(sample))
    print("降序校验:", desc == sorted(sample, reverse=True))


if __name__ == "__main__":
    _demo()
