import React, { useEffect } from 'react'
import { useAppDispatch, useAppSelector } from './store/hooks'
//import { updateBoard } from "./store"
import { createBoard } from './utils/createBoard';

function App() {

  const dispatch = useAppDispatch();

  const board = useAppSelector(({candyCrush: {board}}) => board);
  const boardSize = useAppSelector(
    ({candyCrush: {boardSize}}) => boardSize
  );

  useEffect(()=> {
    //dispatch(updateBoard(createBoard(boardSize)))
    console.log(createBoard(boardSize));
  }, []);
  
  return (
    <div>
      App
    </div>
  )
}

export default App
