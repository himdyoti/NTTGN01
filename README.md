# Network Automation

Network automation assignment project using Python, Flask, Cisshgo .

  - Using Python to connect securely in realtime to a dummy SSH server(Cisshgo).
  - Executing command in the SSH server and getting output back.
  - Parsing The output to specified JSON format.
  - Serving output on a REST Api call.

# Rest Api Endpoints

  - http://127.0.0.1:5000/get_all_interfaces
  - http://127.0.0.1:5000/get_interface?interface=interface_name
  - http://127.0.0.1:5000/get_interface_htm

# Running Server

 - Project Layout

```
src
├── api_handler.py
├── base
│   ├── config.py
│   ├── __init__.py
│   └── utils.py
├── __init__.py
├── interfaces.json
├── show_running-config.txt
├── ssh_app.py
├── ssh_dev_conn.py
├── static
│   ├── css
│   │   └── tree.css
│   └── js
│       └── jquery3.5.1.min.js
├── templates
│   └── index.html
└── test
    ├── __init__.py
    ├── sample.json
    ├── show_running-config.txt
    └── test_api_handler.py

```
 - To start the development server

```
python ssh_app.py
```
# Api Output


  - http://127.0.0.1:5000/get_interface?interface=FastEthernet3/0

```json
{
  "interface": "FastEthernet3/0",
  "ip_address": "172.16.2.1",
  "subnet": "255.255.255.0",
  "description": "This is an assignment",
  "duplex": "",
  "speed": ""
}
```

- http://127.0.0.1:5000/get_all_interfaces

```json
[
  {
    "interface": "FastEthernet0/0",
    "ip_address": "10.0.2.27",
    "subnet": "255.255.255.0",
    "description": "netpalm",
    "duplex": "auto",
    "speed": "auto"
  },
  {
    "interface": "Serial0/0",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet0/1",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "auto",
    "speed": "auto"
  },
  {
    "interface": "Serial0/1",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet1/0",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "auto",
    "speed": "auto"
  },
  {
    "interface": "FastEthernet2/0",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "auto",
    "speed": "auto"
  },
  {
    "interface": "FastEthernet3/0",
    "ip_address": "172.16.2.1",
    "subnet": "255.255.255.0",
    "description": "This is an assignment",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/1",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/2",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/3",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/4",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/5",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/6",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/7",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/8",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/9",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/10",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/11",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/12",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/13",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/14",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/15",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "Vlan1",
    "ip_address": "",
    "subnet": "",
    "description": "",
    "duplex": "",
    "speed": ""
  }
]

```
 - http://127.0.0.1:5000/get_interface_htm

 ```
HTML form to get a specific interface details.
 ```
