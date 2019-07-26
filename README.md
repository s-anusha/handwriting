
**Steps for the ICR-Project on windows:**


* Install Pycharm- https://www.jetbrains.com/pycharm/download/#section=windows(professional edition) 
* Install Python 
  * Python 2, or Python 3. Preferred Python 3.5, or 3.6.
  * Note: Python’s latest release 3.7 is supported only by TensorFlow 1.13.1.
* Download the windows folder from github.
* Extract the folder
* Open the folder on Pycharm
  * Set Virtual Environment (Add python Interpreter) - File ->Settings ->Project (windows) ->Project Interpreter (show all). 
  * The installation of modules can be done by pip install requirements.txt at the terminal or PyCharm detects the requirements.txt file and asks permission for installation and installs it automatically.
  * Unzip the model.zip in “model” directory and remove the files from the new model subfolder created and paste on the outer model directory so the structure will be “model/ (snapshot files)”

* Running the project on Pycharm:
  * Go to the terminal, type the following command cd src
  * From the terminal, in the “src” directory, run python main.py ../test/TESTFILE.
  * TESTFILE is the name of an image file present in the test directory, e.g., test4.jpg.
  * The output is saved in summary.txt in the “out” directory.
  * The remaining sub-folders in the “out” directory are segmentation of each line of the given input image.

* For inferring with new images, add the downloaded file in the “test” directory and while running on the terminal change the name of the TESTFILE to that particular file.

**Steps for the ICR-Project on ubuntu:**(for word-beam search integration)

* Download python 3.5 or 3.6 in ubuntu.
* Download the folder linux from github..
* Open the project in Pycharm 
Setup the virtual environment as discussed above
* Install the modules present in requirements.txt as discussed above.
* Unzip the model.zip in “model” directory and remove the files from the new model subfolder created and paste on the outer model directory so the structure will be “model/ (snapshot files)”
* Running the project on Pycharm:
  * Go to the terminal, type the following command cd src
  * From the terminal, in the “src” directory, run python main.py ../test/TESTFILE.
  * TESTFILE is the name of an image file present in the test directory, e.g., test4.jpg.
  * The output is saved in summary.txt in the “out” directory.
  * The remaining sub-folders in the “out” directory are segmentation of each line of the given input image.

* For inferring with new images, add the downloaded file in the “test” directory and while running on the terminal change the name of the TESTFILE to that particular file.

