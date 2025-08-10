import os
print("Current directory:", os.getcwd())


import re  # For finding IP addresses using patterns
import pandas as pd  # For handling data like a spreadsheet
import matplotlib.pyplot as plt  # For drawing charts
import seaborn as sns  # For prettier charts

def get_ip_addresses(log_file):
    """Read a log file and pull out all the IP addresses."""
    with open(log_file, 'r') as file:
        lines = file.readlines()

    # This pattern matches IPv4 addresses like 192.168.1.1
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

    ip_list = []
    for line in lines:
        found = re.search(ip_pattern, line)
        if found:
            ip_list.append(found.group())

    # Turn the list into a table with one column called 'IP'
    return pd.DataFrame(ip_list, columns=["IP"])

def show_ip_stats(ip_table):
    """Show which IPs appear most and least, and draw a chart."""
    ip_counts = ip_table["IP"].value_counts()

    print("\n🔝 Top 10 Most Frequent IPs:")
    print(ip_counts.head(10))

    print("\n⬇️ Bottom 10 (Least Frequent) IPs:")
    print(ip_counts.tail(10))

    # Draw a chart showing how often each IP appears
    plt.figure(figsize=(12, 6))
    sns.histplot(ip_table["IP"], stat="count", palette="muted")
    plt.xticks(rotation=90)
    plt.title("📊 IP Address Frequency")
    plt.xlabel("IP Address")
    plt.ylabel("Number of Appearances")
    plt.tight_layout()
    plt.show()

# 🧪 Try it out
log_file_path = "log_toanalyse"  # Change this to your actual file
ip_data = get_ip_addresses(log_file_path)
show_ip_stats(ip_data)
