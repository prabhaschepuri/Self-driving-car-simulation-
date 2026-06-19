# Addition of fully connected layers and pooling layers with pretrained MobileNetV2 model  

model=Sequential(
[
    pretrained_model,
    GlobalAveragePooling2D(),
    Dense(128,activation='relu'),
    Dense(64,activation='relu'),
    Dense(1) # Final output i.e steering 
]
)
model.compile(optimizer='adam', loss='mse')

# Model Training 

summary=model.fit(
    X_train,Y_train, epochs=10, batch_size=32, validation_data=(X_test,Y_test)
)
