import shutil
import numpy as np
import tqdm
import os
from yolov5.utils.google_utils import *
import splitfolders
from yolov5.detect import *
import subprocess
from pycocotools.coco import COCO
import yaml

CONFIG_PATH = "../"

def load_config(config_name):
    with open(os.path.join(CONFIG_PATH, config_name)) as file:
        config = yaml.safe_load(file)
    return config


class Yolo_model:
	def __init__(self, data_path, weights_path, output_path):
		self.data_path = data_path
		self.weights_path = weights_path
		self.output_path = output_path
    
	def preprocessData(self):
	    # Downloading yolov5x : other options: yolov5l, yolov5s, yolov5m

		attempt_download(self.weights_path) #weights_path = input/weights/yolov5x.pt #Could be yoloV5l or 5s etc

		filename = "annotations.json"
		data_source = COCO(annotation_file= os.path.join(os.path.normpath(self.data_path), filename)) #data_path = input/tacotrashdataset/data/
		

		# Chosen Categories: 
		'''
			 'Plastic bottle cap': 7
			 'Drink can': 12
			 'Other plastic': 29
			 'Plastic film': 36
			 'Other plastic wrapper': 39
			 'Unlabeled litter': 58
			 'Cigarette': 59
			 'Clear plastic bottle': 5
		'''

		# remapping label id to 0~7
		label_transfer = {5: 0, 7: 1, 12: 2, 29: 3, 36: 4, 39: 5, 58: 6, 59: 7}

		img_ids = data_source.getImgIds()

		catIds = data_source.getCatIds()
		categories = data_source.loadCats(catIds)
		categories.sort(key=lambda x: x['id'])
		classes = {}
		coco_labels = {}
		coco_labels_inverse = {}
		for c in categories:
		    coco_labels[len(classes)] = c['id']
		    coco_labels_inverse[c['id']] = len(classes)
		    classes[c['name']] = len(classes)

		class_num = {}

		
		save_base_path  = os.path.join(os.path.normpath(self.output_path), "tmp/labels")
		save_image_path = os.path.join(os.path.normpath(self.output_path), "tmp/labels")
		os.makedirs(save_base_path)
		os.makedirs(save_image_path)

		for index, img_id in tqdm.tqdm(enumerate(img_ids), desc='change .json file to .txt file'):
		    img_info = data_source.loadImgs(img_id)[0]
		    # Modify the path containing the folder to the file name
		    save_name = img_info['file_name'].replace('/', '_')
		    # Remove file extension
		    file_name = save_name.split('.')[0]
		    # Get the width and height of a single image
		    height = img_info['height']
		    width = img_info['width']
		    # The storage path of the converted txt file
		    save_path = save_base_path + file_name + '.txt'
		    is_exist = False  # Record whether the picture contains the target garbage type object
		    with open(save_path, mode='w') as fp:
		        # Find out the number set of garbage objects according to the picture number
		        annotation_id = data_source.getAnnIds(img_id)
		        boxes = np.zeros((0, 5))
		        if len(annotation_id) == 0:  # 集合大小為0
		            fp.write('')
		            continue
		        # Get tags in coco format
		        annotations = data_source.loadAnns(annotation_id)
		        lines = ''  # Record the label in yolo format after conversion
		        # Traverse the object tag set
		        for annotation in annotations:
		            # Get the label of the garbage object
		            label = coco_labels_inverse[annotation['category_id']]
		            if label in label_transfer.keys():
		                # If the garbage type belongs to the target garbage type, format conversion is performed
		                is_exist = True
		                box = annotation['bbox']
		                if box[2] < 1 or box[3] < 1:
		                    # Skip if there is no length or width data in the original label
		                    continue
		                # top_x,top_y,width,height==>cen_x,cen_y,width,height
		                box[0] = round((box[0] + box[2] / 2) / width, 6)
		                box[1] = round((box[1] + box[3] / 2) / height, 6)
		                box[2] = round(box[2] / width, 6)
		                box[3] = round(box[3] / height, 6)
		                label = label_transfer[label]  # Label mapping
		                if label not in class_num.keys():
		                    class_num[label] = 0
		                class_num[label] += 1
		                lines = lines + str(label)  # Storing tags first
		                for i in box:  # Restore location information
		                    lines += ' ' + str(i)
		                lines += '\n'  
		        fp.writelines(lines)
		    if is_exist:
		        # If the target type object exists, copy the image to the specified directory
		        shutil.copy(self.data_path + '{}'.format(img_info['file_name']), os.path.join(save_image_path, save_name))
		    else:
		        # If it does not exist, delete the generated label file
		        os.remove(save_path)

		'''
		Split Folder
			split into train, val, test (images & labels under each folder)
		'''
		splitfolders.ratio(os.path.join(os.path.normpath(self.output_path), "tmp"), output= os.path.join(os.path.normpath(self.output_path), "taco"), seed=1337, ratio=(.8, 0.1,0.1)) 

    def predict_yolo(self, config, input_image_path, trained_model_weights_path):
    	detect(config, input_image_path, trained_model_weights_path)

    	# cmd = 'python detect.py --weights weights/best.pt --view-img  --img 320 --conf 0.4 --source taco/test/images/batch_9_000004.jpg'
    	# q = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    	# out, err = q.communicate() 
    	# result = out.split('\n')
    	# for lin in result:
    	# 	if not lin.startswith('#'):
    	# 		print(lin)

DLtask = Yolo_model("/data", "",) # data_path: path for taco trash dataset, weights_path(for yolo pretrained weights", output_path -> where you want to write the test anf train folders
DLtask.preprocessData()
config = load_config("yolo_config.yaml")
DLtask.predict_yolo(config, "taco/test/images/batch_9_000004.jpg", ".pt") #config, input_image_path (for inference), trained_model_weights_path(trained model path)