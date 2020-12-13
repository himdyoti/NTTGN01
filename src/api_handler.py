from ssh_dev_conn import get_interfaces, parse_interface_data
from base.config import Device_List


def handler_get_interface(iname):
    conn_config = Device_List["machine1"]
    iface_obj = {}
    raw_data = get_interfaces(conn_config)
    parsed_data = parse_interface_data(raw_data)
    for data in parsed_data:
        if data.get("interface", "") == iname:
            iface_obj = data
    return iface_obj


def handler_get_interfaces():
    conn_config = Device_List["machine1"]
    raw_data = get_interfaces(conn_config)
    parsed_data = parse_interface_data(raw_data)
    return parsed_data
