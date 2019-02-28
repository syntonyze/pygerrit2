from pygerrit2 import GerritRestAPI, HTTPBasicAuthFromNetrc
import logging

if __name__ == '__main__':
    logging.getLogger("pygerrit2").setLevel(logging.DEBUG)
    url = "http://localhost:8080"
    auth = HTTPBasicAuthFromNetrc(url=url)
    api = GerritRestAPI(url=url, auth=auth)
    changeinput = {"project": "test-project",
                   "subject": "subject",
                   "branch": "master"}
    result = api.post("/changes/", json=changeinput)
    change_id = result["id"]
    content = """{"foo" : "bar"}"""
    api.put("/changes/" + change_id + "/edit/file.json",
            data=content)
