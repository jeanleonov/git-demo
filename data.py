import psutil
import tabulate


def list_processes():
    process_attrs = (
        'cpu_times', 'cpu_percent', 'memory_info', 'cmdline'
    )
    return [
        process for process in
        psutil.process_iter(process_attrs)
    ]


def render_process(processes, order, top):
    if order == 'memory':
        processes.sort(key=lambda process: -process.memory_info().rss)
    elif order == 'cpu%':
        processes.sort(key=lambda process: -process.cpu_percent())
    elif order == 'cpu_time':
        processes.sort(key=lambda process: -process.cpu_times().user - process.cpu_times().system)
    table = [
        [
            p.pid, p.status(), p.memory_info().vms, p.memory_info().rss,
            p.cpu_percent(), p.cpu_times().user, p.cpu_times().system,
            p.cmdline()[0] if p.cmdline() else ''
        ]
        for p in processes
    ]
    return tabulate.tabulate(
        tabular_data=table[:top],
        headers=[
            'PID', 'Status', 'V-Memory', 'R-Memory',
            'CPU%', 'CPU User', 'CPU System',
            'Command'
        ]
    )

