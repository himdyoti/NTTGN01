"""
module to securely connect devices using paramiko
"""
import time
import json
from collections import OrderedDict
from netmiko import ConnectHandler
from base.utils import patt, patt2
from base.config import Device_List, Cfg_Timeouts, Conv_Dict


def get_interfaces(conn_config, cmds=None):
    """
    connects to remote ssh server and gets interface details as plain text.
    """
    output = ""

    if cmds is None:
        cmds = ["ls"]
    try:
        conn = ConnectHandler(**conn_config)
        output = conn.send_command(cmds[0])
    except Exception as ex_obj:
        print(ex_obj)

    if len(output) < 5:
        with open("show_running-config.txt") as fdr:
            output = fdr.read()
    return output


def save_data_json(data, fpath="interfaces.json"):
    """
    save python dictionary to a json file
    """
    with open(fpath, "w") as fdo:
        return json.dump(data, fdo)


def parse_interface_data(data):
    """
    parse raw data into a python dictionary
    """
    interface_list = []
    for line_block in data.split("!"):
        line_block = line_block.strip()
        if line_block != "" and patt.match(line_block):
            default_d = {"interface": "", "description": "", "ip_address": "", "subnet": "", "duplex": "", "speed": ""}
            idct = OrderedDict(default_d)
            for m_obj in patt2.finditer(line_block):
                key = m_obj.group("key").strip()
                key = Conv_Dict.get(key, key)
                val = m_obj.group("val").strip().strip('"')
                if key == b"ip_address":
                    ip_addr, *netmask = val.split()
                    idct["ip_address"] = ip_addr
                    idct["subnet"] = netmask[0] if len(netmask) > 0 else ""
                    continue
                idct[key] = val
            interface_list.append(idct)
    print(interface_list)
    return interface_list


def main_batch(conn_config):
    """
    running all functions
    """
    cmds = ["show running-config\n"]
    data = get_interfaces(conn_config, cmds)
    parsed_data = parse_interface_data(data)
    #print(parsed_data)
    save_data_json(parsed_data, fpath="interfaces.json")


if __name__ == "__main__":
    conn_config = Device_List["machine2"]
    main_batch(conn_config)
