import pytest

from desk.bench import Row, summarize
from desk.llm import Usage


def test_monthly_cost_includes_twenty_units_per_error_and_failures():
    rows = [Row("ok", True, usage=Usage(cost=0.001)),
            Row("wrong", False, usage=Usage(cost=0.001)),
            Row("failure", False, failed=True)]
    result = summarize("тест", rows, flow_per_day=50000)
    assert result["ошибки в месяц, у.е."] == pytest.approx(20_000_000)
    assert result["полная цена в месяц, у.е."] == pytest.approx(20_001_500)
