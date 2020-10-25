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
This package depends on graph-tool, which is a C++ library with a Python wrapper. See https://git.skewed.de/count0/graph-tool/-/wikis/installation-instructions
for instructions on how to install graph-tool.

If you have graph-tool installed and want to use its community detection functionality to generate topics, then
import ``generate_topic_distributions_from_corpus``, which expects a pandas DataFrame with columns ``id`` and ``text``:

.. code-block:: Python

   # example 

   import pandas as pd 
   from short_text_tagger.short_text_tagger import generate_topic_distributions_from_corpus

   sample_df = pd.DataFrame({
        'id':[1,2,3,...],
        'text':[
                'The store was crazy today. ',
                'I went to the store to get apples, oranges, and pears. But the lines were long. Waited 45 minutes to checkout.',
                'The lines were so short, so I was out of there quickly. I bought apples, pears, and beer.',
                ...
        ]
   })

   topics_df = generate_topic_distributions_from_corpus(sample_df)

The parameter ``block_level`` will influence how many final topics are present in the corpus. If the corpus is small, smaller
``block_level`` may be necessary due to the lack of many observations. If the corpus is very large, the NSBM will have much 
larger depth, so you may have to increase the ``block_level`` so you do not have an unwieldy amount of topics. ``block_level``
is set to 2 by default.


If you don't have graph-tool installed or want to provide your own word to topic maps, then 
you can import functions that perform text preprocessing and text topic probability generation:

.. code-block:: Python

   # example 2

   import pandas as pd 
   from short_text_tagger.short_text_tagger import cleaned_texts_df_from_data
   from short_text_tagger.short_text_tagger import assign_text_probabilities

   sample_df = pd.DataFrame({
        'id':[1,2,3,...],
        'text':[
                'The store was crazy today. ',
                'I went to the store to get apples, oranges, and pears. But the lines were long. Waited 45 minutes to checkout.',
                'The lines were so short, so I was out of there quickly. I bought apples, pears, and beer.',
                ...
        ]
   })

   preprocessed_df = cleaned_texts_df_from_data(sample_df) # adds a "words" column (List[str])
   
   # Create your own List[Dict[str,str]], where each element in the list is a dict of word to topic mappings.
   # In this package, the function "word_to_block_dict" accomplishes this.
   word_to_topic_dict_list = ...

   final_df = assign_text_probabilities(preprocessed_df,word_to_topic_dict_list) 
   
   

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage



