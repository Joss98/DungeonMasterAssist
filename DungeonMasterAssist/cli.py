import click

@click.command()
@click.option('--count', default=1, help='number of times [message] is printed')
@click.argument('message')
def hello(count, message):
    for x in range(count):
        click.echo(f"{message}")


if __name__ == "__main__":
    hello()