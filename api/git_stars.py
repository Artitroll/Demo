import allure
import requests

class GitStars:

    def __init__(self):
        pass

    @allure.step("Get {project} stargazers")
    def get_stargazers(self, project, per_page, timestamps: bool):
        if timestamps:
            accept = "application/vnd.github.star+json"
        else:
            accept = "application/vnd.github+json"
        response = requests.get(
            f"https://api.github.com/repos/{project}/stargazers",
            params={"per_page": f"{per_page}"},
            headers={"Accept": f"{accept}", "X-GitHub-Api-Version": "2022-11-28"},
        )
        return response.json()

    @allure.step("Put star on {project}")
    def put_star(self, project, user_token):
        response = requests.put(
            f"https://api.github.com/user/starred/{project}",
            headers={"Accept" : "application/vnd.github+json", "Authorization": f"Bearer {user_token}", "X-GitHub-Api-Version": "2022-11-28"},
        )
        return response.status_code

    @allure.step("Get if star is already on {project}")
    def get_star(self, project, user_token):
        response = requests.get(
            f"https://api.github.com/user/starred/{project}",
            headers={"Accept" : "application/vnd.github+json", "Authorization": f"Bearer {user_token}", "X-GitHub-Api-Version": "2022-11-28"},
        )
        return response.status_code

    @allure.step("Delete star already on {project}")
    def delete_star(self, project, user_token):
        response = requests.delete(
            f"https://api.github.com/user/starred/{project}",
            headers={"Accept" : "application/vnd.github+json", "Authorization": f"Bearer {user_token}", "X-GitHub-Api-Version": "2022-11-28"},
        )
        print(response)
        return response.status_code