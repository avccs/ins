class Policy:
    def __init__(self, local_subnet, remote_subnet, mode, pfs, esp):
        self.local_subnet = local_subnet
        self.remote_subnet = remote_subnet
        self.mode = mode
        self.pfs = pfs
        self.esp = esp


class Connection:
    def __init__(self, local_ip, remote_ip):
        self.local_ip = local_ip
        self.remote_ip = remote_ip
        self.policies = []
        self.shared_secret = None

    def add_policy(self, policy):
        self.policies.append(policy)

    def set_psk(self, shared_secret):
        self.shared_secret = shared_secret

    def up(self):
        print("Starting the IPsec connection")
        print(f"Local IP: {self.local_ip}")
        print(f"Remote IP: {self.remote_ip}")
        for policy in self.policies:
            print("\nPolicy:")
            print(f"Local Subnet: {policy.local_subnet}")
            print(f"Remote Subnet: {policy.remote_subnet}")
            print(f"Mode: {policy.mode}")
            print(f"PFS: {policy.pfs}")
            print(f"ESP: {policy.esp}\n")
        print(f"Shared Secret: {self.shared_secret}")
        print("IPsec connection is up")


if __name__ == "__main__":
    local_ip = "192.168.1.1"
    remote_ip = "192.168.2.2"
    local_subnet = "10.0.0.0/24"
    remote_subnet = "10.0.1.0/24"
    shared_secret = "your_shared_secret_here"

    
    connection = Connection(local_ip, remote_ip)

    
    outbound_policy = Policy(local_subnet, remote_subnet, mode="tunnel", pfs="group14", esp="aes128-sha256")
    inbound_policy = Policy(remote_subnet, local_subnet, mode="tunnel", pfs="group14", esp="aes128-sha256")

    
    connection.add_policy(outbound_policy)
    connection.add_policy(inbound_policy)

    
    connection.set_psk(shared_secret)

    
    connection.up()


"""
OUTPUT:-
    Starting the IPsec connection
    Local IP: 192.168.1.1
    Remote IP: 192.168.2.2

    Policy:
    Local Subnet: 10.0.0.0/24
    Remote Subnet: 10.0.1.0/24
    Mode: tunnel
    PFS: group14
    ESP: aes128-sha256


    Policy:
    Local Subnet: 10.0.1.0/24
    Remote Subnet: 10.0.0.0/24
    Mode: tunnel
    PFS: group14
    ESP: aes128-sha256

    Shared Secret: your_shared_secret_here
    IPsec connection is up

"""