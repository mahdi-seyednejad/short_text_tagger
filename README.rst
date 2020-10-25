=================
short_text_tagger
=================


.. image:: https://img.shields.io/pypi/v/short_text_tagger.svg
        :target: https://pypi.python.org/pypi/short_text_tagger

.. image:: https://img.shields.io/travis/JohnAnthonyBowllan/short_text_tagger.svg
        :target: https://travis-ci.com/JohnAnthonyBowllan/short_text_tagger

.. image:: https://readthedocs.org/projects/short-text-tagger/badge/?version=latest
        :target: https://short-text-tagger.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




short_text_tagger generates topic distributions for all texts in a corpus.


* Free software: MIT license

Installation
------------
``pip install short-text-tagger``

Usage 
--------
This package depends on Graph-tool, which is a C++ library with a Python wrapper. See https://git.skewed.de/count0/graph-tool/-/wikis/installation-instructions
for instructions on how to install Graph-tool.

If you have graph-tool installed and want to use its community detection functionality to generate topics, then
import the following function into your script, which expects a pandas DataFrame with columns ``id`` and ``text``:

``from short_text_tagger.short_text_tagger import generate_topic_distributions_from_corpus``


If you don't have graph-tool installed or want to substitute other community detection algorithms, then 
you can import the following function for text preprocessing: ``from short_text_tagger.short_text_tagger import cleaned_texts_df_from_data``,
which adds a required ``words`` column to the aforementioned DataFrame. 

After, you can import ``from short_text_tagger.short_text_tagger import assign_text_probabilities``, 
which expects the input DataFrame with a ``words`` column and a list of dictionaries (word to topic mappings)
and returns the same DataFrame with appended topic probability columns. The hook is the creation of the list of word to 
topic mappings. In this package, that functionality is provided by ``from short_text_tagger.short_text_tagger import word_to_block_dict``.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage



``Test block \n
More text``
