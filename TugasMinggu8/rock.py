import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Tentukan path ke dataset lokal
dataset_path = "./rockpaperscissors"

# Penerapan ImageDataGenerator untuk Normalisasi & Splitting Data (80:20)
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

# Generator Data Latih (Training)
train_generator = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)

# Generator Data Validasi (Validation)
validation_generator = train_datagen.flow_from_directory(
    dataset_path,
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

# Membangun Arsitektur Model CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(3, activation='softmax')
])

model.summary()

# Kompilasi Model
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# Proses Pelatihan Model (Model Fitting)
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=10
)

# Evaluasi Performa Model Terhadap Data Validasi
val_loss, val_acc = model.evaluate(validation_generator)
print(f'\nValidation loss: {val_loss}, Validation accuracy: {val_acc}\n')

# Prediksi Hasil Model pada Gambar Validasi Baru
predictions = model.predict(validation_generator)
print("Output Probabilitas Prediksi Tiap Kelas:")
print(predictions)

plt.figure(figsize=(12, 4))
# Plot Accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

# Plot Loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()