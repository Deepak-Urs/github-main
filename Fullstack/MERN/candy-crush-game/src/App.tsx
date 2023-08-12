import React, { useEffect } from 'react'
import Board from './components/Board';
import { useAppDispatch, useAppSelector } from './store/hooks'
//import { updateBoard } from "./store"
import { createBoard } from './utils/createBoard';
import { formulaForColumnOfFour, formulaForColumnOfThree, generateInvalidMoves } from './utils/formulas';
import { checkForRowOfFour, checkForRowOfThree, isColumnOfFour, isColumnOfThree } from './utils/moveCheckLogic';

function App() {

  const dispatch = useAppDispatch();

  const board = useAppSelector(({candyCrush: {board}}) => board);
  const boardSize = useAppSelector(
    ({candyCrush: {boardSize}}) => boardSize
  );
  console.log('board seen', board);
  
  useEffect(()=> {
    //dispatch(updateBoard(createBoard(boardSize)))
    console.log(createBoard(boardSize));
  }, [boardSize, dispatch]);

  useEffect(() => {
    const timeout = setTimeout(() => {
      const newBoard = [...board];
      isColumnOfFour(newBoard, boardSize, formulaForColumnOfFour(boardSize));
      isColumnOfThree(newBoard, boardSize, formulaForColumnOfThree(boardSize))
      checkForRowOfFour(newBoard, boardSize, generateInvalidMoves(boardSize, true))
      checkForRowOfThree(newBoard, boardSize, generateInvalidMoves(boardSize))
      dispatch(updateBoard(newBoard))
    }, 150);
    return () => clearInterval(timeout)
  }, [board, boardSize, dispatch])
  
  return (
    <div className='flex item-center justify-center h-screen'>
      <Board />
    </div>
  )
}

export default App
