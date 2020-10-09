import nltk
import pandas as pd
from short_text_tagger.text import string_to_valid_word_list
from short_text_tagger.edgelist import EdgeList
from short_text_tagger.nsbm import NSBM
from collections import defaultdict
import sys

nltk.download('stopwords')


if __name__ == '__main__': 

    iterations = 20

    # read data
    short_texts_df = pd.read_csv("Sentiment.csv")

    assert 'id' in short_texts_df.columns, "'id' is a required column name for this analysis" 
    assert 'text' in short_texts_df.columns, "'text' is a required column name for this analysis" 
    assert len(short_texts_df) > 0, "Need at least one short text for this analysis"

    short_texts_df = short_texts_df[['id','text']]
    final_short_texts_df = short_texts_df.copy()

    # creating edge list
    short_texts_df['words'] = short_texts_df['text'].apply(lambda text: string_to_valid_word_list(text)) 
    edgelist = EdgeList(corpus = short_texts_df['words'])

    # initializing dict of topic probabilities for each short text
    text_topic_probabilities = {row['id']: defaultdict(int) for i,row in short_texts_df.iterrows()}
    topics_seen = set()

    for _ in range(iterations):
        # fit NSBM
        nsbm = NSBM(edgelist)
        nsbm.fit()

        # update set of all topics ever seen
        topics_seen = topics_seen.union(set(block for i,block in nsbm.block_index_to_block_name_dict.items()))

        # for each text, get probabilities of topic memberships
        for i,row in short_texts_df.iterrows():
            text_id = row['id']
            words = row['words']
            num_words = len(words)
            for word in words:
                word_index = nsbm.node_name_to_node_index[word]
                block_index = nsbm.get_block_from_node(word_index)
                block = nsbm.block_index_to_block_name_dict[block_index] 
                text_topic_probabilities[text_id][block] += 1/(iterations*num_words)

    for topic in topics_seen:
        final_short_texts_df[f'topic_prob__{topic}'] = short_texts_df['id'].apply(lambda id: text_topic_probabilities[id][topic] if topic in text_topic_probabilities[id].keys() else 0) 
  
    

    final_short_texts_df.to_csv('output.csv')
