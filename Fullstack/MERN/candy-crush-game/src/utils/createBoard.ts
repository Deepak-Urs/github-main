import { candies } from "./candyData"

export const createBoard = (boardSize: number = 9) => 
Array(boardSize*boardSize).fill(null).map(
    () => candies[Math.floor(Math.random())*candies.length]
)