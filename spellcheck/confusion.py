import csv
import spellcheck

delMatrix = [];
subMatrix = [];
addMatrix = [];
revMatrix = [];

with open(spellcheck.DATA + '/del.csv', 'r') as f:
    thedata = csv.reader(f)
    for row in thedata:
        temp=[];
        for elem in row:
            if int(elem) == 0:  # Smoothing
                elem = int(elem) + 1
            temp.append(int(elem));
        delMatrix.append(temp);

with open(spellcheck.DATA + '/sub.csv', 'r') as f:
    thedata = csv.reader(f)
    for row in thedata:
        temp=[];
        for elem in row:
            if int(elem) == 0:  # Smoothing
                elem = int(elem) + 1
            temp.append(int(elem));
        subMatrix.append(temp);

with open(spellcheck.DATA + '/add.csv', 'r') as f:
    thedata = csv.reader(f)
    for row in thedata:
        temp=[];
        for elem in row:
            if int(elem) == 0:  # Smoothing
                elem = int(elem)+ 1
            temp.append(elem);
        addMatrix.append(temp);

with open(spellcheck.DATA + '/rev.csv', 'r') as f:
    thedata = csv.reader(f)
    for row in thedata:
        temp=[];
        for elem in row:
            if int(elem) == 0:  # Smoothing
                elem = int(elem) + 1
            temp.append(int(elem));
        revMatrix.append(temp);

def delMat(x,y):
    return delMatrix[ord(x) - ord('a')][ord(y) - ord('a')];

def subMat(x,y):
    return subMatrix[ord(x) - ord('a')][ord(y) - ord('a')];

def addMat(x,y):
    return addMatrix[ord(x) - ord('a')][ord(y) - ord('a')];

def revMat(x,y):
    return revMatrix[ord(x) - ord('a')][ord(y) - ord('a')];