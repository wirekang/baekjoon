const right = 0
const left = 1
const up = 2
const down = 3

const board = []
let size = 0
let max = 0

;(() => {
	const fs = require("fs")
	const strings = fs.readFileSync("/dev/stdin").toString().split(/ |\n/)
	size = parseInt(strings[0], 10)
	for (let i = 0; i < size * size; i += 1) {
		board[i] = parseInt(strings[i + 1], 10)
	}
})()

const get = (x, y) => board[x + y * size]
const set = (x, y, i) => {
	board[x + y * size] = i
}

function saveMax() {
	max = Math.max(
		board.reduce((a, b) => Math.max(parseInt(a, 10), parseInt(b, 10))),
		max
	)
}

function setBoard(preBoard) {
	for (let i = 0; i < size * size; i += 1) {
		board[i] = preBoard[i]
	}
}

function recursive(n, direction) {
	const preBoard = Array.from(board)
	switch (direction) {
		case right:
			doRight()
			break
		case left:
			doLeft()
			break
		case up:
			doUp()
			break
		case down:
			doDown()
			break
	}
	makePositive()
	n += 1
	if (n === 5) {
		saveMax()
		return
	}

	recursive(n, right)
	recursive(n, up)
	recursive(n, left)
	recursive(n, down)
	setBoard(preBoard)
}

function doRight() {
	for (let y = 0; y < size; y += 1) {
		for (let x = size - 2; x >= 0; x -= 1) {
			doMove(x, y, right)
		}
	}
}

function doLeft() {
	for (let y = 0; y < size; y += 1) {
		for (let x = 1; x < size; x += 1) {
			doMove(x, y, left)
		}
	}
}

function doUp() {
	for (let x = 0; x < size; x += 1) {
		for (let y = 1; y < size; y += 1) {
			doMove(x, y, up)
		}
	}
}

function doDown() {
	for (let x = 0; x < size; x += 1) {
		for (let y = size - 2; y >= 0; y -= 1) {
			doMove(x, y, down)
		}
	}
}

function doMove(x, y, direction) {
	const cur = get(x, y)
	if (cur === 0) {
		return
	}

	const nextPos = getNextPos(x, y, direction)
	if (isOk(nextPos.x, nextPos.y)) {
		const next = get(nextPos.x, nextPos.y)
		if (next === 0) {
			set(x, y, 0)
			set(nextPos.x, nextPos.y, cur)
			doMove(nextPos.x, nextPos.y, direction)
			return
		}

		if (next === cur) {
			set(x, y, 0)
			set(nextPos.x, nextPos.y, cur * -2)
		}
	}
}

function getNextPos(x, y, direction) {
	switch (direction) {
		case right:
			return { x: x + 1, y }
		case left:
			return { x: x - 1, y }
		case up:
			return { x, y: y - 1 }
		case down:
			return { x, y: y + 1 }
	}
}

function isOk(x, y) {
	return x >= 0 && y >= 0 && x < size && y < size
}

function makePositive() {
	for (let i = 0; i < size * size; i += 1) {
		if (board[i] < 0) {
			board[i] = -1 * board[i]
		}
	}
}

recursive(0, right)
recursive(0, up)
recursive(0, left)
recursive(0, down)
console.log(max)
