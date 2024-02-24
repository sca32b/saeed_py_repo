import os
#from replit import clear

class BreakAllLoops(Exception): pass


def clear_screen():
    os.system('cls')

# AWS Infrastructure
aws_instance_types_regular = {"t2.micro": {"vcpu": 1, "memory": 1, "storage": "EBS-Only", "network": "Low to Moderate"}, "t2.small": {"vcpu": 1, "memory": 2, "storage": "EBS-Only", "network": "Low to Moderate"}, "t2.medium": {"vcpu": 2, "memory": 4, "storage": "EBS-Only", "network": "Low to Moderate"}, "t2.large": {"vcpu": 2, "memory": 8, "storage": "EBS-Only", "network": "Low to Moderate"}, "t2.xlarge": {"vcpu": 4, "memory": 16, "storage": "EBS-Only", "network": "Low to Moderate"}, "t2.2xlarge": {"vcpu": 8, "memory": 32, "storage": "EBS-Only", "network": "Low to Moderate"}, "m4.large": {"vcpu": 2, "memory": 8, "storage": "EBS-Only", "network": "Moderate"}, "m4.xlarge": {"vcpu": 4, "memory": 16, "storage": "EBS-Only", "network": "High"}, "m4.2xlarge": {"vcpu": 8, "memory": 32, "storage": "EBS-Only", "network": "High"}, "m4.4xlarge": {"vcpu": 16, "memory": 64, "storage": "EBS-Only", "network": "High"}, "m4.10xlarge": {"vcpu": 40, "memory": 160, "storage": "EBS-Only", "network": "10 Gigabit"}, "m4.16xlarge": {"vcpu": 64, "memory": 256, "storage": "EBS-Only", "network": "20 Gigabit"}, "m5.large": {"vcpu": 2, "memory": 8, "storage": "EBS-Only", "network": "Moderate"}, "m5.xlarge": {"vcpu": 4, "memory": 16, "storage": "EBS-Only", "network": "High"} }

aws_ebs_types = {"gp2": {"volume_type": "General Purpose SSD", "iops": "3 IOPS per GB", "throughput": "128 MiB/s to 250 MiB/s", "latency": "3-4 ms"}, "io1": {"volume_type": "Provisioned IOPS SSD", "iops": "Up to 64,000 IOPS", "throughput": "Up to 1,000 MiB/s", "latency": "Less than 1 ms"}, "st1": {"volume_type": "Throughput Optimized HDD", "iops": "500 IOPS", "throughput": "40 MiB/s to 500 MiB/s", "latency": "Less than 20 ms"}, "sc1": {"volume_type": "Cold HDD", "iops": "250 IOPS", "throughput": "12 MiB/s to 250 MiB/s", "latency": "Less than 20 ms"}, "standard": {"volume_type": "Magnetic", "iops": "40-200 IOPS", "throughput": "40-90 MiB/s", "latency": "Less than 20 ms"} }

aws_s3_types = {"s3standard": {"storage_class": "Standard"}, "s3intelligent_tiering": {"storage_class": "Intelligent-Tiering"}, "s3standard_ia": {"storage_class": "Standard-Infrequent Access"}, "s3onezone_ia": {"storage_class": "One Zone-Infrequent Access"}, "s3glacier": {"storage_class": "Glacier"}, "s3glacier_deep_archive": {"storage_class": "Glacier Deep Archive"}}


print(aws_instance_types_regular["t2.micro"]["storage"])

# GCP Infrastructure 
gcp_instance_types = {
    "e2-micro": {"vcpu": 2, "memory": 1, "storage": "Ephemeral SSD", "network": "Moderate"},
    "e2-small": {"vcpu": 2, "memory": 2, "storage": "Ephemeral SSD", "network": "Moderate"},
    "e2-medium": {"vcpu": 2, "memory": 4, "storage": "Ephemeral SSD", "network": "Moderate"},
    "n1-standard-1": {"vcpu": 1, "memory": 3.75, "storage": "Ephemeral SSD", "network": "High"},
    "n1-standard-2": {"vcpu": 2, "memory": 7.5, "storage": "Ephemeral SSD", "network": "High"},
    "n1-standard-4": {"vcpu": 4, "memory": 15, "storage": "Ephemeral SSD", "network": "High"},
    "n1-standard-8": {"vcpu": 8, "memory": 30, "storage": "Ephemeral SSD", "network": "High"},
    "n1-standard-16": {"vcpu": 16, "memory": 60, "storage": "Ephemeral SSD", "network": "High to Very High"},
    "n1-standard-32": {"vcpu": 32, "memory": 120, "storage": "Ephemeral SSD", "network": "High to Very High"},
    "n1-standard-64": {"vcpu": 64, "memory": 240, "storage": "Ephemeral SSD", "network": "High to Very High"},
    "n1-highmem-2": {"vcpu": 2, "memory": 13, "storage": "Ephemeral SSD", "network": "High"},
    "n1-highmem-4": {"vcpu": 4, "memory": 26, "storage": "Ephemeral SSD", "network": "High"},
    "n1-highmem-8": {"vcpu": 8, "memory": 52, "storage": "Ephemeral SSD", "network": "High to Very High"},
    "n1-highmem-16": {"vcpu": 16, "memory": 104, "storage": "Ephemeral SSD", "network": "High to Very High"},
}

