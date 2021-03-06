nets = {}
nets['yolov2']={'shapes':[[3,3,3,32],[3,3,32,64],[3,3,64,128],[1,1,128,64],[3,3,64,128],[3,3,128,256],[1,1,256,128],[3,3,128,256],[3,3,256,512],[1,1,512,256],[3,3,256,512],[1,1,512,256],
                  [3,3,256,512],[3,3,512,1024],[1,1,1024,512],[3,3,512,1024],[1,1,1024,512],[3,3,512,1024],[3,3,1024,1024],[3,3,1024,1024],[1,1,512,64],[3,3,1280,1024],[1,1,1024,125]],
               'layers':23,'type':'V2_VOC'}
nets['tiny_yolo']={'shapes':[[3,3,3,16],[3,3,16,32],[3,3,32,64],[3,3,64,128],[3,3,128,256],[3,3,256,512],[3,3,512,1024],[3,3,1024,1024],[1,1,1024,125]],
               'layers':9, 'type':'TINY_VOC'}


