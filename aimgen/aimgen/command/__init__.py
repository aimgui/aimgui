import os
import click

from aimgen.main import main

@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)

@cli.command()
@click.pass_context
def gen(ctx):
    main()
