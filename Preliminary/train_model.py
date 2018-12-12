# train_model.py

import  numpy as np
from alexnet import alexnet

WIDTH = 80
HEIGHT = 60
LR = 1e-3       #学习效率
EPOCHS = 8
MODEL_NAME = 'py-car-{}-{}-{}-epochs.model'.format(LR,'alexnetv2',EPOCHS)

model = alexnet(WIDTH,HEIGHT,LR)

train_data = np.load('training_data_v2.npy')

train = train_data[:-500]
test = train_data[-500:]

X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
test_y = [i[1] for i in train]

model.fit({'input':X},{'targets':Y},n_epoch=EPOCHS,
          validation_set=({'input':test_x},{'targets':test_y}),
          snapshot_step=500,show_metric=True,run_id=MODEL_NAME)

# tensorboard --logdir=foo:C:\Users\q\OneDrive\PythonCode\OpenCV-Tensorflow\Preliminary\log

model.save(MODEL_NAME)
