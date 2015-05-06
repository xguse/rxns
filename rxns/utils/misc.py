# misc.py is part of the 'rxns' package.
# It was written by Gus Dunn and was created on 5/4/15.
#
# Please see the license info in the root folder of this package.

"""
Purpose: Provides extra utility that doesn't fit well elsewhere.

=================================================
misc.py
=================================================
"""
__author__ = 'Gus Dunn'

import collections


def tree():
    """
    Return an autovivifying tree structure based on recursive `defaultdict`
    
    Returns:
        (`collections.defaultdict`): `collections.defaultdict(tree)`
    """
    
    return collections.defaultdict(tree)



