# Network Automation

Network automation assignment project using Python, Flask, Cisshgo .

  - Using Python to connect securely in realtime to a dummy SSH server(Cisshgo).
  - Executing command in the SSH server and getting output back.
  - Parsing The output to specified JSON format.
  - Serving output on a REST Api call.

# Rest Api Endpoints

  - http://127.0.0.1:5000/get_all_interfaces
  - http://127.0.0.1:5000/get_interface?interface=interface_name


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
    "description": "netpalm",
    "duplex": "auto",
    "interface": "FastEthernet0/0",
    "ip_address": "10.0.2.27 255.255.255.0",
    "speed": "auto",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "Serial0/0",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "auto",
    "interface": "FastEthernet0/1",
    "ip_address": "",
    "speed": "auto",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "Serial0/1",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "auto",
    "interface": "FastEthernet1/0",
    "ip_address": "",
    "speed": "auto",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "auto",
    "interface": "FastEthernet2/0",
    "ip_address": "",
    "speed": "auto",
    "subnet": ""
  },
  {
    "description": "This is an assignment",
    "duplex": "",
    "interface": "FastEthernet3/0",
    "ip_address": "172.16.2.1 255.255.255.0",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/1",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/2",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/3",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/4",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/5",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/6",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/7",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/8",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/9",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/10",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/11",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/12",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/13",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/14",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "FastEthernet3/15",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "This is an assignment",
    "duplex": "",
    "interface": "FastEthernet3/20",
    "ip_address": "172.16.2.22 255.255.255.0",
    "speed": "",
    "subnet": ""
  },
  {
    "description": "",
    "duplex": "",
    "interface": "Vlan1",
    "ip_address": "",
    "speed": "",
    "subnet": ""
  }
]
```
