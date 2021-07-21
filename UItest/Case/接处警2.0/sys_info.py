import wmi

def get_cpu_info():
    cpuinfo = wmi.WMI()
    for cpu in cpuinfo.Win32_Processor():
        return cpu.LoadPercentage

def get_memory_info():
    tmpdict = {}
    c = wmi.WMI()
    cs = c.Win32_ComputerSystem()
    os = c.Win32_OperatingSystem()
    pfu = c.Win32_PageFileUsage()
    tmpdict["MemTotal"] = int(cs[0].TotalPhysicalMemory) / 1024 / 1024
    tmpdict["MemFree"] = int(os[0].FreePhysicalMemory) / 1024
    tmpdict["SwapTotal"] = int(pfu[0].AllocatedBaseSize)
    tmpdict["SwapFree"] = int(pfu[0].AllocatedBaseSize - pfu[0].CurrentUsage)
    return tmpdict

if __name__ == "__main__":
    print (get_cpu_info())
    print (get_memory_info())