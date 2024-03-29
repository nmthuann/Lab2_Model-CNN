import os
import time
import tensorflow as tf
from tensorflow import keras
from model import create_model
from Model_2 import create_model_2

tf.config.threading.set_inter_op_parallelism_threads(8)
tf.config.threading.set_intra_op_parallelism_threads(8)

img_height = 224 # 224 299
img_width = 224 # 224
batch_size = 16 # 32

train_ds = tf.keras.utils.image_dataset_from_directory(
    'dataset_1000', labels='inferred',
    label_mode='int',
    color_mode='rgb',
    batch_size=batch_size,
    image_size=(img_height,img_width),
    shuffle=True,
    validation_split=0.1,
    seed=7982,
    subset='training',
    interpolation='bilinear'
)

validation_ds = tf.keras.utils.image_dataset_from_directory(
    'test', labels='inferred',
    label_mode='int',
    color_mode='rgb',
    batch_size=batch_size,
    image_size=(img_height,img_width),
    shuffle=True,
    validation_split=0.1,
    seed=4596,
    subset='validation',
    interpolation='bilinear'
)

test_ds = tf.keras.utils.image_dataset_from_directory(
    'test', labels='inferred',
    label_mode='int',
    color_mode='rgb',
    batch_size=batch_size,
    image_size=(img_height,img_width),
    shuffle=True,
    seed=132496,
    interpolation='bilinear'
)

train_ds_size = tf.data.experimental.cardinality(train_ds).numpy()
test_ds_size = tf.data.experimental.cardinality(test_ds).numpy()
validation_ds_size = tf.data.experimental.cardinality(validation_ds).numpy()
print("Training data size:", train_ds_size)
print("Test data size:", test_ds_size)
print("Validation data size:", validation_ds_size)

model = create_model((img_height, img_width, 3))

root_logdir = os.path.join(os.curdir, "logs\\fit\\")

def get_run_logdir():
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(root_logdir, run_id)

run_logdir = get_run_logdir()
tensorboard_cb = keras.callbacks.TensorBoard(run_logdir)

model.compile(loss='sparse_categorical_crossentropy',
                optimizer=tf.optimizers.SGD(learning_rate=0.001),
                metrics=['accuracy'])
model.summary()

earlystopping = keras.callbacks.EarlyStopping(monitor ="val_loss",
                                        mode ="min", patience = 10,
                                        restore_best_weights = True)

model.fit(train_ds,
            epochs=60,
            validation_data=validation_ds,
            validation_freq=1,
            callbacks=[tensorboard_cb, earlystopping])

evaluation = model.evaluate(test_ds, return_dict=True)

print("[+] Result:")

for name, value in evaluation.items():
    print(f"{name}: {value:.4f}")

model.save_weights('./chk_points/checkpoint_1')
