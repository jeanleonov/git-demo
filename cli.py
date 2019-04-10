import click

import data


@click.command()
def show_processes():
    processes = data.list_processes()
    click.echo(data.render_process(processes))


if __name__ == '__main__':
    show_processes()
