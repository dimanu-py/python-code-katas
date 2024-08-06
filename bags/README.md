# :handbag: Bags Kata :handbag:

## Resources

These instructions where extracted from Codurance website. The link to the original instructions can be found in the link bellow.

[![Web](https://img.shields.io/badge/Codurance-Website-14a1f0?style=for-the-badge&logo=web&logoColor=white&labelColor=101010)](https://www.codurance.com/katas/bags)

## Description

When Dimanu left his home to start his adventures, all he brought was a backpack. He eventually found additional smaller bags to stash his
items.

After enchanting his weapons and looking for ingredients and materials for a long time, Dimanu noticed his bags were really disorganized,
maybe we can code a spell for him to organize them?

### Problem

Our goal is to create an application that helps Dimanu organize the items in his bags.

- Each bag can have either a category or not.
- The backpack has no category.
- Items are always added to the backpack, if it happens to be full, the item is added to the next available bag.
- After organizing the items, each bag should have the items belonging to its category, sorted alphabetically. If the bag is full, the
rest of hte items are stored in the backpack or successive bags, following the previous sort.

### Rules
- Dimanu has 1 backpack and 4 extra bags.
- Each bag can store 4 items.
- The backpack can store 8 items
- Each bag can have a category, the backpack has no category.
- Items are sorted alphabetically after organizing the bags.

### Example

Suppose Dimanu has 8 items in his backpack and 1 empty extra bag, which has a category of "Metals":

```python
backpack = ['Leather', 'Iron', 'Copper', 'Marigold', 'Wool', 'Gold', 'Silk', 'Copper']
bag_with_metals_category = []
bag_with_no_category = []
bag_with_weapons_category = []
bag_with_no_category = []
```

He finds 2 new items, which are stored in the next available bag since the backpack is already full:

```python
backpack = ['Leather', 'Iron', 'Copper', 'Marigold', 'Wool', 'Gold', 'Silk', 'Copper']
bag_with_metals_category = ['Copper', 'Cherry Blossom']
bag_with_no_category = []
bag_with_weapons_category = []
bag_with_no_category = []
```

Now he casts the organizing spell, the result is:

```python
backpack = ['Cherry Blossom', 'Iron', 'Leather', 'Marigold', 'Silk', 'Wool']
bag_with_metals_category = ['Copper', 'Copper', 'Copper', 'Gold']
bag_with_no_category = []
bag_with_weapons_category = []
bag_with_no_category = []
```

## Objective

The main objective is to practice TDD and the SOLID principles.

## Visit my GitHub profile to see all solved katas 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py/python-code-katas)
