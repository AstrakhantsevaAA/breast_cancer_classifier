import pickle
from os import path as osp
import pandas as pd
import os
import ast


def get_meta(path):
    info = pd.read_csv(path)
    info['files'] = info["files"].apply(lambda s: list(ast.literal_eval(s)))
    return info


def create_exam_list(meta):
    exam_list = []
    for i in range(len(meta)):
        idx = meta['ID'][i]
        l_cc = meta['files'].iloc[i][0][0][0][0].split('/')[-1]
        l_mlo = meta['files'].iloc[i][0][0][0][1].split('/')[-1]
        r_cc = meta['files'].iloc[i][0][1][0][0].split('/')[-1]
        r_mlo = meta['files'].iloc[i][0][1][0][1].split('/')[-1]

        exam_dict = {
            'id': [idx],
            'horizontal_flip': 'NO',
            'L-CC': [f'{l_cc}.png'],
            'L-MLO': [f'{l_mlo}.png'],
            'R-CC': [f'{r_cc}.png'],
            'R-MLO': [f'{r_mlo}.png'],
        }

        exam_list.append(exam_dict)
    return exam_list


def pickle_to_file(file_name, data, protocol=pickle.HIGHEST_PROTOCOL):
    with open(file_name, 'wb') as handle:
        pickle.dump(data, handle, protocol)


def main():
    meta_path = osp.join("data", "processed", "new_meta_patients.csv")
    meta = get_meta(meta_path)
    exam_list = create_exam_list(meta)
    filename_output = "data/processed/exam_list_before_cropping.pkl"
    print(exam_list[:2])
    pickle_to_file(filename_output, exam_list)


if __name__ == "__main__":
    main()
