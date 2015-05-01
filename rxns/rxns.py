import configparser

import click




def read_config(path):
    parser = configparser.RawConfigParser()
    parser.read(path)
    rv = {}
    for section in parser.sections():
        for key, value in parser.items(section):
            rv['%s.%s' % (section, key)] = value
    return rv




@click.group()
@click.option('--config', default='',
    help="Path to config.ini",
    type=click.Path())
@click.pass_context
def cli(ctx, config, ):
    """
    react helps you plan and execute hierarchical molecular biology reactions.


    """

    if config:
        ctx.obj['CONFIG'] = read_config(config)

@cli.command()
@click.option('--nutin',is_flag=True,
    help='nothing to see; move a long')
@click.pass_context
def dummy(ctx,nutin):
    """
    This is a dummy command.
    """
    pass
