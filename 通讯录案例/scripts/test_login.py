import pytest
import yaml

from base.base_analyze import analyze_data


class TestLogin:

    @pytest.mark.parametrize("args", analyze_data("login_data.yaml", "test_login"))
    def test_login(self, args):
        age = args["age"]
        name = args["name"]
        height = args["height"]

        print(age)
        print(name)
        print(height)