from mmdet.apis import init_detector, inference_detector, show_result
import json
import os
import xlwt

config_file = '/media/shijiawei/program/mmdetection/configs/faster_rcnn_r101_spikelet.py'
checkpoint_file = '/media/shijiawei/program/mmdetection/work_dirs/faster_rcnn_r101_fpn_1x-200-1115/epoch_1000.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

img_path = '/media/shijiawei/program/mmdetection/data/coco/test80/'

#get test filenames from json
datapath = './data/coco/annotations/instances_test2017.json'
jsondata = json.load(open(datapath))

imgs = []
filename = []
re = os.listdir(img_path)
print(img_path)
re.sort()
for i in re:
    img = img_path + i
    imgs.append(img)
    filename.append(i)

print(imgs)


workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0,0, label = 'filename')
worksheet.write(0,1, label = 'number')
worksheet.write(0,2, label = 'category')
workbook.save('spikelet_number.xls')

for i in range(len(imgs)):
    result= inference_detector(model, imgs[i])
    show_result(imgs[i], result, model.CLASSES, out_file='spikelet_number/result/result%s' % (filename[i]))
    b=list(result)
    number = len(b[0]) + len(b[1])
    if len(b[0]) >= len(b[1]):
        category = 'indica'
    else:
        category = 'japonica'
    worksheet.write(i+1, 0, label='%s'%filename[i])
    worksheet.write(i+1, 1, label='%s'%number)
    worksheet.write(i+1, 2, label='%s'%category)
    workbook.save('spikelet_number.xls')
    print(i)
print('work done')
