# @Author: DennisShaw
# @Email: cyan.lab.ai@gmail.com
import re
from .base_parser import BaseParser

class NatParser(BaseParser):
    def parse(self, lines):
        full_nat, port_nat = {}, {}

        for line in lines:
            line = line.strip()
            # Note: The actual format may vary depending on device configuration rules. Adjust the regex accordingly.
            full_match = re.match(
                r'nat inside source static (\S+)  (\S+)', line)
            if full_match:
                internal_ip, external_ip = full_match.groups()
                full_nat[external_ip] = internal_ip
                continue

            port_match = re.match(
                r'nat inside protocol (\S+) (\d+) (\S+) (\d+)', line)
            if port_match:
                proto, ext_ip, ext_port, int_ip, int_port = port_match.groups()
                key = f"{ext_ip}:{ext_port}/{proto.lower()}"
                port_nat[key] = f"{int_ip}:{int_port}"

        return {'full_nat': full_nat, 'port_nat': port_nat}