import { WritableDraft } from "immer/dist/internal";
import { formulaForMoveBelow } from "../../utils/formulas";

export const moveBelowReducer = (
    state: WritableDraft<{
        board: string[];
        boardSize: number;
        squareBeingReplaced: Element | undefined;
        squareBeingDragged: Element | undefined;
    }>
) => {
    const newBoard: string[] = [...state.board];
    const { boardSize } = state;

    let boardChanges: boolean = false;
    const formulaForMove: number = formulaForMoveBelow(boardSize);
    for (let i=0; i< formulaForMove; i++) {
        const firstROw = Array(boardSize).fill(0).map((_value, index: number) => index)
    }
    const isFirstRow = Array(boardSize).fill(0).map((_value: number, index: number) => index);
}