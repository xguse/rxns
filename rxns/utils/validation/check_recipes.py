# check_recipes.py is part of the 'rxns' package.
# It was written by Gus Dunn and was created on 5/6/15.
#
# Please see the license info in the root folder of this package.

"""
Purpose: Validate information relating to recipes.

=================================================
check_recipes.py
=================================================
"""

import os
import collections

import rxns.errors as e


__author__ = 'Gus Dunn'

def files_exist(conf):
    """
    Enforce that recipe files exist.

    extended description

    Args:
        conf (dict): configuration values.

    Returns:
        None

    Raises:
        `rxn.ValidationError`

    """

    paths = conf.recipe_files.values()

    for path in paths:

        missing = [path for path in paths if not os.path.exists(path)]

        if missing:
            msg = "recipe_files: {paths}, listed in config: {conf} do not exist.".format(
                paths=missing,
                conf=conf.meta_data.path)

            raise e.ValidationError(msg)



def unique_recipe_names(conf):
    """
    Enforce that unique recipe names were provided in the configuration file.

    extended description

    Args:
        conf (dict): configuration values.

    Returns:
        None

    Raises:
        `rxn.ValidationError`

    """
    raise NotImplementedError(
        "This method is useless because pyyaml overwrites duplicated keys because... well Dictionaries."
    )

    dups = [x for x, count in collections.Counter(conf.recipe_files.keys()).items() if count > 1]

    if dups:
        msg = "recipe_files: {names} are duplicated in config: {path}".format(
            names=dups,
            path=conf.meta_data.path)

        raise e.ValidationError()


def unique_recipe_paths(conf):
    """
    Enforce that unique recipe paths were provided in the configuration file.

    extended description

    Args:
        conf (dict): configuration values.

    Returns:
        None

    Raises:
        `rxn.ValidationError`

    """

    dups = [x for x, count in collections.Counter(conf.recipe_files.values()).items() if count > 1]

    if dups:
        msg = "recipe_files: {recipe_paths} are duplicated in config: {path}".format(
            recipe_paths=dups,
            path=conf.meta_data.path)

        raise e.ValidationError(msg)
