from tensorflow import keras

def create_model(input_shape):
    model = keras.models.Sequential([

        # Alex Net (2012)
        # # the first - Conv2D
        # keras.layers.Conv2D(filters=96, kernel_size=(11,11), strides=(4,4), activation='relu', input_shape=input_shape, padding='same'),
        # keras.layers.BatchNormalization(),
        # keras.layers.MaxPool2D(pool_size=(3,3), strides=(2,2)),
        #
        # # the second - Conv2D
        # keras.layers.Conv2D(filters=256, kernel_size=(5,5), strides=(1,1), activation='relu', padding="same"),
        # keras.layers.BatchNormalization(),
        # keras.layers.MaxPool2D(pool_size=(3,3), strides=(2,2)),
        #
        # # the third - Conv2D
        # keras.layers.Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), activation='relu', padding="same"),
        # keras.layers.BatchNormalization(),
        #
        # # the fourth - Conv2D
        # keras.layers.Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), activation='relu', padding="same"),
        # keras.layers.BatchNormalization(),
        #
        # # the fifth - Conv2D
        # keras.layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), activation='relu', padding="same"),
        # keras.layers.BatchNormalization(),
        # #original implement of alexnet
        # keras.layers.MaxPool2D(pool_size=(3,3), strides=(2,2)),
        #
        # keras.layers.Flatten(),
        # keras.layers.Dense(4096, activation='relu'),
        # keras.layers.Dropout(0.2),
        # keras.layers.Dense(4096, activation='relu'),
        # keras.layers.Dropout(0.2),
        # keras.layers.Dense(2, activation='softmax')



        keras.layers.Conv2D(filters=64, kernel_size=(1, 1), strides=(2, 2), input_shape=input_shape, activation='relu', padding='same'),
        keras.layers.MaxPool2D(pool_size=(2, 2)),

        keras.layers.Conv2D(filters=128, kernel_size=(1, 1), strides=(1, 1), activation='relu', padding='same'),
        keras.layers.MaxPool2D(pool_size=(2, 2)),

        keras.layers.Conv2D(filters=128, kernel_size=(1, 1), strides=(1, 1), activation='relu', padding='same'),

        keras.layers.Flatten(),  # 64*64*8
        keras.layers.Dense(1024, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(512, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(2, activation='softmax')


        # model effcientNet
        # keras.applications.efficientnet.EfficientNetB3(include_top=False,
        #                                                   weights="imagenet",
        #                                                   input_shape=input_shape,
        #                                                   pooling="max"
        #                                                   ),
        # keras.layers.Flatten(),  # 64*64*8
        # keras.layers.Dense(1024, activation='relu'),
        # keras.layers.Dropout(0.2),
        # keras.layers.Dense(512, activation='relu'),
        # keras.layers.Dropout(0.2),
        # keras.layers.Dense(128, activation='relu'),
        # keras.layers.Dropout(0.2),
        # keras.layers.Dense(2, activation='softmax')
    ])

    return model
