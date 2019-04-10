import click

import data


@click.command()
@click.option('--top', default=10, type=int, help='Number of top.')
def show_processes(top):
    processes = data.list_processes()
    click.echo(data.render_process(processes, top))


if __name__ == '__main__':
    show_processes()
