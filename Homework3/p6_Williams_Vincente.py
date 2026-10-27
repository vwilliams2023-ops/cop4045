from collections.abc import Iterable


class Entry:
    """Represent an entry with a name and an optional parent entry."""

    def __init__(self, name: str, parent: Entry | None = None) -> None:
        """Initialize an entry."""
        self.name: str = name
        self._parent: Entry | None = parent

    def parent(self) -> Entry | None:
        """Return this entry's parent, or None when it has no parent."""
        return self._parent

    def size(self) -> int:
        """Return this entry's size in bytes.

        Subclasses provide the size calculation.
        """
        raise NotImplementedError("Entry subclasses must implement size()")


class File(Entry):
    """Represent a file entry with a nonnegative size in bytes."""

    def __init__(
        self, name: str, parent: Entry | None, bytes_used: int
    ) -> None:
        """Initialize a file and reject invalid byte counts."""
        super().__init__(name, parent)
        if isinstance(bytes_used, bool) or not isinstance(bytes_used, int):
            raise TypeError("bytes_used must be an integer")
        if bytes_used < 0:
            raise ValueError("bytes_used must be nonnegative")
        self.bytes_used: int = bytes_used

    def size(self) -> int:
        """Return the number of bytes used by this file."""
        return self.bytes_used


def total_size(entries: Iterable[Entry]) -> int:
    """Return the combined size of entries using the Entry interface."""
    return sum(entry.size() for entry in entries)


def main() -> None:
    """Demonstrate polymorphic size processing through Entry references."""
    folder = Entry("documents")
    entries: list[Entry] = [
        File("report.txt", folder, 1200),
        File("notes.txt", folder, 300),
    ]
    print(f"Total size: {total_size(entries)} bytes")


if __name__ == "__main__":
    main()