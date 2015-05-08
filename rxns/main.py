import os

import yaml
import munch
import click

from rxns import errors as e
from rxns.utils import reagents
from rxns.utils import recipes

from rxns.utils.validation import check_recipes

spoils = munch.Munch()


def process_config(config):
    """
    Prepare user's config file.

    Also handles validation.

    Args:
        config (str): path to config file.

    Returns:
        conf (dict): configuration values.
    """
    conf = munch.munchify(yaml.load(config))
    conf.meta_data = munch.Munch()
    conf.meta_data.path = os.path.abspath(config.name)

    # # Run all validations that we can do on conf
    # # Can add more later
    check_recipes.files_exist(conf)
    # check_recipes.unique_recipe_names(conf)
    check_recipes.unique_recipe_paths(conf)

    return conf


@click.group()
@click.option('--config', default=None,
              help="Path to config.yaml",
              type=click.File())
@click.pass_context
def cli(ctx, config):
    """Helps plan and execute hierarchical molecular biology reactions."""

    ctx.obj = munch.Munch()

    if config:
        ctx.obj.CONFIG = process_config(config)

    reagents.ReagentRegistry(ctx)
    recipes.RecipeRegistry(ctx)


    spoils.obj = ctx.obj




@cli.command()
@click.pass_context
def validate(ctx):
    """
    Validate your config and exit.
    """
    click.secho('\nValidation results:', fg='yellow')

    click.echo(
        """\nI did not notice a problem with your settings. \nThis does {not_} guarantee it has none.""".format(
            not_=click.style('not', fg='red'))
    )


if __name__ == '__main__':
    conf = cli()
