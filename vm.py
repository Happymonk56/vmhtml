import subprocess

# Define VM parameters
vm_name = "Windows10VM"
os_type = "Windows10_64"
memory_size = "2048"  # in MB
cpu_count = "2"
iso_path = "/path/to/Windows10.iso"

# Create a new VM
create_vm_cmd = [
    "VBoxManage",
    "createvm",
    "--name", vm_name,
    "--ostype", os_type,
    "--register"
]
subprocess.run(create_vm_cmd, check=True)

# Configure VM settings
modify_vm_cmd = [
    "VBoxManage",
    "modifyvm", vm_name,
    "--memory", memory_size,
    "--cpus", cpu_count
]
subprocess.run(modify_vm_cmd, check=True)

# Add an IDE controller
add_controller_cmd = [
    "VBoxManage",
    "storagectl", vm_name,
    "--name", "IDE Controller",
    "--add", "ide"
]
subprocess.run(add_controller_cmd, check=True)

# Attach Windows 10 ISO
attach_iso_cmd = [
    "VBoxManage",
    "storageattach", vm_name,
    "--storagectl", "IDE Controller",
    "--port", "0",
    "--device", "0",
    "--type", "dvddrive",
    "--medium", iso_path
]
subprocess.run(attach_iso_cmd, check=True)

# Create and start the VM
create_vm_cmd = [
    "VBoxManage",
    "createvm",
    "--name", vm_name,
    "--ostype", os_type,
    "--register"
]
subprocess.run(create_vm_cmd, check=True)

# Start the VM
start_vm_cmd = ["VBoxManage", "startvm", vm_name]
subprocess.run(start_vm_cmd, check=True)
