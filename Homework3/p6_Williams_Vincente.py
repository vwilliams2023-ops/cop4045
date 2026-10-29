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

    def absolute_path(self) -> list[Entry]:
        """Return this entry and its ancestors, ending with the root entry."""
        parent = self.parent()
        if parent is None:
            return [self]
        return [self] + parent.absolute_path()

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


class Folder(Entry):
    """Represent a folder containing file and folder entries."""

    def __init__(self, name: str, parent: Entry | None = None) -> None:
        """Initialize an empty folder."""
        super().__init__(name, parent)
        self._children: list[Entry] = []

    def add(self, entry: Entry) -> None:
        """Add an entry to this folder's children."""
        self._children.append(entry)

    def size(self) -> int:
        """Return the combined size of all files in this folder tree."""
        return total_size(self._children)

    def children(self) -> tuple[Entry, ...]:
        """Return this folder's children as an immutable tuple."""
        return tuple(self._children)


def total_size(entries: Iterable[Entry]) -> int:
    """Return the combined size of entries using the Entry interface."""
    return sum(entry.size() for entry in entries)


def find_large_files(entry: Entry, minimum_size: int) -> list[File]:
    """Find files at least minimum_size bytes starting at entry.

    If entry is a File, return it only when its size meets the threshold.
    If entry is a Folder, recursively search its children and return matching
    files in child traversal order.
    """
    if isinstance(entry, File):
        return [entry] if entry.size() >= minimum_size else []
    if isinstance(entry, Folder):
        return [
            file
            for child in entry.children()
            for file in find_large_files(child, minimum_size)
        ]
    raise TypeError("entry must be a File or Folder")


def main() -> None:
    """Demonstrate recursive sizing and large-file searches."""
    folder = Folder("documents")
    drafts = Folder("drafts", folder)
    revisions = Folder("revisions", drafts)
    folder.add(File("report.txt", folder, 1200))
    folder.add(drafts)
    drafts.add(File("notes.txt", drafts, 300))
    drafts.add(revisions)
    revisions.add(File("revision.txt", revisions, 1800))
    print(f"Total size: {folder.size()} bytes")
    path = revisions.absolute_path()
    print("absolute_path():", " -> ".join(entry.name for entry in path))
    for threshold in (1000, 1500):
        large_files = find_large_files(folder, threshold)
        print(
            f"Files at least {threshold} bytes:",
            ", ".join(file.name for file in large_files),
        )


if __name__ == "__main__":
    main()