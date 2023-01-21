import nltk, re, os
import file_handler

def fix_end_of_sentence(text: str): # -> str
  """
  ### Adds a space after the end of a sentence without a space
  #### Example
  The tokeniser will interpret this as a whole sentence.A human reader can detect the missing space.
  """
  end_of_sentece_chars = ['.','?','!']
  i = 0
  while i < len(text)-1:
    if text[i] in end_of_sentece_chars:
      if (ord(text[i+1]) >= 97 and ord(text[i+1]) <= 122): 
        if re.search('[a-z]\.co\.za',text[i-1:i+6]) or re.search('\.co\.za',text[i-3:i+3]):
          i+=1
          continue
        text = ' '.join([text[:i+1], text[i+1:]])
    i+=1
  return text
    


def pre_process_text(text): # -> str
  text = text.lower()
  text = re.sub('\-','',text) # removes hyphens from line breaks eg. con-fidence
  text = re.sub('\”','"',text) # standardise apostrophes 
  text = re.sub('\“','"',text) # standardise apostrophes 
  text = re.sub('\•','',text) # remove bullet points
  text = re.sub('ŉ','n',text) # read the aftikaans 'n' as some funny char 'ŉ'
  text = re.sub('\s{2,}',' ',text) # replace more than 2 spaces with 1
  text = re.sub('\t',' ',text) # replace tabs with one space
  text = re.sub('\n',' ',text) # replace newlines with one space
  text = fix_end_of_sentence(text) #split sentences without spaces
  return text

def tokenise(text): # -> str
  return nltk.tokenize.sent_tokenize(pre_process_text(text))

