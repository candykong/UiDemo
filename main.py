import pytest


from datetime import datetime, timedelta
from util.getIni import get_loan_config



if __name__ == '__main__':
    # # pytest.main([])
    pytest.main(['-q', './testcase/test_01_sbed/test_01_jjgl/test_02_fhxxcx.py'])

    # # pytest.main(['-q','./testcase/test_sbed.py','-k', 'test_parentMenus'])

