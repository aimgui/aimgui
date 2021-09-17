import os
import click

from aimgen.runner import Runner

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    if ctx.invoked_subcommand is None:
      Runner().gen_all()

@cli.command()
@click.pass_context
@click.argument('name')
def gen(ctx, name):
    Runner().gen(name)
