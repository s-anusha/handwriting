# Handwritten Page Recognition

#### Tested with:
- Python 3.7.3
- TensorFlow 1.14.0
- OpenCV 4.1.0.25
- Pyspellchecker 0.5.0

#### How to run:
- Open project root at terminal.
- `cd src`
- `python main.py path_to_test_image`

#### Output:
- The output is stored in the out directory as summary.txt.
- Each subdirectory in out represents one line of the page as recognized by the method, numbered in order.
- Each image in each subdirectory represents one word in that line, as recognized by the method, numbered in order. 

#### Note:
- This project combines page segmentation and word recognition.
- A snapshot of the trained word segmentation model is stored in the model directory.
- Retraining the model in this project is not possible.
- Instead, train the model in simplehtr and replace the existing snapshot with the new one.
