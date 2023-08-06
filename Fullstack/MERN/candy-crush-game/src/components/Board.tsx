import React from 'react'
import { useAppSelector } from '../store/hooks';
import Tile from './Tile';

function Board() {
  const board = useAppSelector(({candyCrush: {board}}) => board);
  console.log('board seen', board);
  
  return (
    <div>
      {board.map(
        (candy:string, index:number) => (
        <Tile candy={candy} key={index} candyId={index}/>
        ))
      }
    </div>
  )
}

export default Board;
