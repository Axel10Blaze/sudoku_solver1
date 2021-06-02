import pytesseract
import cv2
import numpy as np
import util
import sudoku

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img = cv2.imread("test2.jpg")
height = 540
width = 540

img = cv2.resize(img, (width, height))


boxes = util.splitImageToBoxes(img)


board = []
arr = []
for i in range(len(boxes)):
    processed_block = util.preprocessImage(boxes[i])
    cropped_block = boxes[i][5:55, 5:55]
    board.append(pytesseract.image_to_string(cropped_block, config="--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789"))
# print(board)
dict1 = {'\x0c': 0, '1\n\x0c': 1, '2\n\x0c': 2, '3\n\x0c': 3, '4\n\x0c': 4,
         '5\n\x0c': 5, '6\n\x0c': 6, '7\n\x0c': 7, '8\n\x0c': 8, '9\n\x0c': 9}

for i in range(len(board)):
    if board[i] in dict1.keys():
        board[i] = dict1[board[i]]
board = np.asarray(board)
board = board.reshape(9, 9)

board_copy = board.astype(int)
print(board_copy)
sudoku.solve_sudoku(board)
print(board)
for i in range(len(board)):
    for j in range(len(board)):
        if int(board_copy[i][j]) == 0:
            cv2.putText(img, str(board[i][j]), util.getcoordinate(i, j), cv2.FONT_HERSHEY_PLAIN, 2.5, (0, 0, 255), 2, cv2.LINE_AA)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


