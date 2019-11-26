# import pytest
# import yaml
#
#
# def analyze():
#     with open("./data/hello_data.yaml", "r") as f:
#         return yaml.load(f, Loader=yaml.FullLoader)
#
# class TestHello:
#
#     @pytest.mark.parametrize(("username", "password"), analyze())
#     def test_hello1(self, username, password):
#         print(username)
#         print(password)
#
#     @pytest.mark.parametrize(("username", "password"), analyze())
#     def test_hello2(self, username, password):
#         print(username)
#         print(password)
