import csv
import argparse
import os
import json
from collections import Counter


CHI_LIST = ('CHI')
PAR_LIST = ('FAT', 'MOT')


###########################
# Part 1: parse arguments
parser = argparse.ArgumentParser(description='Compare between annotations and generate a .csv file.')

# parser.add_argument('--verbose', action='store_true', help='dump verbosely')
parser.add_argument('--charlie', type=str, default='../comparaison/data_PAR_nov_23/Yamaguchi_031113_PAR_charlie.json', help="path to the first file")
parser.add_argument('--morgane', type=str, default='../comparaison/data_PAR_nov_23/Yamaguchi_031113-PAR-MP.json', help="path to the second file")
parser.add_argument('--csvpath', type=str, default='Yamaguchi_031113_PAR.csv', help="path where the csv file would be saved")

#args = parser.parse_args()
args, unknown = parser.parse_known_args()
print(args)

if not os.path.isfile(args.charlie):
    raise FileNotFoundError(args.charlie)

if not os.path.isfile(args.morgane):
    raise FileNotFoundError(args.morgane)

with open(args.charlie, 'r') as f:
    annotation_data_1 = json.load(f)

with open(args.morgane, 'r') as f:
    annotation_data_2 = json.load(f)


###########################
# Part 2: do the comparison


comparison_result = []

for i, (annotation_1_i, annotation_2_i) in enumerate(zip(annotation_data_1['documents'], annotation_data_2['documents'])):
    if annotation_1_i['type'] != 'utterance':
        continue
    # if annotation_1_i['subject'] in CHI_LIST:
    #     labels_1_i = [annotation_1_i['label_1_a'], annotation_1_i['label_1_b'], annotation_1_i['label_1_c']]
    #     labels_2_i = [annotation_2_i['label_1_a'], annotation_2_i['label_1_b'], annotation_2_i['label_1_c']]
    #     labels_type = 1
    # elif annotation_1_i['subject'] in PAR_LIST:
    #     labels_1_i = [annotation_1_i['label_2_a'], annotation_1_i['label_2_b'], annotation_1_i['label_2_c']]
    #     labels_2_i = [annotation_2_i['label_2_a'], annotation_2_i['label_2_b'], annotation_2_i['label_2_c']]
    #     labels_type = 2
    # else:
    #     labels_type = 3
    #     # TODO: should we allow type-3?
    #     # raise KeyError("invalid subject: " + annotation_1_i['subject']);

    labels_1_C = '[' + ','.join([annotation_1_i['label_1_a'], annotation_1_i['label_1_b'], annotation_1_i['label_1_c']]) + ']'
    labels_1_M = '[' + ','.join([annotation_2_i['label_1_a'], annotation_2_i['label_1_b'], annotation_2_i['label_1_c']]) + ']'
    comparison_result.append([
        i,                          # ID
        annotation_1_i['turn'],     # utterance
        labels_1_C,                 # annotation-C
        labels_1_M,                 # annotation-M
        1,                          # list-ID, 1 or 2
        ])

    labels_2_C = '[' + ','.join([annotation_1_i['label_2_a'], annotation_1_i['label_2_b'], annotation_1_i['label_2_c']]) + ']'
    labels_2_M = '[' + ','.join([annotation_2_i['label_2_a'], annotation_2_i['label_2_b'], annotation_2_i['label_2_c']]) + ']'
    comparison_result.append([
        i,                          # ID
        annotation_1_i['turn'],     # utterance
        labels_2_C,                 # annotation-C
        labels_2_M,                 # annotation-M
        2,                          # list-ID, 1 or 2
    ])


with open(args.csvpath, 'w', newline='') as csvfile:
    #spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(['ID', 'utterance', 'annotation-charlie', 'annotation-morgane', 'list-ID'])
    spamwriter.writerows(comparison_result)
