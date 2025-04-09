# NetReveal - IP Mapping Finder

![license](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-green.svg)
![python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

A simple and user-friendly network device IP mapping analysis tool. It supports automatic parsing and mapping queries for various device configuration files, including firewall NAT and load balancer (SLB) configurations.

## ✨ Features

- Supports NAT mapping from firewall devices (full port mapping, port mapping).
- Supports IP mapping resolution for load balancer (SLB) devices.
- Easily extendable to support new types of network device configurations.
- Provides a unified IP mapping query interface to analyze the mapping path from public IPs to internal servers.

## 🛠 Project Structure

```
NetReveal/
├── config_parser/      # # Configuration file parsers
│   ├── __init__.py
│   ├── base_parser.py
│   ├── nat_parser.py
│   └── slb_parser.py
├── mapping_finder.py   # Core IP mapping logic
├── utils.py            # Utility functions
├── main.py             # Example usage and entry point
└── main_argparse.py    # Command-line entry point
```

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/Cyan-Lab-AI/NetReveal.git
cd NetReveal
```

### Dependencies

- Python 3.8+

### Usage

1. **Prepare Configuration Files**:

```bash
data/
├── NAT_Config_Folder/
│   ├── nat_config1.txt
│   └── nat_config2.txt
├── SLB_Config_Folder/
│   ├── slb_config1.txt
│   └── slb_config2.txt
```

2. **Program Execution**:

### Program Interface

```bash
python main.py
```

### Command-line Interface

```bash
python main_argparse.py --nat-config <path_to_nat_config> --slb-config <path_to_slb_config> --query <IP:PORT> [<IP:PORT> ...]
```

### Example Output:

```bash
36.***.***.133:443 → 10.***.***.***:443(NAT) → 10.***.***.***:31500(SLB)
36.***.***.66:49000 → 10.***.***.139:49000(NAT)
```

## 📃 License

This project is licensed under the CC BY-NC-SA 4.0 license. See the LICENSE file for details.

## 📬 Contact

If you have any questions or suggestions, feel free to reach out:

- Email: cyan.lab.ai@gmail.com
- GitHub: [Cyan Lab](https://github.com/Cyan-Lab-AI)
