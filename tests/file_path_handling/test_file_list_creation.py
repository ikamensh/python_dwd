from python_dwd.file_path_handling.file_list_creation import create_file_list_for_dwd_server
from python_dwd.enumerations.period_type_enumeration import PeriodType
from python_dwd.enumerations.time_resolution_enumeration import TimeResolution
from python_dwd.enumerations.parameter_enumeration import Parameter
from python_dwd.constants.column_name_mapping import FILENAME_NAME


def test_create_file_list_for_dwd_server():
    remote_file_path = create_file_list_for_dwd_server(statid=[1048],
                                                       parameter=Parameter.CLIMATE_SUMMARY,
                                                       time_resolution=TimeResolution.DAILY,
                                                       period_type=PeriodType.RECENT)
    assert remote_file_path[FILENAME_NAME].tolist() == ['daily/kl/recent/tageswerte_KL_01048_akt.zip']