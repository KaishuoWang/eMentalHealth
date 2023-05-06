# -*- coding: utf-8 -*-
import re

class PreProcessing:
    def __init__(self, records, taxonomy):
        self.records = records
        self.taxonomy = taxonomy

    def cleanHtml(self, raw_html):
        CLEANER = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        cleanText = re.sub(CLEANER, '', raw_html)
        return cleanText

    def remove_new_line(self, raw):
        cleanText = re.sub(r"[\r\n\t]+", '', raw)
        return cleanText
    
    def preprocess(self):
        print('Length of records before preprocessing:', len(self.records))
        print('Length of taxonomy before preprocessing:', len(self.taxonomy))

        self.records['description'] = self.records['description'].apply(lambda x: self.cleanHtml(x))
        self.taxonomy['description'] = self.taxonomy['description'].apply(lambda x: self.cleanHtml(x))

        self.records['description'] = self.records['description'].apply(lambda x: self.remove_new_line(x))
        self.taxonomy['description'] = self.taxonomy['description'].apply(lambda x: self.remove_new_line(x))

        # Remove empty description
        indices = []
        for index, row in self.records.iterrows():
            if row['description'] == '':
                indices.append(index)

        self.records = self.records.drop(self.records.index[indices])
        self.records.reset_index(drop=True, inplace=True)

        indices = []
        for index, row in self.taxonomy.iterrows():
            if row['description'] == '':
                indices.append(index)

        self.taxonomy = self.taxonomy.drop(self.taxonomy.index[indices])
        self.taxonomy.reset_index(drop=True, inplace=True)

        print('Length of records after preprocessing:', len(self.records))
        print('Length of taxonomy after preprocessing:', len(self.taxonomy))

        return self.records, self.taxonomy