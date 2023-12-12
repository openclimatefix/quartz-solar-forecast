from quartz_solar_forecast.dataset.make_test_set import make_test_set
import tempfile
import pandas as pd


def test_make_test_set():
    with tempfile.TemporaryDirectory() as tmpdirname:

        output_file = tmpdirname + '/test.csv'

        make_test_set(output_file_name=output_file)

        test_set = pd.read_csv(output_file)
        assert len(test_set) == 50*50
        # we can check this as we have set the seed
        assert test_set.iloc[0].datetime == '2021-01-26 01:15:00'


