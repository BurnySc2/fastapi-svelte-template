from seleniumbase import BaseCase
# see https://github.com/seleniumbase/SeleniumBase

import subprocess
import time
import os
import signal
from typing import Optional


class MyTestClass(BaseCase):
    webserver_process: Optional[subprocess.Popen] = None

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        # pylint: disable=R1732
        MyTestClass.webserver_process = subprocess.Popen(["npm", "run", "dev"])
        # MyTestClass.webserver_process = subprocess.Popen(["npx", "webpack", "serve"])
        time.sleep(5)

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        if MyTestClass.webserver_process is not None:
            time.sleep(0.1)
            os.kill(MyTestClass.webserver_process.pid, signal.SIGTERM)
            time.sleep(0.1)
            if MyTestClass.webserver_process.poll() is None:
                os.kill(MyTestClass.webserver_process.pid, signal.SIGKILL)

        MyTestClass.webserver_process = None

    def test_basic_site_display(self):
        """ Check if HOME site is visible """
        self.open("http://localhost:8080")
        self.assert_text("Hello world!")

    def test_shows_todos(self):
        """ Check if the to-do site is visible """
        self.open("http://localhost:8080")
        self.assert_text("Hello world!")
        self.click("#todo")
        self.assert_text("Unable to connect to server")

    def test_add_todo(self):
        """ Add a new to-do entry """
        self.open("http://localhost:8080")
        self.click("#todo")
        test_text = "my amazing test todo text"
        self.write("#newTodoInput", test_text)
        self.click("#submit1")
        self.assert_text(test_text)

    def test_example(self):
        url = "https://store.xkcd.com/collections/posters"
        # Go to url
        self.open(url)
        # Type in input field "xkcd book"
        self.type('input[name="q"]', "xkcd book")
        # Click the search icon to start searching
        self.click('input[value="Search"]')
        # Assert that there is a header with class "h3" which has text: "xkcd: volume 0"
        self.assert_text("xkcd: volume 0", "h3")
        # Go to new url
        self.open("https://xkcd.com/353/")
        self.assert_title("xkcd: Python")
        self.assert_element('img[alt="Python"]')
        # Click on <a> element with rel="license"
        self.click('a[rel="license"]')
        # Assert that there is this text on the website visible
        self.assert_text("free to copy and reuse")
        # Click go_back
        self.go_back()
        # Click the "About" link
        self.click_link("About")
        # Assert that there is a header with class "h2" which has text: "xkcd.com"
        self.assert_exact_text("xkcd.com", "h2")
