import psutil


def list_processes():
    process_attrs = (
        'cpu_times', 'cpu_percent', 'memory_info', 'cmdline'
    )
    return [
        process for process in
        psutil.process_iter(process_attrs)
    ]
