"""Structured data for the India MSME opportunity study.

Every number in the report is defined once in these modules and written to
CSV by ``scripts/build_datasets.py``. Each record carries a ``source_ids``
field that points to ``SOURCES`` in ``sources.py`` and a ``data_type`` field:

* ``observed``  - figure published by the cited source (official or company)
* ``derived``   - arithmetic on observed figures (method stated in ``notes``)
* ``estimate``  - our modelled estimate; assumptions stated in ``notes``
* ``assumption``- an input we chose that must be validated in the field
"""
