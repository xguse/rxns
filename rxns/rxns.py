
import yaml
import munch
import click

from rxns.utils import reagents
from rxns.utils import recipes

# def read_config(path):
#     parser = configparser.RawConfigParser()
#     parser.read(path)
#     rv = {}
#     for section in parser.sections():
#         for key, value in parser.items(section):
#             rv['%s.%s' % (section, key)] = value
#     return rv




@click.group()
@click.option('--config', default='',
              help="Path to config.yaml",
              type=click.File())
@click.pass_context
def cli(ctx, config):
    """Helps you plan and execute hierarchical molecular biology reactions."""

    ctx.obj = munch.Munch()

    if config:
        conf = munch.munchify(yaml.load(config))
        ctx.obj.CONFIG = conf

    recipes.RecipeRegistry(ctx)
    reagents.ReagentRegistry(ctx)





@cli.command()
@click.option('--nutin', is_flag=True,
              help='nothing to see; move a long')
@click.pass_context
def dummy(ctx, nutin):
    """
    This is a dummy command.
    """
    pass
