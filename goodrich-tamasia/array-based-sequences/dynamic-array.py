"""Dynamic Array."""

from __future__ import annotations

from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")


class DynamicArray(Generic[T]):
    __slots__ = ("_size", "_capacity", "_data")

    DEFAULT_CAPACITY = 4
    GROWTH_FACTOR = 2
    SHRINK_THRESHOLD = 0.25

    def __init__(self, iterable: Optional[Iterable[T]] = None) -> None:
        self._size = 0
        self._capacity = self.DEFAULT_CAPACITY
        self._data = self._make_array(self._capacity)
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> T:
        return self._data[self._normalize_index(index)]

    def __setitem__(self, index: int, value: T) -> None:
        self._data[self._normalize_index(index)] = value

    def __iter__(self) -> Iterator[T]:
        for i in range(self._size):
            yield self._data[i]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self)})"

    def append(self, value: T) -> None:
        if self._size == self._capacity:
            self._resize(self._capacity * self.GROWTH_FACTOR)
        self._data[self._size] = value
        self._size += 1

    def pop(self) -> T:
        if self._size == 0:
            raise IndexError("pop from empty DynamicArray")
        value = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        if self._should_shrink():
            self._resize(max(self.DEFAULT_CAPACITY, self._capacity // self.GROWTH_FACTOR))
        return value  # type: ignore[return-value]

    def insert(self, index: int, value: T) -> None:
        if index < 0:
            index += self._size
        index = max(0, min(index, self._size))
        if self._size == self._capacity:
            self._resize(self._capacity * self.GROWTH_FACTOR)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def remove(self, value: T) -> None:
        for i in range(self._size):
            if self._data[i] == value:
                self._delete_at_index(i)
                return
        raise ValueError(f"{value} not found")

    def clear(self) -> None:
        self._data = self._make_array(self.DEFAULT_CAPACITY)
        self._size = 0
        self._capacity = self.DEFAULT_CAPACITY

    def capacity(self) -> int:
        return self._capacity

    def is_empty(self) -> bool:
        return self._size == 0

    def _delete_at_index(self, index: int) -> None:
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        if self._should_shrink():
            self._resize(max(self.DEFAULT_CAPACITY, self._capacity // self.GROWTH_FACTOR))

    def _should_shrink(self) -> bool:
        return self._capacity > self.DEFAULT_CAPACITY and self._size < self._capacity * self.SHRINK_THRESHOLD

    def _resize(self, new_capacity: int) -> None:
        new_data = self._make_array(new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def _normalize_index(self, index: int) -> int:
        if not isinstance(index, int):
            raise TypeError("index must be an integer")
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return index

    @staticmethod
    def _make_array(capacity: int) -> list[Optional[T]]:
        return [None] * capacity


if __name__ == "__main__":
    arr = DynamicArray([1, 2, 3])
    arr.append(4)
    print(len(arr))
    B = [1, 2]
    A = [1, 2, B]
    print(A)
