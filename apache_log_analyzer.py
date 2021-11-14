import sys
def get_totals(file: str) -> dict:
    """
    Reads in Apache log file path and parses
    number of requests/day and number of
    requests/IP returned as a dict.
    
    Args:
        file (string): Apache access.log file path

    Returns:
        dict: Dictionary of dictionaries containing ips/days as keys.
    """
    ip_dict = {}
    day_dict = {}
    with open('{}'.format(file)) as f:
        for line in f:
            split = line.split(' ')
            if ip_dict.get(split[0], None) and day_dict.get(split[3][1:12],None):
                ip_dict[split[0]] += 1
                day_dict[split[3][1:12]] += 1
            if day_dict.get(split[3][1:12],None):
                day_dict[split[3][1:12]] += 1
            if ip_dict.get(split[0], None):
                ip_dict[split[0]] += 1
            else:
                ip_dict[split[0]] = 1
                day_dict[split[3][1:12]] = 1
    return {
        "ips": ip_dict,
        "days": day_dict
    }
    
def write_totals(file: str, totals: dict):
    """
    Writes dictionary day and IP totals to
    provided file path.

    Args:
        file (str): Destination file path
        totals (dict): Totals as computed by get_totals
    """
    with open('{}'.format(file), 'w') as f:
        f.write("############ DAYS ############\n")
        for day in totals["days"]:
            f.write("{}: {}\n".format(day, totals["days"][day]))
        f.write("############ IPS ############\n")
        for ip in totals["ips"]:
            f.write("{}: {}\n".format(ip, totals["ips"][ip]))

    
if __name__ == '__main__':
    totals = get_totals(sys.argv[1])
    write_totals(sys.argv[2],totals)
            