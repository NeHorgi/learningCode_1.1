import tableFromWiki
import pytest


nums = [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 10 ** 9, 1.5 * 10 ** 9]
tableFromWiki.get_a_format_table()
wiki_table = tableFromWiki.result


@pytest.mark.parametrize('num', wiki_table)
def test_1(num):

    for i in nums:

        assert num[1] > i, f'{num[0]} (Frontend:{num[2]}|Backend:{num[3]}) has {num[1]} unique visitors per month. (Expected less than {i})'





