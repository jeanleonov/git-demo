import click

import data


@click.command()
@click.option('--top', default=10, type=int, help='Number of top.')
@click.option('--order', default='cpu%', type=str, help='...')
def show_processes(order, top):
    processes = data.list_processes()
    click.echo(data.render_process(processes, order, top))


if __name__ == '__main__':
    show_processes()
