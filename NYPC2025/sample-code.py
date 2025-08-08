from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Tuple
from itertools import combinations
import sys


class DiceRule(Enum):
    ONE = 0; TWO = 1; THREE = 2; FOUR = 3; FIVE = 4; SIX = 5
    CHOICE = 6; FOUR_OF_A_KIND = 7; FULL_HOUSE = 8
    SMALL_STRAIGHT = 9; LARGE_STRAIGHT = 10; YACHT = 11


@dataclass
class Bid:
    group: str        # 'A' 또는 'B'
    amount: int       # 입찰 금액


@dataclass
class DicePut:
    rule: DiceRule
    dice: List[int]


class GameState:
    MAX_POTENTIAL = {
        DiceRule.ONE: 5*1*1000,
        DiceRule.TWO: 5*2*1000,
        DiceRule.THREE: 5*3*1000,
        DiceRule.FOUR: 5*4*1000,
        DiceRule.FIVE: 5*5*1000,
        DiceRule.SIX: 5*6*1000,
        DiceRule.CHOICE:      5*6*1000,
        DiceRule.FOUR_OF_A_KIND: 5*6*1000,
        DiceRule.FULL_HOUSE:      5*6*1000,
        DiceRule.SMALL_STRAIGHT: 15000,
        DiceRule.LARGE_STRAIGHT: 30000,
        DiceRule.YACHT:          50000,
    }

    def __init__(self):
        self.dice: List[int] = []
        self.rule_score: List[Optional[int]] = [None]*12
        self.bid_score: int = 0

    def get_total_score(self) -> int:
        basic = sum(s for s in self.rule_score[0:6] if s is not None)
        bonus = 35000 if basic >= 63000 else 0
        combo = sum(s for s in self.rule_score[6:12] if s is not None)
        return basic + bonus + combo + self.bid_score

    def bid(self, success: bool, amt: int):
        self.bid_score += (-amt if success else amt)

    def add_dice(self, new: List[int]):
        self.dice.extend(new)

    def use_dice(self, put: DicePut):
        assert self.rule_score[put.rule.value] is None, "Rule already used"
        for d in put.dice:
            self.dice.remove(d)
        self.rule_score[put.rule.value] = GameState.calculate_score(put)

    @staticmethod
    def calculate_score(put: DicePut) -> int:
        r, d = put.rule, put.dice
        if r in (DiceRule.ONE, DiceRule.TWO, DiceRule.THREE,
                 DiceRule.FOUR, DiceRule.FIVE, DiceRule.SIX):
            face = r.value + 1
            return sum(x for x in d if x == face) * 1000
        if r is DiceRule.CHOICE:
            return sum(d) * 1000
        if r is DiceRule.FOUR_OF_A_KIND:
            return sum(d)*1000 if any(d.count(i) >= 4 for i in range(1,7)) else 0
        if r is DiceRule.FULL_HOUSE:
            cnts = [d.count(i) for i in range(1,7)]
            return sum(d)*1000 if (3 in cnts and 2 in cnts) or 5 in cnts else 0
        if r is DiceRule.SMALL_STRAIGHT:
            has = [d.count(i) > 0 for i in range(1,7)]
            if has[0:4] == [True]*4 or has[1:5] == [True]*4 or has[2:6] == [True]*4:
                return 15000
            return 0
        if r is DiceRule.LARGE_STRAIGHT:
            has = [d.count(i) > 0 for i in range(1,7)]
            if has[0:5] == [True]*5 or has[1:6] == [True]*5:
                return 30000
            return 0
        if r is DiceRule.YACHT:
            return 50000 if any(d.count(i) == 5 for i in range(1,7)) else 0
        raise AssertionError("Invalid rule")


