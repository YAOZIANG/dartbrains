import os, glob
import datalad.api as dl

localizer_path = r'C:\Users\qq844\Desktop\dartbrains\course\data'
ds = dl.Dataset(localizer_path)

# 下载 sub-S01 的原始数据
ds.get(os.path.join(localizer_path, 'sub-S01'))

# 下载元数据
ds.get(glob.glob(os.path.join(localizer_path, '*.json')))
ds.get(glob.glob(os.path.join(localizer_path, '*.tsv')))
ds.get(os.path.join(localizer_path, 'phenotype'))

# 下载前 20 个被试的 fmriprep 数据
file_list = glob.glob(os.path.join(localizer_path, '*', 'fmriprep', 'sub*'))
file_list.sort()
for f in file_list[:20]:
    ds.get(f)