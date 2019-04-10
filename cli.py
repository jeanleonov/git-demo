import click

import data


@click.command()
@click.option('--order', default='cpu%', type=str, help='...')
def show_processes(order):
    processes = data.list_processes()
    click.echo(data.render_process(processes, order))


if __name__ == '__main__':
    show_processes()
