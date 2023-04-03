from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Sequence

from tabulate import TableFormat

ReportTitle = str  # added for this report, not standard to tabulate
Title = str  # added for this report, not standard to tabulate
TabularData = Mapping[str, Iterable[Any]] | Iterable[Iterable[Any]]
RowData = Mapping[str, Any] | Iterable[Any]  # subset of TabularData with restrictions for test generation
Headers = str | dict[str, str] | Sequence[str]
Tablefmt = str | TableFormat
Floatfmt = str | Iterable[str]
Intfmt = str | Iterable[str]
Numalign = str | None
Stralign = str | None
Missingval = str | Iterable[str]
Showindex = str | bool | Iterable[Any]
DisableNumparse = bool | Iterable[int]
Colalign = Iterable[str | None] | None
Maxcolwidths = int | Iterable[int | None] | None
Rowalign = str | Iterable[str] | None
Maxheadercolwidths = int | Iterable[int] | None


class Defaults:
    REPORT_TITLE_DEFAULT = 'TABULATED TEST FAILURES'
    TABLEFMT_DEFAULT = 'simple'
    FLOATFMT_DEFAULT = 'g'
    INTFMT_DEFAULT = ''
    NUMALIGN_DEFAULT = 'default'
    STRALIGN_DEFAULT = 'default'
    MISSINGVAL_DEFAULT = ''
    SHOWINDEX_DEFAULT = 'default'
    DISABLE_NUMPARSE_DEFAULT = False
    COLALIGN_DEFAULT = None
    MAXCOLWIDTHS_DEFAULT = None
    ROWALIGN_DEFAULT = None
    MAXHEADERCOLWIDTHS_DEFAULT = None


@dataclass
class TabulateProperties:
    report_title: ReportTitle = Defaults.REPORT_TITLE_DEFAULT
    tablefmt: Tablefmt = Defaults.TABLEFMT_DEFAULT
    floatfmt: Floatfmt = Defaults.FLOATFMT_DEFAULT
    intfmt: Intfmt = Defaults.INTFMT_DEFAULT
    numalign: Numalign = Defaults.NUMALIGN_DEFAULT
    stralign: Stralign = Defaults.STRALIGN_DEFAULT
    missingval: Missingval = Defaults.MISSINGVAL_DEFAULT
    showindex: Showindex = Defaults.SHOWINDEX_DEFAULT
    disable_numparse: DisableNumparse = Defaults.DISABLE_NUMPARSE_DEFAULT
    colalign: Colalign = Defaults.COLALIGN_DEFAULT
    maxcolwidths: Maxcolwidths = Defaults.MAXCOLWIDTHS_DEFAULT
    rowalign: Rowalign = Defaults.ROWALIGN_DEFAULT
    maxheadercolwidths: Maxheadercolwidths = Defaults.MAXHEADERCOLWIDTHS_DEFAULT


class AssertionErrorWithRowData(AssertionError):

    def __init__(self, msg: str, row_data: RowData) -> None:
        super().__init__(msg)
        self.__row_data = row_data

    @property
    def row_data(self) -> RowData:
        return self.__row_data