# Note on Storage: GCP instances use either local SSDs (ephemeral) or Persistent Disks. "EBS-Only" in AWS is closest to using Persistent Disks in GCP.
# Note on Network: GCP's network performance categories are not directly comparable to AWS's. The classifications provided are approximations.

gcp_disk_types = {
    "pd-standard": {
        "volume_type": "Standard Persistent Disk",
        "iops": "Depends on volume size",
        "throughput": "Up to 180 MiB/s",
        "latency": "Typical latency"
    },
    "pd-balanced": {
        "volume_type": "Balanced Persistent Disk",
        "iops": "3 IOPS per GB, up to 10,000 IOPS",
        "throughput": "Up to 240 MiB/s",
        "latency": "Lower latency than pd-standard"
    },
    "pd-ssd": {
        "volume_type": "SSD Persistent Disk",
        "iops": "30 IOPS per GB, up to 100,000 IOPS",
        "throughput": "Up to 1,200 MiB/s",
        "latency": "Lower latency than pd-balanced"
    },
    "pd-extreme": {
        "volume_type": "Extreme Persistent Disk",
        "iops": "Up to 160,000 read IOPS and 120,000 write IOPS",
        "throughput": "Up to 2,400 MiB/s",
        "latency": "Lowest latency for Persistent Disks"
    }
}

# Note: GCP does not have direct equivalents to AWS's "Throughput Optimized HDD" (st1) and "Cold HDD" (sc1) for lower-cost, high-throughput, and less frequently accessed workloads. For these use cases, consider balancing cost and performance requirements with the available disk types or look into file storage options like Google Cloud Storage for 

gcp_storage_classes = {
    "standard": {
        "storage_class": "Standard",
        "description": "For frequently accessed data that needs to be retrieved quickly."
    },
    "nearline": {
        "storage_class": "Nearline",
        "description": "For data that is accessed less frequently, but requires rapid access when needed."
    },
    "coldline": {
        "storage_class": "Coldline",
        "description": "For data that is accessed infrequently and can tolerate slightly higher latency for retrieval."
    },
    "archive": {
        "storage_class": "Archive",
        "description": "For long-term storage of data that is accessed very infrequently and can tolerate high latency for retrieval."
    }
}

# Note: Google Cloud Storage does not have a direct equivalent to AWS's "Intelligent-Tiering" which automatically moves data between access tiers based on access patterns.

def addClient(clients, name, employees):
    clients.append({"name": name, "employees": employees})


clients = [
    {"name": "Numerix", "employees": 300}
]
response = 'y'
while response == 'y':
    company = input("\nEnter the name of the company you want to add to the list of clients: ")
    employees = int(input("Enter the number of employees at the company: "))
    addClient(clients, company, employees)
    print(clients)
    print(f"\n{company} has been added to the list of clients.")
    print(f"Total number of clients: {len(clients)}")
    response = input("\nDo you want to add another client? (y/n): ")


cloud_providers = {"aws": "aws_infrastructure", "azure": "azure_infrastructure", "gcp": "gcp_infrastructure"}

aws_infrastructure = {}
aws_infrastructure["compute"] = aws_instance_types_regular
aws_infrastructure["storage-ebs"] = aws_ebs_types
aws_infrastructure["storage-s3"] = aws_s3_types

gcp_infrastructure = {}
gcp_infrastructure["compute"] = gcp_instance_types
gcp_infrastructure["storage-pd"] = gcp_disk_types
gcp_infrastructure["storage-gcs"] = gcp_storage_classes
first_time = True
try:
    while True:
        if first_time:
            first_time = False
        else:
            print("\nPress Enter to continue...\n")
            response = input()
        clear_screen()
        print("\n****Welcome to the GCO cloud infrastructure deployment tool***\n****************************************\n")
        cloud_providers = input("\nEnter the cloud provider you want to deploy infrastructure - (a)ws, (g)cp, (az)ure and (q)uit:")
        if cloud_providers == "q":
            raise BreakAllLoops
        choice = input("\nEnter the infrstructure type you want to deploy - (c)ompute, (s)torage-(e)bs, (s)torage-(s)3 and (q)uit:")
        if cloud_providers == "a":
            match choice:
                case "c":
                    print(aws_infrastructure["compute"])
                case "se":
                    print(aws_infrastructure["storage-ebs"])
                case "ss":
                    print(aws_infrastructure["storage-s3"])
                case "q":
                    raise BreakAllLoops
                case _:
                    print("Invalid choice of infrastructure type")
        elif cloud_providers == "g":
            match choice:
                case "c":
                    print(gcp_infrastructure["compute"])
                case "se":
                    print(gcp_infrastructure["storage-pd"])
                case "ss":
                    print(gcp_infrastructure["storage-gcs"])
                case "q":
                    raise BreakAllLoops
                case _:
                    print("Invalid choice of infrastructure type")
        elif cloud_providers == "az":
            print("Azure infrastructure not available")
        elif cloud_providers == "q":
            raise BreakAllLoops
except BreakAllLoops:
    pass

for client in clients:
    print(f"\nName: {client['name']} : Employees: {client['employees']}")