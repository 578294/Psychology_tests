# app/tests/__init__.py
from .bdi_ii import BDITest
from .suicide_risk import SuicideRiskTest
from .mbi import MBITest
from .sf36 import SF36Test
from .ies_r import IESRTest
from .spielberger import SpielbergerTest

__all__ = [
    'BDITest',
    'SuicideRiskTest',
    'MBITest',
    'SF36Test',
    'IESRTest',
    'SpielbergerTest'
]