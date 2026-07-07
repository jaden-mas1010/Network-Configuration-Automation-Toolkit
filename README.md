# 🌐 Network Automation Toolkit

A Python-based network automation toolkit that generates Cisco router and switch configurations using **Interactive**, **JSON**, and **Excel** workflows.

> 🚧 This project is actively being developed as I learn Python, networking, and network automation.

---

## ✨ Features

- Interactive CLI configuration generation
- JSON-based configuration generation
- Excel-to-JSON conversion
- Cisco Router interface configuration
- Cisco VLAN configuration
- Automatic configuration export
- Input validation (IP, subnet mask, VLAN ID)

---

## 🚀 Planned Features

- Static Route Generation
- OSPF Configuration
- ACL Configuration
- Inter-VLAN Routing
- Netmiko Deployment
- Jinja2 Templates
- Configuration Auditing
- Logging
- Unit Testing
- Support for Multiple Routers and Switches

---

## 📁 Project Structure

```text
network-automation-toolkit/
│
├── main.py
├── router.py
├── switch.py
├── routing.py
├── utils.py
├── excel_to_json.py
│
├── modes/
│   ├── interactive.py
│   ├── json_mode.py
│   └── excel_mode.py
│
├── configs/
│
├── network.json
├── company.xlsx
│
├── README.md
└── .gitignore
```

---

## 🖥️ Interactive Mode

The toolkit allows users to generate Cisco configurations through a command-line interface.

Example:

```text
Hostname: Branch1
Interface: GigabitEthernet0/0
IP Address: 192.168.1.1
Subnet Mask: 255.255.255.0
Description: ISP Connection

VLAN 10 - HR
VLAN 20 - Finance
```

---

## 📄 JSON Mode

Example `network.json`

```json
{
    "hostname": "Branch1",
    "interface": "GigabitEthernet0/0",
    "ip": "192.168.1.1",
    "mask": "255.255.255.0",
    "description": "ISP Connection",

    "vlans": [
        {
            "id": 10,
            "name": "HR"
        },
        {
            "id": 20,
            "name": "Finance"
        }
    ]
}
```

---

## 📊 Excel Mode

The toolkit can read network information from an Excel workbook.

### Routers Sheet

| Hostname | Interface | IP | Mask | Description |
|----------|-----------|----|------|-------------|
| Branch1 | GigabitEthernet0/0 | 192.168.1.1 | 255.255.255.0 | ISP |

### VLANs Sheet

| Hostname | VLAN ID | VLAN Name |
|----------|---------|-----------|
| Branch1 | 10 | HR |
| Branch1 | 20 | Finance |

---

## 📋 Example Output

```cisco
hostname Branch1

interface GigabitEthernet0/0
 description ISP Connection
 ip address 192.168.1.1 255.255.255.0
 no shutdown

vlan 10
 name HR

vlan 20
 name Finance
```

---

## 🛠️ Technologies Used

- Python
- OpenPyXL
- JSON
- Cisco IOS
- Git
- GitHub

---

## 📚 What I Learned

This project helped me practice:

- Python Modules
- Functions
- Loops
- Dictionaries
- Lists
- File Handling
- JSON Processing
- Excel Automation
- Cisco Network Configuration
- Python Project Structure

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/network-automation-toolkit.git
```

Move into the project directory:

```bash
cd network-automation-toolkit
```

Install the required package:

```bash
pip install openpyxl
```

Run the application:

```bash
py main.py
```

---

## 📌 Future Improvements

- Deploy configurations directly to Cisco devices using Netmiko
- Generate configurations using Jinja2 templates
- Support multiple routers and switches
- Build a graphical interface
- Add automated tests

---



---

## ⭐ If you found this project interesting, consider giving it a star!
