# @Author: DennisShaw
# @Email: cyan.lab.ai@gmail.com
from config_parser import NatParser, SlbParser
from utils import read_config
from mapping_finder import MappingFinder

def main():
    nat_configs = read_config('./data/NAT_Config_Folder/')
    slb_configs = read_config('./data/SLB_Config_Folder/')

    nat_parser = NatParser()
    slb_parser = SlbParser()

    nat_data = nat_parser.parse(nat_configs)
    slb_data = slb_parser.parse(slb_configs)

    finder = MappingFinder(nat_data, slb_data)

    queries = ["36.***.***.133:443", "36.***.***.66:49000"]
    for q in queries:
        result = finder.find_mapping(q)
        print(result)

if __name__ == "__main__":
    main()
