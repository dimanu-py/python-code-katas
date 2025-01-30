import pytest
from approvaltests.reporters import GenericDiffReporter, GenericDiffReporterConfig


class PyCharmReporter(GenericDiffReporter):
    def __init__(self):
        config = GenericDiffReporterConfig(
            name="PyCharm",
            path="/home/dimanu/.local/share/JetBrains/Toolbox/apps/pycharm-professional",
            extra_args=["diff"]
        )
        super().__init__(config)


@pytest.fixture(scope="session", autouse=True)
def pycharm_diff_reporter():
    return PyCharmReporter()
