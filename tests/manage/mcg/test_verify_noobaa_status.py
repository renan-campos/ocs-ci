import logging

from ocs_ci.framework.pytest_customization.marks import tier2
from ocs_ci.framework.testlib import polarion_id, bugzilla
from ocs_ci.ocs import defaults

log = logging.getLogger(__name__)


@tier2
@polarion_id('OCS-2084')
@bugzilla('1799077')
def test_verify_noobaa_status(mcg_obj_session):
    """
    Verify noobaa status output is clean without any errors
    """
    # Get noobaa status
    status = mcg_obj_session.exec_mcg_cmd('status').stderr
    for line in status.split('\n'):
        if 'Not Found' in line:
            assert 'Optional' in line, f"Error in noobaa status output- {line}"
    log.info("Verified: noobaa status does not contain any error.")
