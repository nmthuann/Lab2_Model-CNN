import tensorflow as tf
from model import create_model

img_height = 224
img_width = 224
batch_size = 32

model = model = create_model((img_height, img_width, 3))

model.compile(loss='sparse_categorical_crossentropy', optimizer=tf.optimizers.SGD(learning_rate=0.001), metrics=['accuracy'])
model.summary()

model.load_weights('./chk_points/checkpoint_1')

test_ds = tf.keras.utils.image_dataset_from_directory(
    'test', labels='inferred',
    label_mode='int',
    color_mode='rgb',
    batch_size=batch_size,
    image_size=(img_height,img_width),
    shuffle=True,
    seed=6796013,
    interpolation='bilinear'
)

evaluation = model.evaluate(test_ds, return_dict=True)

print("[+] Result:")

for name, value in evaluation.items():
    print(f"{name}: {value:.4f}")
