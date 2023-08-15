import { configureStore, createSlice, PayloadAction } from "@reduxjs/toolkit";

const initialState : {
    board: string[];
    boardSize: number;
} = {
    board: [],
    boardSize: 8 // set board size here
}

const candyCrushSlice = createSlice({
    name: "candyCrush",
    initialState,
    reducers: {
        updateBoard: (state, action: PayloadAction<string[]>) => {
            state.board = action.payload;
        },
        moveBelow: moverBelowReducer
    },
});

export const store = configureStore({
    reducer: {
        candyCrush: candyCrushSlice.reducer
    }
})

export const {} = candyCrushSlice.actions

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;