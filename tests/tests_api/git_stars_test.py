import json

import allure
import pytest
from jsonschema import validate

from api.git_stars import GitStars


class TestGitStars:

    @pytest.fixture(autouse=True)
    def prepare_api(self):
        self.api =  GitStars()

    @allure.tag("api")
    @allure.title("Test for get on stargazers, validating dates")
    def test_get_stars(self):
        resp = self.api.get_stargazers("termux/termux-packages",10, True)
        with open("./json/stargazers_schema") as file:
            schema = json.load(file)
            validate(resp, schema)

    @allure.title("Test for put star on project, validating if checked")
    def test_add_star(self):
        return_code = self.api.put_star("bleedline/aimoneyhunter", "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")
        assert return_code == 204
        return_code = self.api.get_star("bleedline/aimoneyhunter", "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")
        assert return_code == 204
        #В курсе что можно вынести все удаления на после yield фикстуры, но для 1-2 кейсов не стал.
        return_code = self.api.delete_star("bleedline/aimoneyhunter", "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")
        assert return_code == 204

    @allure.title("Test for negative scenarios")
    def test_negative(self):
        return_code = self.api.get_star("ScoodfsgfdpInstaller/Extras", "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")
        assert return_code == 404
        return_code = self.api.get_star("ScoopInstaller/Extras", "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s")
        assert return_code == 401
