from niav.testcase import TestCase
from niav.env import Env
from niav.utils import Utils
from niav.http import Http

from .helpers.template.template import ApiHello


class TestTemplate(TestCase):

    # running before tests
    def setUp(self):
        self.env = Env(__file__)
        self.url = "%s://%s:%s" % (
            self.env.get("api_to_test.protocol"),
            self.env.get("api_to_test.host"),
            self.env.get("api_to_test.port"))
        self.http = Http()

    # running after all tests
    def tearDown(self):
        pass

    # one test
    def test_template_01(self):
        api_hello = ApiHello("John")
        res = api_hello.hello()
        Utils.pprint(res)

        payload = {
            "name": res["name"]
        }
        url = "%s/user/register" % self.url
        r = self.http.post(url, data=payload)
        self.assertEqual(r.status_code, 200)

