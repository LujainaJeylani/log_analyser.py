import re
import pandas as pd
import matplotlib.pyplot as plt

def get_ip(log):  #Get IP addresses
    with open(log, 'r') as file:
        lines = file.readlines()

    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ip_list = []
    for line in lines:
        match = re.search(ip_pattern, line)
        if match:
            ip_list.append(match.group())
    
    table = pd.DataFrame({"IP": ip_list})
    return table

def frequency(ip_table):
    ip_counts = ip_table["IP"].value_counts()
    print("Top 10 Most Frequent IPs:\n")
    print(ip_counts.head(10))
    print("\n10 Least Frequent IPs:\n")
    print(ip_counts.tail(10))

    #Error handling
    if len(ip_counts) >= 10:
        bottom = ip_counts.tail(5)
        top = ip_counts.head(5)
        combined = pd.concat([top, bottom])
        plt.figure()
        plt.bar(combined.index, combined.values, color=['blue']*5 + ['red']*5)
        plt.xlabel("IP Address")
        plt.ylabel("Number of Appearances")
        plt.title("IP Address Frequency")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("Not enough unique IPs to plot top and bottom 5.")




# Applying your file
file_path = "OpenSSH_2k.log"  # Change this to your actual file
ip_data = get_ip(file_path)
frequency(ip_data)
