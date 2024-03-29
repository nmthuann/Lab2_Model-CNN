from tensorflow import keras

# Alex Net (2012) + VGG (2014)
def create_model_2(input_shape):
    model = keras.models.Sequential([
        # # the first - Conv2D
        # keras.layers.Conv2D(filters=32, kernel_size=(3,3), strides=(1,1), activation='relu', padding='same'),
        # keras.layers.BatchNormalization(),
        # # keras.layers.MaxPool2D(pool_size=(2,2), strides=(1,1)),
        # # the second - Conv2D
        # keras.layers.Conv2D(filters=32, kernel_size=(3,3), strides=(2,2), activation='relu', padding="same"),
        # keras.layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
        # keras.layers.BatchNormalization(),
        #
        # # the first - Conv2D
        # keras.layers.Conv2D(filters=128, kernel_size=(3, 3), strides=(2, 2), activation='relu', padding='same'),
        # keras.layers.BatchNormalization(),
        # keras.layers.Conv2D(filters=128, kernel_size=(3, 3), strides=(2, 2), activation='relu', padding='same'),
        # keras.layers.BatchNormalization(),
        #
        # keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
        #
        # # the first - Conv2D
        # keras.layers.Conv2D(filters=256, kernel_size=(1, 1), strides=(2, 2), activation='relu', padding='same'),
        # keras.layers.Conv2D(filters=256, kernel_size=(3, 3), strides=(2, 2), activation='relu', padding='same'),
        # keras.layers.Conv2D(filters=256, kernel_size=(1, 1), strides=(2, 2), activation='relu', padding='same'),
        # keras.layers.BatchNormalization(),
        # keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
        #
        # keras.layers.Conv2D(filters=728, kernel_size=(1, 1), strides=(2, 2), activation='relu', padding='same'),
        # keras.layers.Conv2D(filters=728, kernel_size=(3, 3), strides=(2, 2), activation='relu', padding='same'),
        # keras.layers.Conv2D(filters=728, kernel_size=(1, 1), strides=(2, 2), activation='relu', padding='same'),
        # keras.layers.BatchNormalization(),
        # keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),

        keras.layers.Conv2D(filters=64, kernel_size=(1, 1), strides=(1, 1), activation='relu', padding='same'),
        keras.layers.MaxPool2D(pool_size=(2, 2), strides=(1, 1)),

        keras.layers.Conv2D(filters=128, kernel_size=(1, 1), strides=(1, 1), activation='relu', padding='same'),
        keras.layers.MaxPool2D(pool_size=(2, 2), strides=(1, 1)),

        keras.layers.Conv2D(filters=128, kernel_size=(1, 1), strides=(1, 1), activation='relu', padding='same'),


        keras.layers.Flatten(input_shape=(64,64,8)),# 64*64*8
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(2, activation='softmax')
    ])

    return model
