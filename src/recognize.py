from __future__ import division
from __future__ import print_function

import cv2
from DataLoader import Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess
import os
from spellchecker import SpellChecker


class FilePaths:
    "filenames and paths to data"
    fnCharList = '../model/charList.txt'
    fnInfer = '../out/'

def infer(model, fnImg):
    "recognize text in image provided by file path"
    img = preprocess(cv2.imread(fnImg, cv2.IMREAD_GRAYSCALE), Model.imgSize)
    batch = Batch(None, [img])
    (recognized, probability) = model.inferBatch(batch, True)
    print('Recognized:', '"' + recognized[0] + '"')
    print('Probability:', probability[0])
    return recognized[0], probability[0]

def recognize():
    decoderType = DecoderType.BestPath
    model = Model(open(FilePaths.fnCharList).read(), decoderType, mustRestore=True)
    folderNumber = 0
    file = open('../out/summary.txt', 'w')
    file.close()
    spell = SpellChecker()
    if os.path.isdir(FilePaths.fnInfer):
        probability = 0
        count = 0
        while os.path.isdir(FilePaths.fnInfer + str(folderNumber) + '/'):
            folder = FilePaths.fnInfer + str(folderNumber) + '/'
            fileNumber = 0
            while os.path.isfile(folder + str(fileNumber) + '.png'):
                file = folder + str(fileNumber) + '.png'
                print(file)
                word, wordProbability = infer(model, os.path.abspath(file))
                probability += wordProbability
                count += 1
                misspelled = spell.unknown([word])
                file = open('../out/summary.txt', 'a')
                if len(misspelled) is not 0:
                    for item in misspelled:
                        word = spell.correction(item)
                file.write(word + ' ')
                file.close()
                fileNumber += 1
            folderNumber += 1
            file = open('../out/summary.txt', 'a')
            file.write('\n')
            file.close()
        probability = probability / count
        print('Average page probability: ', probability)
