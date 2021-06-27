from pytest_benchmark.fixture import BenchmarkFixture
from seleniumbase import BaseCase
# see https://github.com/seleniumbase/SeleniumBase
# https://seleniumbase.io/

import subprocess
import time
import os
import signal
from typing import Optional
import pytest

WEBSITE_ADDRESS = "http://localhost:8080"


class MyBaseCase(BaseCase):
    webserver_process: Optional[subprocess.Popen] = None

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        See https://docs.pytest.org/en/6.2.x/xunit_setup.html
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


class MyTestClass(MyBaseCase):
    def test_basic_site_display(self):
        """ Check if HOME site is visible """
        self.open(WEBSITE_ADDRESS)
        self.assert_text("Hello world!")

    def test_shows_todos(self):
        """ Check if the to-do site is visible """
        self.open(WEBSITE_ADDRESS)
        self.assert_text("Hello world!")
        self.click("#todo")
        self.assert_text("Unable to connect to server")

    def test_add_todo(self):
        """ Add a new to-do entry """
        self.open(WEBSITE_ADDRESS)
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


class MyBenchClass(MyBaseCase):
    def __init__(self):
        super().__init__()
        self.benchmark: Optional[BenchmarkFixture] = None

    @pytest.fixture(autouse=True)
    def setup_benchmark(self, benchmark):
        """
        Assign the benchmark to a class variable
        For more info see https://pytest-benchmark.readthedocs.io/en/latest/usage.html
        https://github.com/ionelmc/pytest-benchmark/blob/master/tests/test_with_testcase.py
        """
        self.benchmark = benchmark

    def basic_site_display(self):
        """ Check if HOME site is visible """
        self.open(WEBSITE_ADDRESS)
        self.assert_text("Hello world!")

    def test_bench_basic_site_display(self):
        """ Benchmark how fast the site loads """
        self.benchmark(self.basic_site_display)

    def add_todo(self):
        """ Add a new to-do entry """
        self.open(WEBSITE_ADDRESS)
        self.click("#todo")
        test_text = "my amazing test todo text"
        self.write("#newTodoInput", test_text)
        self.click("#submit1")
        self.assert_text(test_text)

    def test_bench_add_todo(self):
        """ Benchmark how fast a to-do can be added """
        self.benchmark(self.add_todo)
