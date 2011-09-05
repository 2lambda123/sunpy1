# -*- coding: utf-8 -*-
# Author: Florian Mayer <florian.mayer@bitsrc.org>

from sunpy.net import attr

def test_dummyattr():
    one = attr.DummyAttr()
    other = attr.ValueAttr({'a': 'b'})
    assert (one | other) is other
    assert (one & other) is other