import numpy as np

X = []
Y = []

correction = 0.15

for i in range(len(df)):

    center_path = df.iloc[i, 0]
    left_path   = df.iloc[i, 1]
    right_path  = df.iloc[i, 2]

    steering = float(df.iloc[i, 3])

    X.append(preprocessed(center_path))
    Y.append(steering)

    flipped_1=cv.flip(cv.imread(center_path),1)
    
    X.append(preprocessed_aug(flipped_1))
    Y.append(-steering)

    X.append(preprocessed(left_path))
    Y.append(steering + correction)

    flipped_2=cv.flip(cv.imread(center_path),1)

    X.append(preprocessed_aug(flipped_2))
    Y.append(-(steering + correction))

    X.append(preprocessed(right_path))
    Y.append(steering - correction)

    flipped_3=cv.flip(cv.imread(right_path),1)

    X.append(preprocessed_aug(flipped_3))
    Y.append(-(steering - correction))

X_data = np.array(X)
Y_data = np.array(Y)

print(X_data.shape)
print(Y_data.shape)
