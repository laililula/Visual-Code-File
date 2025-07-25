# ================================
# Game 클래스: 게임 상태 관리
# ================================
class Game:

    def __init__(self, board, first):
        self.board = board            # 게임 보드 (2차원 배열)
        self.first = first            # 선공 여부
        self.passed = False           # 마지막 턴에 패스했는지 여부

    # 사각형 (r1, c1) ~ (r2, c2)이 유효한지 검사 (합이 10이고, 네 변을 모두 포함)
    def isValid(self, r1, c1, r2, c2):
        sums = 0
        r1fit = c1fit = r2fit = c2fit = False

        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if self.board[r][c] != 0:
                    sums += self.board[r][c]
                    if r == r1:
                        r1fit = True
                    if r == r2:
                        r2fit = True
                    if c == c1:
                        c1fit = True
                    if c == c2:
                        c2fit = True
        return sums == 10 and r1fit and r2fit and c1fit and c2fit

    # ================================================================
    # ===================== [필수 구현] ===============================
    # 합이 10인 유효한 사각형을 찾아 (r1, c1, r2, c2) 튜플로 반환
    # 없으면 (-1, -1, -1, -1) 반환 (패스 의미)
    # ================================================================
    def calculateMove(self, _myTime, _oppTime):
        rows = len(self.board)
        cols = len(self.board[0])

        def getValidMoves(board):
            moves = []
            for r1 in range(rows):
                for c1 in range(cols):
                    for r2 in range(r1, rows):
                        for c2 in range(c1, cols):
                            sums = 0
                            r1fit = c1fit = r2fit = c2fit = False
                            for r in range(r1, r2+1):
                                for c in range(c1, c2+1):
                                    if board[r][c] != 0:
                                        sums += board[r][c]
                                        if r == r1: r1fit = True
                                        if r == r2: r2fit = True
                                        if c == c1: c1fit = True
                                        if c == c2: c2fit = True
                            if sums == 10 and r1fit and r2fit and c1fit and c2fit:
                                moves.append((r1, c1, r2, c2))
            return moves

        def applyMove(board, move):
            new_board = [row[:] for row in board]
            r1, c1, r2, c2 = move
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    new_board[r][c] = 0
            return new_board

        def evaluate(board):
            # 평가 함수: 내 차례에서 가능한 수 개수 - 상대 차례에서 가능한 수 개수
            my_moves = len(getValidMoves(board))
            # 상대 턴 시뮬레이션용, 상대가 많이 못두게 하는 게 좋음
            # 그냥 내 차례 관점에서 평가하므로 상대 턴에서는 같은 evaluate 씀
            return my_moves

        best_move = (-1, -1, -1, -1)
        best_value = -float('inf')

        for move in getValidMoves(self.board):
            next_board = applyMove(self.board, move)
            # 상대 차례, 상대가 둘 수 있는 수들 중 최소값 찾기 (내가 최대화하려는 값)
            opp_moves = getValidMoves(next_board)
            if not opp_moves:
                # 상대가 수를 못 두면 최고점
                value = float('inf')
            else:
                # 상대가 둔 다음 내 차례에서 가능한 수 평가
                value = min(evaluate(applyMove(next_board, opp_move)) for opp_move in opp_moves)

            if value > best_value:
                best_value = value
                best_move = move

        return best_move

    # =================== [필수 구현 끝] =============================

    # 상대방의 수를 받아 보드에 반영
    def updateOpponentAction(self, action, _time):
        self.updateMove(*action, False)

    # 주어진 수를 보드에 반영 (칸을 0으로 지움)
    def updateMove(self, r1, c1, r2, c2, _isMyMove):
        if r1 == c1 == r2 == c2 == -1:
            self.passed = True
            return
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                self.board[r][c] = 0
        self.passed = False


# ================================
# main(): 입출력 처리 및 게임 진행
# ================================
def main():
    while True:
        line = input().split()

        if len(line) == 0:
            continue

        command, *param = line

        if command == "READY":
            # 선공 여부 확인
            turn = param[0]
            global first
            first = turn == "FIRST"
            print("OK", flush=True)
            continue

        if command == "INIT":
            # 보드 초기화
            board = [list(map(int, row)) for row in param]
            global game
            game = Game(board, first)
            continue

        if command == "TIME":
            # 내 턴: 수 계산 및 실행
            myTime, oppTime = map(int, param)
            ret = game.calculateMove(myTime, oppTime)
            game.updateMove(*ret, True)
            print(*ret, flush=True)
            continue

        if command == "OPP":
            # 상대 턴 반영
            r1, c1, r2, c2, time = map(int, param)
            game.updateOpponentAction((r1, c1, r2, c2), time)
            continue

        if command == "FINISH":
            break

        assert False, f"Invalid command {command}"


if __name__ == "__main__":
    main()