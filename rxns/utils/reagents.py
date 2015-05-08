# reagents.py is part of the 'rxns' package.
# It was written by Gus Dunn and was created on 5/4/15.
#
# Please see the license info in the root folder of this package.
"""
Model logic and data for reagents of a reaction.

=================================================
reagents.py
=================================================
Model logic and data for reagents of a reaction.
"""
__author__ = 'Gus Dunn'
import  munch
import pubchempy as pcp


import pandas as pd




class ReagentRegistry(object):

    """
    Class to represent and expose a registry of all reagents to the current running context.
    """

    def __init__(self, ctx):
        """
        Initialize a `ReagentRegistry` object and attach it to the running context.

        Args:
            ctx (click.Context): the current `click.Context` object.

        Returns:
            None

        Raises:
            TODO
        """
        ctx.obj.REAGENTS = self

        self.obj = ctx.obj
        self.reagents = pd.DataFrame()
        self.deps = pd.DataFrame()

        self._

        # 1. create table of reagents tagged with which recipe they belong to
        # 2. establish unique index ID for each reagent
        # 3. extract dependencies for each reagent to a separate table
        for recipe in {recipe.name: recipe for recipe in self._yield_recipes(ctx.obj.CONFIG)}:

            recipe.table['recipe'] = recipe.name

            self.reagents = pd.concat([self.reagents, recipe.table])






    def _yield_recipes(self, conf):
        """
        Yields a list of instantiated `Recipe` objects.

        Args:
            conf (dict): A dict of the configuration values used for this call.

        Yield:
            `Recipe` objects
        """
        assert isinstance(conf, dict)

        for name, path in conf.recipe_files.items():
            try:
                deps = conf.dependencies[name]
                yield Recipe(conf, name, path, dependencies=deps)
            except KeyError:
                yield Recipe(conf, name, path, dependencies=None)

    def register_reagents(self, recipe):
        """
        Registers reagents listed in `recipe`.


        Args:
            recipe (rxn.utils.recipes.Recipe): a recipe object

        Returns:
            None
        """




