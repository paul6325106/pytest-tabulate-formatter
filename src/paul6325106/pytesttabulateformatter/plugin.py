from paul6325106.pytesttabulateformatter.domain import Defaults, TabulateProperties
from paul6325106.pytesttabulateformatter.report import write_report


def pytest_addoption(parser):
    group = parser.getgroup('tabulate-formatter')
    group.addoption('--tabular-filename', action='store', default='tabular_report.txt')
    group.addoption('--report-title', action='store', default=Defaults.REPORT_TITLE_DEFAULT)
    group.addoption('--tablefmt', action='store', default=Defaults.TABLEFMT_DEFAULT)
    group.addoption('--floatfmt', action='store', default=Defaults.INTFMT_DEFAULT)
    group.addoption('--numalign', action='store', default=Defaults.NUMALIGN_DEFAULT)
    group.addoption('--stralign', action='store', default=Defaults.STRALIGN_DEFAULT)
    group.addoption('--missingval', action='store', default=Defaults.MISSINGVAL_DEFAULT)
    group.addoption('--showindex', action='store', default=Defaults.SHOWINDEX_DEFAULT)
    group.addoption('--disable-numparse', action='store', default=Defaults.DISABLE_NUMPARSE_DEFAULT)
    group.addoption('--colalign', action='store', default=Defaults.COLALIGN_DEFAULT)
    group.addoption('--maxcolwidths', action='store', default=Defaults.MAXCOLWIDTHS_DEFAULT)
    group.addoption('--rowalign', action='store', default=Defaults.ROWALIGN_DEFAULT)
    group.addoption('--maxheadercolwidths', action='store', default=Defaults.MAXHEADERCOLWIDTHS_DEFAULT)


def pytest_configure(config):
    filename = config.getoption('--tabular-filename')

    properties = TabulateProperties()
    properties.report_title = config.getoption('--report-title')
    properties.tablefmt = config.getoption('--tablefmt')
    properties.floatfmt = config.getoption('--floatfmt')
    properties.numalign = config.getoption('--numalign')
    properties.stralign = config.getoption('--stralign')
    properties.missingval = config.getoption('--missingval')
    properties.showindex = config.getoption('--showindex')
    properties.disable_numparse = config.getoption('--disable-numparse')
    properties.colalign = config.getoption('--colalign')
    properties.maxcolwidths = config.getoption('--maxcolwidths')
    properties.rowalign = config.getoption('--rowalign')
    properties.maxheadercolwidths = config.getoption('--maxheadercolwidths')

    if filename:
        config._tabulate_formatter = TabulateFormatter(filename, properties)
        config.pluginmanager.register(config._tabulate_formatter)


def pytest_unconfigure(config):
    tabulate_formatter = getattr(config, '_tabulate_formatter', None)
    if tabulate_formatter:
        del config._tabulate_formatter
        config.pluginmanager.unregister(tabulate_formatter)


class TabulateFormatter:

    def __init__(self, filename: str, properties: TabulateProperties):
        self.__filename = filename
        self.__properties = properties
        self.__report_data = {}

    def pytest_runtest_makereport(self, item, call):
        tabulate_formatted = next(item.iter_markers(name='tabulate_formatted'), None)

        if call.when != 'call' or not tabulate_formatted or not call.excinfo:
            return

        title = tabulate_formatted.kwargs.get('title')
        headers = tabulate_formatted.kwargs.get('headers')
        row_data = call.excinfo.value.row_data

        if title in self.__report_data:
            _, tabular_data = self.__report_data[title]
        else:
            tabular_data = []
            self.__report_data[title] = headers, tabular_data

        tabular_data.append(row_data)

    def pytest_sessionfinish(self):
        write_report(self.__filename, self.__report_data, self.__properties)
