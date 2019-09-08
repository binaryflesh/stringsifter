# Copyright (C) 2019 FireEye, Inc. All Rights Reserved.

import io
import os
import sys
import contextlib
import typing

if typing.TYPE_CHECKING:
    from os.path import Path
    from typing import Coroutine, Union


def package_base() -> Path:
    """
    return package base folder (one level up from here)
    """
    pth = os.path.join(os.path.dirname(__file__), '..')
    return os.path.abspath(pth)


@contextlib.contextmanager
def redirect_stderr() -> Union[Coroutine, sys.stderr]:
    _stderr = sys.stderr
    sys.stderr = io.StringIO()
    yield
    sys.stderr = _stderr
