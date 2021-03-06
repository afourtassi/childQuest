import csv
import argparse
import os
import json
from collections import Counter


CHI_LIST = ('CHI')
PAR_LIST = ('FAT', 'MOT')


###########################
# Part 1: parse arguments
parser = argparse.ArgumentParser(description='.proccess jason to csv files.')

# parser.add_argument('--verbose', action='store_true', help='dump verbosely')
parser.add_argument('--jsonInput', type=str, help="path to the first file")
parser.add_argument('--csvpath', type=str, help="path where the csv file would be saved")

#args = parser.parse_args()
args, unknown = parser.parse_known_args()
print(args)

#if not os.path.isfile(args.jsonInput):
#    raise FileNotFoundError(args.jsonInput)

with open(args.jsonInput, 'r') as f:
    annotation_data = json.load(f)


result = []

for i, annotation_i in enumerate(annotation_data['documents']):
    if annotation_i['type'] != 'utterance':
        continue

    labels_1 = '[' + ','.join([annotation_i['label_1_a'], annotation_i['label_1_b'], annotation_i['label_1_c']]) + ']'
    result.append([
        i, # utterance ID
	annotation_i['subject'],  # Speaker
        annotation_i['turn'],     # utterance
        labels_1,                 # annotation-C
        1,                          # list-ID, 1 or 2
        ])

    labels_2 = '[' + ','.join([annotation_i['label_2_a'], annotation_i['label_2_b'], annotation_i['label_2_c']]) + ']'
    result.append([
        i,                          # ID
	annotation_i['subject'],  # Speaker
        annotation_i['turn'],     # utterance
        labels_2,                 # annotation-C
        2,                          # list-ID, 1 or 2
    ])


with open(args.csvpath, 'w', newline='') as csvfile:
    #spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(['ID', 'Speaker','utterance', 'annotation', 'list-ID'])
    spamwriter.writerows(result)
