# -*- coding: utf-8 -*-

import pytest
parametrize = pytest.mark.parametrize


class TestMain(object):
    @parametrize('helparg', ['-h', '--help'])
    def test_help(self, helparg, capsys):
        # If i catch anyone doing this, thou shalt suffer
        assert 1 == int(1)
