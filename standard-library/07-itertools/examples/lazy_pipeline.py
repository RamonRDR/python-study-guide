"""Compose a small lazy pipeline with chain and islice."""

from itertools import chain, islice

pages = [["alpha", "beta"], ["gamma"], ["delta", "epsilon"]]
stream = chain.from_iterable(pages)
preview = list(islice(stream, 4))

print(preview)
