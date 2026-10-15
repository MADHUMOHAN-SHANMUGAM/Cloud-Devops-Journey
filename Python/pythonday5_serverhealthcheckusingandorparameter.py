server_name = input("Enter the servername:")
cpu_usage = float(input("Enter the cpu_usage:"))
memory_usage = float(input("Enter the memory_usage:"))
if cpu_usage >= 80 and memory_usage >= 80:
    print("Critical: CPU and memory usage are high in server",server_name)
elif cpu_usage >= 80 or memory_usage >= 80:
    print("Warning: CPU or memory usage is high in server", server_name)
else:
    print("server", server_name, "usage is normal")