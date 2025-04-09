# @Author: DennisShaw
# @Email: cyan.lab.ai@gmail.com
class MappingFinder:
    def __init__(self, nat_data, slb_data):
        self.nat_data = nat_data
        self.slb_data = slb_data

    def find_nat(self, query):
        ip_port, _, protocol = query.partition('/')
        protocol = protocol or 'tcp'
        ip, port = ip_port.split(':')
        key = f"{ip}:{port}/{protocol}"

        if key in self.nat_data['port_nat']:
            return self.nat_data['port_nat'][key]

        if ip in self.nat_data['full_nat']:
            return f"{self.nat_data['full_nat'][ip]}:{port}"
        return None

    def find_slb(self, query_ip_port):
        ip, port = query_ip_port.split(':')

        for vid, vip in self.slb_data['virtual'].items():
            if vip['ip'] == ip and vip['port'] == port:
                pid = self.slb_data['policy'].get(vid)
                gid = self.slb_data['group'].get(pid)
                rip = self.slb_data['real'].get(gid)
                if rip:
                    return f"{rip['ip']}:{rip['port']}"
        return None

    def find_mapping(self, query):
        nat_result = self.find_nat(query)
        if not nat_result:
            return f"{query} Not Find Mapping"

        slb_result = self.find_slb(nat_result)
        if slb_result:
            return f"{query} → {nat_result}(NAT) → {slb_result}(SLB)"
        else:
            return f"{query} → {nat_result}(NAT)"
