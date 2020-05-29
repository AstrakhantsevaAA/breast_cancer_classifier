import png
import pydicom
from os import path as osp
import glob
import pandas as pd
import tqdm
import ast


def get_meta(path):
    info = pd.read_csv(path)
    info['files'] = info["files"].apply(lambda s: list(ast.literal_eval(s)))
    return info


def save_dicom_image_as_png(
        dicom_filename,
        png_filename,
        bitdepth=12
):
    """
    Save 12-bit mammogram from dicom as rescaled 16-bit png file.
    :param dicom_filename: path to input dicom file.
    :param png_filename: path to output png file.
    :param bitdepth: bit depth of the input image. Set it to 12 for 12-bit mammograms.
    """
    image = pydicom.dcmread(dicom_filename).pixel_array
    with open(png_filename, 'wb') as f:
        writer = png.Writer(
            height=image.shape[0],
            width=image.shape[1],
            bitdepth=bitdepth,
            greyscale=True
        )
        writer.write(f, image.tolist())


def main():
    meta_path = osp.join("sample_data", "new_meta_patients.csv")
    meta = get_meta(meta_path)
    path_dicom = osp.join("data", "raw", "Patients")
    path_output = osp.join("data", "processed", "Patients")

    for i in tqdm.tqdm(range(len(meta))):
        for side in [0, 1]:
            for view in [0, 1]:
                path = meta['files'].iloc[i][0][side][0][view]
                fname = path.split('/')[-1]
                print(osp.join(path_dicom, path), osp.join(path_output, f'{fname}.png'))
                save_dicom_image_as_png(osp.join(path_dicom, path), osp.join(path_output, f'{fname}.png'))


if __name__ == "__main__":
    main()

