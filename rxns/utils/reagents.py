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


class Reagent(object):

    """
    Class to represent a generic reagent.

    Enables looking up recipes that contain this reagent, etc.

    pcid (int): The PubChem CID of this reagent.
    recipes (pandas.DataFrame): Pandas `DataFrame` containing recipe IDs and links to the objects.

    """

    def __init__(self, pubchemid):
        """
        Initializes a reagent.

        Uses the pubchemid to obtain a pubchempy.Compound object from pubchem.
        
        Args:
            name (str): human-readable name
            pubchemid (int): CID number of reagent on PubChem [https://pubchem.ncbi.nlm.nih.gov/]
        
        Returns:
            None
        """

        self.pcid = pubchemid
        self.pubchem = pcp.Compound.from_cid(pubchemid)

        # self.recipes = pd.DataFrame(columns=['IDS', 'OBJS', ])  ## THis should be in the RecipeRegistry


    def register_reagent(self, ctx):
        """
        Registers reagent with `ReagentRegistry` object.

        If no registry exists in the current context, `ReagentRegistry` creates and registers one with the context.

        Args:
            ctx (click.Context): reference to the current context

        Returns:
            None
        """

        try:
            ctx.obj["REAGENTS"].register_reagent(self)
        except TypeError as exc:
            if "object is not subscriptable" in exc.args[0]:
                ctx.obj["REAGENTS"] = ReagentRegistry()
                ctx.obj["REAGENTS"].register_reagent(self)




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

        self.reagents = pd.DataFrame(columns=['PCID', 'OBJS'])

        self._add_to_context(ctx)

    def _add_to_context(self, ctx):
        """
        Adds this registry to `ctx`.

        extended description

        Args:
            ctx (click.Context): the current application context

        Returns:
            None
        """

        ctx.obj.REAGENTS = self

    def register_reagents(self, recipe):
        """
        Registers `Reagent` objects for all reagents listed in `recipe`.

        Adds all of `recipe`'s reagents to `self.reagents` if not already present.
        Adds reference to the `recipe` to `self.recipes`


        Args:
            recipe (rxn.utils.recipes.Recipe): a recipe object

        Returns:
            None
        """

        raise NotImplementedError()




