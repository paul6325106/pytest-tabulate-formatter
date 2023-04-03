from typing import Dict, Tuple, List

from tabulate import tabulate

from paul6325106.pytesttabulateformatter.domain import Title, Headers, TabularData, TabulateProperties


def write_report(filename: str, report_data: Dict[Title, Tuple[Headers, TabularData]],
                 properties: TabulateProperties) -> None:

    output = f'{properties.report_title}\n'

    for title, (headers, tabular_data) in report_data.items():
        table = tabulate(
            tabular_data=tabular_data,
            headers=headers,
            tablefmt=properties.tablefmt,
            floatfmt=properties.floatfmt,
            intfmt=properties.intfmt,
            numalign=properties.numalign,
            stralign=properties.stralign,
            missingval=properties.missingval,
            showindex=properties.showindex,
            disable_numparse=properties.disable_numparse,
            colalign=properties.colalign,
            maxcolwidths=properties.maxcolwidths,
            rowalign=properties.rowalign,
            maxheadercolwidths=properties.maxheadercolwidths,
        )
        output += f'\n{title}\n\n{table}\n'

    with open(filename, 'w') as file:
        file.write(output)
