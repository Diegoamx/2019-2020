#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:12:20 2019

@author: diegomurcia
"""
import math

def clean_text(txt):
    """takes a string of text txt as a parameter and returns a list containing
       the words in txt after it has been “cleaned”.
    """
    txt = txt.replace('.', '')
    txt = txt.replace(',', '')
    txt = txt.replace('!', '')
    txt = txt.replace('?', '')
    txt = txt.replace('"', '')
    txt = txt.replace('$', '')
    txt = txt.replace(':', '')
    txt = txt.replace(';', '')
    txt = txt.replace('-', '')
    txt = txt.replace('=', '')
    txt = txt.replace('-', '')
    txt = txt.replace('/', '')
    txt = txt.replace('(', '')
    txt = txt.replace(')', '')
    txt = txt.lower().split()
    return txt
    
def sample_file_write(filename):
    """A function that demonstrates how to write a
       Python dictionary to an easily-readable file.
    """
    d = {'test': 1, 'foo': 42}   # Create a sample dictionary.
    f = open(filename, 'w')      # Open file for writing.
    f.write(str(d))              # Writes the dictionary to the file.
    f.close()                    # Close the file.
    
def sample_file_read(filename):
    """A function that demonstrates how to read a
       Python dictionary from a file.
    """
    f = open(filename, 'r')    # Open for reading.
    d_str = f.read()           # Read in a string that represents a dict.
    f.close()

    d = dict(eval(d_str))      # Convert the string to a dictionary.

    print("Inside the newly-read dictionary, d, we have:")
    print(d)

def stem(s):
    """ accepts a string as a parameter and returns the stem of s """

    if len(s) >= 5:
        if s[-3:] == 'ing':
            if s[-5] != s[-4]:
                s = s[:-3]
            else:
                s = s[:-4]
        if s[-3:] == 'ies':
            s = s[:-3]
            s += 'y'
        if s[-1:] == 's':
            s = s[:-1]
        if s[-2:] == 'er':
            s = s[:-2]
        if s[-2:] == 'es':
            s = s[:-2]
        if s[-4:] == 'tion':
            s = s[:-4]
        if s[-1:] == 'y':
            s = s[:-1] + 'i'
        if s[-1:] == 'd':
            s = s[:-1]
        if s[-2:] == 'th':
            s = s[:-2]

    return s


def compare_dictionaries(d1, d2):
    """ compute and return their log similarity score """

    score = 0
    total = 0

    for key in d1:
        total += d1[key]
    
    for i in d2:
        if i in d1:
            score += math.log(d1[i]/total) * d2[i]
        else:
            score += math.log(0.5/total) * d2[i]

    return score


class TextModel:
    def __init__(self, model_name):
        """constructs a new TextModel object by accepting a string model_name 
           as a parameter and initializing three attributes:
               1. name - a string that is a label for this text model
               2. words - a dictionary that records the number of times each 
                  word appears in the text.
               3. word_length - a dictionary that records the number of times 
                  each word length appears.
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.exclamation = {}
        
    def __repr__(self):
        """ returns a string that includes the name of the model as well as 
            the sizes of the dictionaries for each feature of the text.
        """
        s = ''
        s += 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of exclamation marks: ' + str(len(self.exclamtion)) + '\n'
        
        return s  

    
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces to all of the 
           dictionaries in this text model.
        """
        word_list = clean_text(s)
        for x in word_list:
            length = len(x)
            st = stem(x)
            if x in self.words:
                self.words[x] += 1
            else:
                self.words[x] = 1
            if length in self.word_lengths:
                self.word_lengths[length] += 1
            else:
                self.word_lengths[length] = 1
            if st in self.stems:
                self.stems[st] += 1
            else:
                self.stems[st] = 1
            if '.' in self.sentence_lengths:
                self.sentence_lengths[st] += 1
            else:
                self.sentence_lengths[st] = 1
            if '!' in self.exclamation:
                self.exclamation[st] += 1
            else:
                self.exclamation[st] = 1

        
        
    def add_file(self, filename):
        """ adds all of the text in the file identified by filename to the
            model; it should not explicitly return a value 
        """

        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        self.add_string(text)


    def save_model(self):
        """ saves the TextModel object self by writing its various feature
            dictionaries to files """

        a = open(self.name + '_words.txt', 'w')      
        a.write(str(self.words))              
        a.close()

        b = open(self.name + '_word_lengths.txt', 'w')      
        b.write(str(self.word_lengths))              
        b.close()

        c = open(self.name + '_stems.txt', 'w')      
        c.write(str(self.stems))              
        c.close()

        d = open(self.name + '_sentence_lengths.txt', 'w')      
        d.write(str(self.sentence_lengths))              
        d.close()

        e = open(self.name + '_exclamation.txt', 'w')      
        e.write(str(self.exclamation))              
        e.close()

    def read_model(self):
        """ reads the stored dictionaries for the called TextModel object from
         their files and assigns them to the attributes of the called TextModel """

        a = open(self.name + '_words.txt', 'r')
        self.words = a.read()
        a.close()
        self.words = eval(self.words)

        b = open(self.name + '_word_lengths.txt', 'r')
        self.word_lengths = b.read()
        b.close()
        self.word_lengths = eval(self.word_lengths)

        c = open(self.name + '_stems.txt', 'r')
        self.stems = c.read()
        c.close()
        self.stems = eval(self.stems)

        d = open(self.name + '_sentence_lengths.txt', 'r')
        self.sentence_lengths = d.read()
        d.close()
        self.sentence_lengths = eval(self.sentence_lengths)
        
        e = open(self.name + '_exclamation.txt', 'r')
        self.exclamation = e.read()
        e.close()
        self.exclamation = eval(self.exclamation)
        
        
    def similarity_scores(self, other):
        """computes and returns a list of log similarity scores measuring
           the similarity of self and other – one score for each type of
           feature 
        """

        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        exclamation_score = compare_dictionaries(other.exclamation, self.exclamation)

        a = [word_score, word_lengths_score, stems_score, sentence_lengths_score, exclamation_score]
        
        return a

    def classify(self, source1, source2):
        """ compares the called TextModel object (self) to two other “source”
            TextModel objects (source1 and source2) and determines which of 
            these other TextModels is the more likely source of the called
            TextModel
        """

        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)

        print('scores for: ', source1.name, scores1)
        print('scores for: ', source2.name, scores2)

        a = 0
        b = 0

        for i in range(len(scores1)):
            if scores1[i] > scores2[i]:
                a += 1
            else:
                b += 1
        if a > b:
            print(self.name, ' is more likely to have come from ', source1.name)
        else:
            print(self.name, ' is more likely to have come from ', source2.name)

    
def test():
    """ Testing the function"""
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')
    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
        
        
def run_tests():
    """ Tests the Function for Friends versus Fresh Prince of Bel Air """
    source1 = TextModel('Friends')
    source1.add_file('friends_source_text.txt')

    source2 = TextModel('Fresh Prince of Bel Air')
    source2.add_file('fresh_prince_source_text.txt')

    new1 = TextModel('Drake and Josh - Tree Scene')
    new1.add_file('d&j_tree_source_text.txt')
    new1.classify(source1, source2)