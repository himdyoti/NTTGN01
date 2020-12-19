from ssh_dev_conn import get_interfaces, parse_interface_data
from base.config import Device_List
from tabulate import tabulate


def handler_get_interface(iname):
    conn_config = Device_List["machine2"]
    iface_obj = {}
    cmds = ["show running-config"]
    raw_data = get_interfaces(conn_config, cmds)
    parsed_data = parse_interface_data(raw_data)
    for data in parsed_data:
        if data.get("interface", "") == iname:
            iface_obj = data
            print(tabulate([iface_obj], headers="keys", tablefmt="grid"))
    return iface_obj


def handler_get_interfaces():
    conn_config = Device_List["machine2"]
    cmds = ["show running-config"]
    raw_data = get_interfaces(conn_config, cmds)
    parsed_data = parse_interface_data(raw_data)
    if parsed_data:
        print(tabulate(parsed_data, headers="keys", tablefmt="grid"))
    return parsed_data
