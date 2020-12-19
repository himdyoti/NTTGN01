"""
module to securely connect devices using netmiko
"""
import json
from collections import OrderedDict
from netmiko import ConnectHandler
from base.utils import patt2
from base.config import Device_List, Conv_Dict


def get_interfaces(conn_config, cmds=None):
    """
    connects to remote ssh server and gets interface details as plain text.
    """
    output = ""
    conn = None

    if cmds is None:
        cmds = ["ls"]
    try:
        conn = ConnectHandler(**conn_config)
        output = conn.send_command(cmds[0])
    except Exception as ex_obj:
        print(ex_obj)
    finally:
        if conn is not None:
            conn.cleanup()
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
        if line_block != "" and line_block.find("interface") != -1:
            dict_order = {"interface": "", "ip_address": "", "subnet": "", "description": "", "duplex": "", "speed": ""}
            idct = OrderedDict(dict_order)
            for m_obj in patt2.finditer(line_block):
                key = m_obj.group("key").strip()
                key = Conv_Dict.get(key, key)
                val = m_obj.group("val").strip().strip('"')
                if key == "ip_address":
                    ip_addr, *netmask = val.split()
                    idct["ip_address"] = ip_addr
                    idct["subnet"] = netmask[0] if len(netmask) > 0 else ""
                    continue
                idct[key] = val
            interface_list.append(idct)
    return interface_list


def main_batch(conn_config):
    """
    running all functions
    """
    cmds = ["show running-config"]
    data = get_interfaces(conn_config, cmds)
    parsed_data = parse_interface_data(data)
    save_data_json(parsed_data, fpath="interfaces.json")


if __name__ == "__main__":
    conn_config = Device_List["machine2"]
    main_batch(conn_config)
