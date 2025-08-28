import streamlit as st


def parse_page_numbers(page_string: str) -> list[int] | None:
    """Parses a string like '1, 3, 5-7' into a list of numbers [1, 3, 5, 6, 7]."""
    if not page_string:
        return None

    pages = set()

    for part in page_string.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            try:
                start, end = map(int, part.split("-"))
                if start <= end:
                    pages.update(range(start, end + 1))
            except ValueError:
                st.warning(f"Ignoring invalid range: {part}")
        else:
            try:
                pages.add(int(part))
            except ValueError:
                st.warning(f"Ignoring invalid page number: {part}")

    return sorted(list(pages))
