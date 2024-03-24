function solution(board) {
    let OCnt = 0, XCnt = 0;
    let OWin = 0, XWin = 0;
    
    for (let i = 0; i < 3; i++) {
        // row
        if (board[i] === 'OOO') {
            OWin++;
        } else if (board[i] === 'XXX') {
            XWin++;
        }
        // col
        if ((board[0][i] + board[1][i] + board[2][i]) === 'OOO') {
            OWin++;
        } else if ((board[0][i] + board[1][i] + board[2][i]) === 'XXX') {
            XWin++;
        }
        // cnt
        for (let j = 0; j < 3; j++) {
            if (board[i][j] === 'O') {
                OCnt++;
            } else if (board[i][j] === 'X') {
                XCnt++;
            }
        }
    }
    // diagonal
    if (board[0][0] + board[1][1] + board[2][2] ===  'OOO') {
        OWin++;
    } else if (board[0][0] + board[1][1] + board[2][2] ===  'XXX') {
        XWin++;
    }
    if (board[0][2] + board[1][1] + board[2][0] ===  'OOO') {
        OWin++;
    } else if (board[0][2] + board[1][1] + board[2][0] ===  'XXX') {
        XWin++;
    }

    if (XCnt > OCnt) {
        return 0;
    } else if (OCnt > XCnt + 1) {
        return 0;
    } else if (OWin === 1 && XWin === 1) {
        return 0;
    } else if (OWin && (OCnt !== XCnt + 1)) {
        return 0;
    } else if (XWin && (OCnt !== XCnt)) {
        return 0;
    } else {
        return 1;
    }
}