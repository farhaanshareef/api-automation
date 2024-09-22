import pytest

def pytest_html_report_title(report):
    ''' modifying the title of html report '''
    report.title = "API Automation Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    outcome._result.custom_description = item.function.__doc__