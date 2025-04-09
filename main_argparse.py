# @Author: DennisShaw
# @Email: cyan.lab.ai@gmail.com
import argparse
from config_parser import NatParser, SlbParser
from utils import read_config
from mapping_finder import MappingFinder

def main():
    parser = argparse.ArgumentParser(description="NetReveal - IP Mapping Finder")
    parser.add_argument('--nat-config', type=str, required=True, help='Path to the NAT configuration file')
    parser.add_argument('--slb-config', type=str, required=True, help='Path to the SLB configuration file')
    parser.add_argument('--query', type=str, required=True, nargs='+', help='IP and port to query (format: IP:PORT, e.g., 36.***.***.133:443)')

    args = parser.parse_args()

    nat_configs = read_config(args.nat_config)
    slb_configs = read_config(args.slb_config)

    nat_parser = NatParser()
    slb_parser = SlbParser()

    nat_data = nat_parser.parse(nat_configs)
    slb_data = slb_parser.parse(slb_configs)

    finder = MappingFinder(nat_data, slb_data)

    for q in args.query:
        result = finder.find_mapping(q)
        print(result)

if __name__ == "__main__":
    main()