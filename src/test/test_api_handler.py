import unittest
import json
import sys
from collections import OrderedDict
sys.path.append("../")
from ssh_dev_conn import parse_interface_data


with open("show_running-config.txt") as fd:
    cmd_outp = fd.read()
with open("sample.json") as fd:
    expected = json.load(fd, object_pairs_hook=OrderedDict)


class TestDevConn(unittest.TestCase):

    def test_parse_interface_data(self):
        parsed_data = parse_interface_data(cmd_outp)
        for expect, outpd in zip(expected, parsed_data):
            if expect != outpd:
                print(expect, outpd)
            assert expect == outpd

    def test_handler_get_interfaces(self):
        pass


if __name__ == '__main__':
    unittest.main()
