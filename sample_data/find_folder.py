from os import path as osp
import os


def main():
    path = osp.join("data", "external", "MMG")
    folders = os.listdir(path)

    for fold in folders:
        if fold == 'four_views':
            continue
        path_fold = osp.join(path, fold)
        if osp.isdir(path_fold):
            for subfold in os.listdir(path_fold):
                path_subfold = osp.join(path_fold, subfold)
                if osp.isdir(path_subfold):
                    for file in os.listdir(path_subfold):
                        if file.endswith(".258"):
                            print(fold)

if __name__ == "__main__":
    main()
