import { WritableDraft } from "immer/dist/internal";

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
    //const formau
}