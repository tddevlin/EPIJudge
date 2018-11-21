from test_framework import generic_test


def get_valid_ip_address(s):
    ips = []
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                should_add = True
                if len(s[i+j+k:]) > 3 or len(s[i+j+k:]) == 0:
                    continue
                for part in [s[:i], s[i:i+j], s[i+j:i+j+k], s[i+j+k:]]:
                    if int(part) > 255:
                        should_add = False
                    if len(part) > 1 and part[0] == '0':
                        should_add = False
                if should_add:
                    ips.append('.'.join([s[:i], s[i:i+j], s[i+j:i+j+k], s[i+j+k:]]))
    return ips


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
