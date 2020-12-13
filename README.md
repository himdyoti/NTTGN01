# Network Automation

Network automation assignment project using Python, Flask, Cisshgo .

  - Using Python to connect securely in realtime to a dummy SSH server(Cisshgo).
  - Executing command in the SSH server and getting output back.
  - Parsing The output to specified JSON format.
  - Serving output on a REST Api call.

# Rest Api Endpoints

  - http://127.0.0.1:5000/get_all_interfaces
  - http://127.0.0.1:5000/get_interface?interface=interface_name

# Running Server

 - Directory structure

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
│   └── html
│       └── tree.html
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
  "description": "This is an assignment",
  "duplex": "",
  "interface": "FastEthernet3/0",
  "ip_address": "172.16.2.1 255.255.255.0",
  "speed": "",
  "subnet": ""
}
```

- http://127.0.0.1:5000/get_all_interfaces

```json
[
  {
    "interface": "FastEthernet0/0",
    "description": "netpalm",
    "ip_address": "10.0.2.27",
    "subnet": "255.255.255.0",
    "duplex": "auto",
    "speed": "auto"
  },
  {
    "interface": "Serial0/0",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet0/1",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "auto",
    "speed": "auto"
  },
  {
    "interface": "Serial0/1",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet1/0",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "auto",
    "speed": "auto"
  },
  {
    "interface": "FastEthernet2/0",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "auto",
    "speed": "auto"
  },
  {
    "interface": "FastEthernet3/0",
    "description": "This is an assignment",
    "ip_address": "172.16.2.1",
    "subnet": "255.255.255.0",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/1",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/2",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/3",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/4",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/5",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/6",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/7",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/8",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/9",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/10",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/11",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/12",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/13",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/14",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "FastEthernet3/15",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  },
  {
    "interface": "Vlan1",
    "description": "",
    "ip_address": "",
    "subnet": "",
    "duplex": "",
    "speed": ""
  }
]

```