class Game:
    def __init__(self):
        self.my_state = GameState()
        self.opp_state = GameState()
        self.opp_history: List[Tuple[int,int]] = []

    def calculate_bid(self, dice_a: List[int], dice_b: List[int]) -> Bid:
        potA = self._estimate_max(dice_a)
        potB = self._estimate_max(dice_b)
        if potA > potB:
            group, my_pot, opp_pot = "A", potA, potB
        else:
            group, my_pot, opp_pot = "B", potB, potA

        diff = my_pot - opp_pot
        pred_ratio = 0.5
        if self.opp_history:
            ratios = [b/(abs(d)+1) for d,b in self.opp_history]
            pred_ratio = sum(ratios)/len(ratios)
        predicted_opp_bid = int(abs(diff)*pred_ratio)
        bid_amt = predicted_opp_bid + int(abs(diff)*0.1) + 1
        bid_amt = max(1, min(bid_amt, int(my_pot*0.4), 100000))
        return Bid(group, bid_amt)

    def _estimate_max(self, dice_roll: List[int]) -> int:
        best = 0
        for idx, used in enumerate(self.my_state.rule_score):
            if used is None:
                s = GameState.calculate_score(DicePut(DiceRule(idx), dice_roll))
                best = max(best, s)
        return best

    # ================================ [필수 구현: YACHT 우선 모으기] ================================
    def calculate_put(self) -> DicePut:
        dice = self.my_state.dice[:]

        # 0) YACHT 규칙이 아직 사용되지 않았다면 우선 타겟으로 설정
        if self.my_state.rule_score[DiceRule.YACHT.value] is None:
            target_rule = DiceRule.YACHT

            # 1) 즉시 Yacht 달성 가능 여부 검사
            best_immediate = 0
            best_subset = dice[:5]
            for subset in combinations(dice, 5):
                sc = GameState.calculate_score(DicePut(target_rule, list(subset)))
                if sc > best_immediate:
                    best_immediate = sc
                    best_subset = list(subset)
            if best_immediate > 0:
                return DicePut(target_rule, best_subset)

            # 2) 그렇지 않으면, 가장 자주 나온 숫자 우선 보존
            cnts = [dice.count(i) for i in range(1,7)]
            common_face = cnts.index(max(cnts)) + 1
            # 보존할 주사위: common_face, 나머지를 버릴 5개 선정
            non_common = [d for d in dice if d != common_face]
            if len(non_common) >= 5:
                to_put = non_common[:5]
            else:
                # 부족하면 common_face로 채움
                to_put = non_common + [common_face] * (5 - len(non_common))
            return DicePut(target_rule, to_put)

        # 3) 그 외 규칙은 기존 모으기 전략 사용
        # (직전 보너스 기여도 전략 or 즉시 점수 전략 등)
        # 여기서는 즉시 점수 우선 + 미래 기여도 전략을 간단히 유지
        # 3-1) 즉시 점수 가능한 모든 규칙/조합 검사
        best_immediate = 0
        best_rule_im = None
        best_subset_im = dice[:5]
        for idx, used in enumerate(self.my_state.rule_score):
            if used is None:
                rule = DiceRule(idx)
                for subset in combinations(dice, 5):
                    sc = GameState.calculate_score(DicePut(rule, list(subset)))
                    if sc > best_immediate:
                        best_immediate = sc
                        best_rule_im = rule
                        best_subset_im = list(subset)
        if best_immediate > 0:
            return DicePut(best_rule_im, best_subset_im)

        # 3-2) 미래 기여도 기반 규칙 선택
        best_rule = None
        best_metric = -1.0
        for idx, used in enumerate(self.my_state.rule_score):
            if used is None:
                rule = DiceRule(idx)
                # 기존 _rule_metric 함수 사용
                metric = self._rule_metric(dice, rule)
                if metric > best_metric:
                    best_metric = metric
                    best_rule = rule

        assert best_rule is not None
        # 3-3) 기여도 낮은 주사위부터 5개 버리기
        contrib = self._die_contributions(dice, best_rule)
        dice_idx = list(enumerate(dice))
        dice_idx.sort(key=lambda x: contrib[x[1]])
        to_put = [dice[i] for i,_ in dice_idx[:5]]
        return DicePut(best_rule, to_put)
    # ============================== [필수 구현 끝] ==============================

    def _rule_metric(self, dice: List[int], rule: DiceRule) -> float:
        cnts = [dice.count(i) for i in range(1,7)]
        maxpot = GameState.MAX_POTENTIAL[rule]
        if rule in (DiceRule.ONE, DiceRule.TWO, DiceRule.THREE,
                    DiceRule.FOUR, DiceRule.FIVE, DiceRule.SIX):
            face = rule.value + 1
            ratio = cnts[face-1] / 5
        elif rule is DiceRule.YACHT:
            ratio = cnts.count(max(cnts)) / 5
        elif rule is DiceRule.FOUR_OF_A_KIND:
            ratio = max(cnts) / 4
        elif rule is DiceRule.FULL_HOUSE:
            triple = max((c for c in cnts if c>=2), default=0)
            pair   = max((c for c in cnts if c>=2 and c!=triple), default=0)
            ratio = (min(triple,3) + min(pair,2)) / 5
        elif rule is DiceRule.SMALL_STRAIGHT:
            seqs = ([1,2,3,4],[2,3,4,5],[3,4,5,6])
            best = max(sum(1 for x in seq if cnts[x-1]>0) for seq in seqs)
            ratio = best / 4
        elif rule is DiceRule.LARGE_STRAIGHT:
            seqs = ([1,2,3,4,5],[2,3,4,5,6])
            best = max(sum(1 for x in seq if cnts[x-1]>0) for seq in seqs)
            ratio = best / 5
        elif rule is DiceRule.CHOICE:
            ratio = 1.0
        else:
            ratio = 0.0
        return ratio * maxpot

    def _die_contributions(self, dice: List[int], rule: DiceRule) -> dict:
        contrib = {}
        cnts = [dice.count(i) for i in range(1,7)]
        if rule in (DiceRule.ONE, DiceRule.TWO, DiceRule.THREE,
                    DiceRule.FOUR, DiceRule.FIVE, DiceRule.SIX):
            face = rule.value + 1
            for d in dice:
                contrib[d] = 1.0 if d == face else 0.0
        elif rule in (DiceRule.YACHT, DiceRule.FOUR_OF_A_KIND):
            common = max(range(1,7), key=lambda i: cnts[i-1])
            for d in dice:
                contrib[d] = cnts[d-1] / cnts[common-1] if cnts[common-1]>0 else 0.0
        elif rule is DiceRule.FULL_HOUSE:
            triples = [i for i,c in enumerate(cnts,1) if c>=3]
            pairs   = [i for i,c in enumerate(cnts,1) if c>=2 and i not in triples]
            for d in dice:
                if d in triples:
                    contrib[d] = 1.0
                elif d in pairs:
                    contrib[d] = 0.7
                else:
                    contrib[d] = 0.0
        elif rule in (DiceRule.SMALL_STRAIGHT, DiceRule.LARGE_STRAIGHT):
            seqs = (
                [1,2,3,4] if rule is DiceRule.SMALL_STRAIGHT else [1,2,3,4,5],
                [2,3,4,5] if rule is DiceRule.SMALL_STRAIGHT else [2,3,4,5,6],
            )
            best_seq = max(seqs, key=lambda seq: sum(1 for x in seq if cnts[x-1]>0))
            for d in dice:
                contrib[d] = 1.0 if d in best_seq else 0.0
        elif rule is DiceRule.CHOICE:
            for d in dice:
                contrib[d] = 1.0
        else:
            for d in dice:
                contrib[d] = 0.0
        return contrib

    def update_get(self, da, db, myb: Bid, oppb: Bid, me: str):
        potA = self._estimate_max(da)
        potB = self._estimate_max(db)
        diff = potA - potB if me=="A" else potB - potA
        self.opp_history.append((diff, oppb.amount))

        if me=="A":
            self.my_state.add_dice(da); self.opp_state.add_dice(db)
        else:
            self.my_state.add_dice(db); self.opp_state.add_dice(da)
        self.my_state.bid(myb.group==me, myb.amount)
        og = "B" if me=="A" else "A"
        self.opp_state.bid(oppb.group==og, oppb.amount)

    def update_put(self, put: DicePut):
        self.my_state.use_dice(put)

    def update_set(self, put: DicePut):
        self.opp_state.use_dice(put)


def main():
    game = Game()
    dice_a = [0]*5; dice_b = [0]*5; my_bid = Bid("",0)

    while True:
        try:
            line = input().strip()
            if not line:
                continue
            cmd, *args = line.split()
            if cmd == "READY":
                print("OK"); continue
            if cmd == "ROLL":
                sa, sb = args
                for i, c in enumerate(sa): dice_a[i] = int(c)
                for i, c in enumerate(sb): dice_b[i] = int(c)
                my_bid = game.calculate_bid(dice_a, dice_b)
                print(f"BID {my_bid.group} {my_bid.amount}")
                continue
            if cmd == "GET":
                g, og, os = args
                game.update_get(dice_a, dice_b, my_bid, Bid(og, int(os)), g)
                continue
            if cmd == "SCORE":
                put = game.calculate_put()
                game.update_put(put)
                print(f"PUT {put.rule.name} {''.join(map(str, put.dice))}")
                continue
            if cmd == "SET":
                r, sd = args
                game.update_set(DicePut(DiceRule[r], [int(c) for c in sd]))
                continue
            if cmd == "FINISH":
                break
            print(f"Invalid command: {cmd}", file=sys.stderr); sys.exit(1)
        except EOFError:
            break


if __name__ == "__main__":
    main()