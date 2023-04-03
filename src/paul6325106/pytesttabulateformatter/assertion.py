__all__ = [
    'fail',
]

from typing import Optional

from pytest import fail as fail_original

from paul6325106.pytesttabulateformatter.domain import AssertionErrorWithRowData, TabularData


def fail(reason: str = "", pytrace: bool = True, row_data: Optional[TabularData] = None) -> None:
    if row_data is None:
        fail_original(reason, pytrace)
    else:
        raise AssertionErrorWithRowData(reason, row_data)
