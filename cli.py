import click

import data


@click.command()
def show_processes():
    processes = data.list_processes()
    for process in processes:
        click.echo(process)


if __name__ == '__main__':
    show_processes()
