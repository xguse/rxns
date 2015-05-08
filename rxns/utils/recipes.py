# recipes.py is part of the 'rxns' package.
# It was written by Gus Dunn and was created on 5/4/15.
#
# Please see the license info in the root folder of this package.

"""
Purpose: Model the logic and functions associated with reaction recipes.

=================================================
recipes.py
=================================================
"""
__author__ = 'Gus Dunn'

import pandas as pd

from rxns.utils.reagents import Reagent


# def load_recipes(path_list):
#     """
#     Yields a list of instantiated `Recipe` objects.
#
#     Iterates through the list of paths, calling `Recipe(path)` on each and yielding the object.
#
#     Args:
#         path_list (list): A list of paths pointing to recipe table files.
#         argN (argN_type): argN_description
#
#     Yield:
#         `Recipe` objects
#     """
#     assert isinstance(path_list, list)
#
#     for path in path_list:
#         yield Recipe(name, path, dependencies=)


class Recipe(object):

    """
    Base class to represent a set of reactants that make up a whole or partial recipe for a reaction.

    Attributes:
        conf (dict): configuration values.
        name (str): its a name come on.
        path (str): recipe file location.
        deps (list): references to any `Recipe` objects that this one depends on.
        reagents (dict): mappings to the `Reagent` objects that make up this recipe's ingredients.
        table (pandas.DataFrame): pandas table read directly from `path`.

    """

    def __init__(self, conf, name, path, dependencies=None):
        """
        Initializes a recipe object containing the information stored in the `recipe_path` argument.

        Loads, initializes, and registers any new reactants defined in the included `recipe_path`

        Args:
            conf (dict): configuration values.
            name (str): unique name for this recipe.
            path (str): location of table-formatted recipe definition.
            dependencies (list): list of recipe names that this recipe depends on.

        Returns:
            None
        """

        self.conf = conf
        self.name = name
        self.path = path
        self.deps = dependencies
        self.table = pd.read_table(path, sep='|')
        self.reagents = None

    def _recode_reagents(self):
        """
        Process `self.table`, converting reagent strings into `Reagent` objects and registering them.

        Also stores them in `self.reagents`

        Returns:
            None
        """

        raise NotImplementedError

    def _process_reagents(self):
        """
        Process this recipe's reagents and log them into the reagents registry.

        Returns:
            None
        """

        raise NotImplementedError





class RecipeRegistry(object):
    """
    Class to represent and expose a registry of all recipes to the current running context.
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
        ctx.obj.RECIPES = self

        self.obj = ctx.obj
        self.registry = {recipe.name: recipe for recipe in self._yield_recipes(ctx.obj.CONFIG)}

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



