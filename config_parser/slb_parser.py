# @Author: DennisShaw
# @Email: cyan.lab.ai@gmail.com
import re
from .base_parser import BaseParser

class SlbParser(BaseParser):
    def parse(self, lines):
        virtual, policy, group, real = {}, {}, {}, {}

        for line in lines:
            line = line.strip()
            # Note: The actual format may vary depending on device configuration rules. Adjust the regex accordingly.
            if (vm := re.match(r'slb virtual (\S+) (\S+)', line)):
                virtual[vm[1]] = {'ip': vm[2], 'port': vm[3]}
                continue

            if (pm := re.match(r'slb policy (\S+) (\S+)', line)):
                policy[pm[1]] = pm[2]
                continue

            if (gm := re.match(r'slb group (\S+) (\S+)', line)):
                group[gm[1]] = gm[2]
                continue

            if (rm := re.match(r'slb real (\S+) (\S+)', line)):
                real[rm[1]] = {'ip': rm[2], 'port': rm[3]}

        return {'virtual': virtual, 'policy': policy, 'group': group, 'real': real}