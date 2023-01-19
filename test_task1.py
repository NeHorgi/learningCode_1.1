import tableFromWiki
import pytest


nums = [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9]
tableFromWiki.get_a_format_table()
wiki_table = tableFromWiki.get_a_format_table()


@pytest.fixture(params=wiki_table)
def take_a_num(request):

    yield request.param


@pytest.mark.parametrize('num', nums)
def test_1(num):

    error = []

    for row in wiki_table:

        if num > row[1]:
            error.append(row)

    assert not error, [f'{row[0]} (Frontend:{row[2]}|Backend:{row[3]}) has {row[1]} unique visitors per month. (Expected less than {num})' for row in error]








